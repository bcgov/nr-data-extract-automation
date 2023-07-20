docker build -t query-automation-demo .

docker run --name query_container query-automation-demo

docker cp query_container:/extracts/rar_output.xlsx //objectstore.nrs.bcgov/datafoundations_test/rar_query_output/rar_output_from_docker.xlsx