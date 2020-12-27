docker exec -it seg_app_flask_1 bash

curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username": "k1t1k", "password":"xyz"}' \
    http://0.0.0.0:5000/post