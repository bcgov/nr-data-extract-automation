oc login --token= --server=https://api.silver.devops.gov.bc.ca:6443

oc project c2b678-prod

oc port-forward service/nr-oracle-service 4001:80

oc get pods -o wide

oc get svc

oc get deployments

oc describe deployment nrs-query-automation

oc get pod -l app=nrs-query-automation -o jsonpath="{.items[0].spec.containers[0].image}"

kubectl config get-contexts 

kubectl config use-context c2b678-prod/api-silver-devops-gov-bc-ca:6443/abigail.michel@gov.bc.ca

oc apply -f cronjob.yaml --validate=false

oc get cronjob query-automation-cronjob

oc get jobs --selector=job-name=query-automation-cronjob

oc describe pod nrs-query-automation-5fdc44fbc8-d7qfw

oc logs nrs-query-automation-5fdc44fbc8-d7qfw










