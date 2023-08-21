docker build -t nrs-query-automation .

docker run --env-file=.env --name query_container nrs-query-automation

docker run -d --name query_container -p 4001:4001 nrs-query-automation

docker cp query_container:/extracts/rar_output.xlsx //objectstore.nrs.bcgov/datafoundations_test/rar_query_output/rar_output_from_docker.xlsx

docker rm query_container

docker rmi -f nrs-query-automation