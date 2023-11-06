
## 🧱  Setting Up the Project Locally
  ##### create virtual environment

  ```
  $ python -m venv venv
  ```

  ##### environment activation

  ```
  $ .\venv\Scripts\activate
  ```

  **(mac/linux)**
  ```
  $ source venv/bin/activate
  ```

  ##### dependency installation 

  ```
  $ pip install -r .\requirements.txt
  ```

  ##### makemigratoins
  ```
    $ python manage.py makemigrations authentication
    $ python manage.py makemigrations api
  ```

  ##### migrate
  ```
    $ python manage.py migrate
  ```

  ##### overload settings with environment variables
  it will convert terminal variables into environment variables
  ```$ 
  set -a; source .env.local; set +a;
  ```

  ##### launch the backend server
  ```
    $ python manage.py runserver
  ```

  ##### If you need to create a user (admin)
  ```
    $ python manage.py createsuperuser
  ```

<br>

## 💡 Setting up Precommit
It's important to enforce code styling and formatting. we use **[pre-commit](consistent_codebase.md)**. before each commit we do linting and formatting.

<br>


## 📦 Start project locally with Docker
  ##### docker-compose (recommended)
    ```
      $ docker-compose up -d --build
      $ docker-compose exec api python manage.py migrate
      $ docker-compose exec api python manage.py createsuperuser
    ```

  ##### build and run image
    ```
      $ docker build -t boilerplate_back .
      $ docker run -it -d --name boilerplate_back -v "./:/home/app" -p 8000:8000 boilerplate_back python manage.py runserver 0.0.0.0:8000
      $ docker exec -it boilerplate_back bash
      $ python manage.py migrate
      $ python manage.py createsuperuser
    ```

<br>

## 🚢 Deploying back in Production Environment
```
  $ ./scripts/run-compose-prod.sh
```