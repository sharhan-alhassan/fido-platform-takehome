import aiohttp
from collections import namedtuple
from my_service.utils.logger import setup_logger

logger = setup_logger()

class ArgoInteractionError(Exception):
    """Any error in interacting with ArgoCD"""
    pass

AppUrl = namedtuple("AppUrl", ["name", "url"])

class ArgoClient:
    """Simple wrapper class to serve as ArgoCD client"""

    def __init__(self, server, token):
        self.base_url = f"http://{server}/api/v1"
        self.token = token
        self.server = server
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def request(self, method, endpoint, *args, **kwargs):
        """Generic request method with error handling."""
        url = f"https://{self.server}/api/v1/{endpoint}"
        logger.debug(f"Making request to ArgoCD: {method} {url}")
        
        headers = kwargs.pop('headers', {})
        headers['Authorization'] = f'Bearer {self.token}'
        kwargs['headers'] = headers
        
        if self.session is None:
            self.session = aiohttp.ClientSession()

        try:
            async with self.session.request(method, url, *args, ssl=False, **kwargs) as response:
                logger.debug(f"Response status code: {response.status}")
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            error_message = f"Could not complete request to ArgoCD, endpoint={endpoint}, method={method}, reason={str(e)}"
            logger.error(error_message)
            logger.error(f"Full exception: {e}")
            raise ArgoInteractionError(error_message) from e

    async def get(self, endpoint, *args, **kwargs):
        return await self.request("GET", endpoint, *args, **kwargs)

    async def post(self, endpoint, *args, **kwargs):
        return await self.request("POST", endpoint, *args, **kwargs)

    async def put(self, endpoint, *args, **kwargs):
        return await self.request("PUT", endpoint, *args, **kwargs)

    async def delete(self, endpoint, *args, **kwargs):
        return await self.request("DELETE", endpoint, *args, **kwargs)

    async def get_app(self, name) -> dict:
        """Get an app"""
        try:
            response = await self.get(f"applications/{name}")
            return response
        except ArgoInteractionError:
            return False

    async def get_apps(self, project) -> dict:
        """Get all apps in a given project"""
        params = {
            "project": [
                project,
            ]
        }
        response = await self.get("applications", params=params)
        return response["items"]

    async def delete_app(self, name) -> dict:
        """Delete an app"""
        response = await self.delete(f"applications/{name}")
        return response
    
    
    async def list_projects(self) -> list:
        """
        List all ArgoCD projects.
        
        Returns:
            list: A list of project objects containing metadata and specifications
        """
        try:
            response = await self.get("projects")
            # The response should contain an 'items' key with the list of projects
            if isinstance(response, dict) and 'items' in response:
                return response['items']
            return []
        except Exception as e:
            logger.error(f"Error listing ArgoCD projects: {str(e)}")
            raise