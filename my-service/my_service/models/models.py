from pydantic import BaseModel
from typing import Dict, List, Optional


class HealthCheckResponse(BaseModel):
    status_code: int
    message: str


class ArgoCDCreds(BaseModel):
    username: str
    password: str


class Application(BaseModel):
    application_name: str
    status: str


class ApplicationsResponse(BaseModel):
    applications: List[Application]


class Project(BaseModel):
    project_name: str
    namespace: str


class ProjectsResponse(BaseModel):
    projects: List[Project]
