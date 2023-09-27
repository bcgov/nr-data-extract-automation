# nrs-query-automation

## Objective: 
Automate the process of executing daily database queries, generating tabular reports in the .xlsx format, and storing them in object storage for easy access via GeoDrive.

[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](<Redirect-URL>)

## Basic Requirements:
* OpenShift
* Docker 
* WSL2

### Step 1 - Build and test Docker image locally
```sh
docker build -t nrs-query-automation .
```
```sh
docker run --env-file=.env --name query_container nrs-query-automation
```
### Step 2 - Log in to OpenShift and navigate to project
```sh
oc login --token=[your-token] --server=https://api.silver.devops.gov.bc.ca:6443
```
```sh
oc project c2b678-prod
```
### Step 3 - Deploy the Oracle Service
[NR Oracle Service](https://github.com/bcgov/nr-oracle-service)

### Step 4 - Upload the Docker image 
```sh
oc apply -f imagestream.yaml
```
### Step 5 - Create OpenShift secrets 
```sh
oc create -f secrets.yaml
```
### Step 6 - Build container with required resources, secrets, env variables, etc
```sh
oc apply -f deployment.yaml
```
### Step 7 - Confirm the pod works
```sh
oc describe pod nrs-query-automation-[pod-name]
```
```sh
oc logs nrs-query-automation-[pod-name]
```
### Step 8 - Schedule cron job
```sh
oc apply -f cronjob.yaml --validate=false
```

