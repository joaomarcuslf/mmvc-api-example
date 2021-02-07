# mmvc-api-example

MMVC (Model-Manager-View-Controller), is an extension of the MVC pattern, but it extracts and encapsulates the business logic and model-based logic into another class called Manager.

![Actions Workflow](https://github.com/joaomarcuslf2/mmvc-api-example/workflows/Flask/badge.svg)

## How to Start Development

1. Copy ```sample.env.dev``` to ```.env.dev``` and rename the variables if you need
2. Build the images and run the containers:

    ```sh
    docker-compose up -d --build
    docker-compose exec api python run.py create_db # Only needed the first time
    docker-compose exec api python run.py seed_db # Only needed the first time
    ```

    - API: [http://localhost:5000/api/v1/users](http://localhost:5000/api/v1/users)

## Useful Commands

```
docker-compose exec client npm run test
docker-compose exec api pytest -v
docker-compose exec api pip install -r requirements.txt
docker-compose exec api python run.py seed_db
docker-compose exec api python -m pylint application helpers models resources run.py
docker-compose exec api python -m autopep8 --in-place --aggressive --aggressive application/config.py  application/__init__.py helpers/http_status.py helpers/user_responses.py models/__init__.py resources/__init__.py  resources/test_user_resource.py  resources/test_users_resource.py  resources/user_resource.py  resources/users_resource.py run.py
```
