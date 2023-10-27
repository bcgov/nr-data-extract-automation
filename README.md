# nrs-query-automation

## Objective: 
Automate the process of executing daily database queries, generating tabular reports in the .xlsx format, and storing them in object storage for easy access via GeoDrive.

[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](<Redirect-URL>)

## Basic Requirements:
* OpenShift
* Docker 
* WSL2

### Step 1 - Build Docker image locally
```sh
docker build -t nrs-query-automation:<tag> .
```
### Step 2 - Log in to OpenShift and navigate to project
```sh
oc project c2b678-prod
```
### Step 3 - Deploy the Oracle Service
[NR Oracle Service](https://github.com/bcgov/nr-oracle-service)

### Step 4 - Upload the Docker image 
```sh
docker push image-registry.apps.emerald.devops.gov.bc.ca/c2b678-prod/nrs-query-automation:<tag>
```
### Step 5 - Build container with required resources, secrets, env variables, etc
```sh
oc apply -f deployment.yaml
```
### Step 6 - Schedule cron job
```sh
oc apply -f cronjob.yaml 
```

