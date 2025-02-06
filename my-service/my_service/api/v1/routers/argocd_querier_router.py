
from fastapi import FastAPI, Depends, HTTPException
from my_service.dependencies import get_token
from my_service.utils.logger import setup_logger
from fastapi import APIRouter
from my_service.argocd_client import ArgoClient
from my_service.config.config import settings

router = APIRouter(
    prefix="/arogocd",
    tags=["arogocd"],
)


logger = setup_logger()


app = FastAPI()



@router.get("/application_status")
async def application_status(token: str = Depends(get_token)):
    """Fetches all ArgoCD applications statuses

    Args:
        token (str, optional): _description_. Defaults to Depends(get_token).

    Returns:
        applications_data_conscise: concise application metadata json strucure
    """
    ##############################################################################
    # Please complete the fastapi route to get applications metadata from argocd #
    # Make sure to use argocd token for authentication                           #  
    ##############################################################################
    
    # async with ArgoClient(server=settings.ARGOCD_URL, token=token) as client:
    #     return await client.get_apps(project="default")

    async with ArgoClient(server=settings.ARGOCD_URL, token=token) as client:
        apps = await client.get_apps(project="default")
        # Format the response according to the specified structure
        formatted_apps = {
            "applications": [
                {
                    "application_name": app["metadata"]["name"],
                    "status": app["status"]["sync"]["status"]
                }
                for app in apps
            ]
        }
        return formatted_apps

@router.get("/list_projects")
async def list_projects(token: str = Depends(get_token)):
    """Fetches all argocd projects names and namespaces to which they are configured

    Args:
        token (str, optional): _description_. Defaults to Depends(get_token).
    Returns:
        projects_data_conscise: concise argocd projects metadata json strucure
    """

    ##########################################################################
    # Please complete the fastapi route to get projects metadata from argocd #
    # Make sure to use argocd token for authentication                       #  
    ##########################################################################

    async with ArgoClient(server=settings.ARGOCD_URL, token=token) as client:
        projects = await client.list_projects()
        formatted_projects = {
            "projects": [
                {
                    "project_name": project.get("metadata", {}).get("name", ""),
                    "namespace": project.get("spec", {}).get("destinations", [{}])[0].get("namespace", "default")
                }
                for project in projects
            ]
        }
        return formatted_projects
