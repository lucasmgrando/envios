docker container run -d \
-p 8000:8000 \
--network net \
--name dynamodb \
-v dynamodb:/root \
--rm amazon/dynamodb-local

sam local start-api --docker-network net
