

## ArgoCD Apps
- Contains the Argocd App CRD for the FastAPI service and the Nginx service
- There are available in the directory `infra-k8s/argocd-apps`

## Services Manifests
- Manifest files for both the FastAPI service and the Nginx service
- There are also available in the directory `infra-k8s/k8s-app`

## Additional Configuration
- Added `ConfigMap` and `Secret` for the FastAPI service

##  Screenshots of the application
### List Applications Endpoint
![List of Applications](/images/list_apps.png)

### List Projects Endpoint
![List of Projects](/images/list_projects.png)

### Argocd Landing Page Showing the 2 Applications
![List of Projects](/images/argocd_landing.png)

### Argocd of the My Service App (FastAPI service) and its components
![List of Projects](/images/my_service_app.png)

### Logs of the FastAPI service
![List of Projects](/images/logs.png)

### Swagger UI of the FastAPI deployed to "my-service.local"
![List of Projects](/images/swagger.png)

### Swagger UI of the Nginx deployed to "nginx.local"
![List of Projects](/images/nginx.png)

### References
- [Argocd Instllation](https://argo-cd.readthedocs.io/en/stable/getting_started/)