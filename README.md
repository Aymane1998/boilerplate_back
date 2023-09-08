# Boilerplate BACK

## La documentation
Veuillez trouver la documentation

## Allumer le projet en local
  ##### cration de l'environnement virtuel

  ```$ python -m venv venv```

  ##### activation de l'environnement

  ```$ .\venv\Scripts\activate```

  **(mac/linux)**
  ```$source venv/bin/activate```

  ##### installation des dependances 

  pip install -r .\requirements.txt

  ##### makemigratoins

  - python manage.py makemigrations authentication
  - python manage.py makemigrations api

  ##### migrate

  python manage.py migrate

  ##### surcharger les settings avec les variables d'environnement
  il va convertir les variables de terminal en variable d'environnement
    ```$ set -a; source .env.local; set +a;```

  ##### lancer le serveur backend

  python manage.py runserver

  ##### Si besoin de creer un user (admin)

  python manage.py createsuperuser


## Allumer le projet en local avec Docker
  ##### docker-compose (recommandé)
    docker-compose up -d
    docker-compose exec api python manage.py migrate
    docker-compose exec api python manage.py createsuperuser

  ##### build and run image
    docker build -t boilerplate_back .
    docker run -it -d --name boilerplate_back -v "./:/home/app" -p 8000:8000 boilerplate_back python manage.py runserver 0.0.0.0:8000
    docker exec -it boilerplate_back bash
    python manage.py migrate
    python manage.py createsuperuser

## Déploiment du back en Environnement Production
```./scripts/run-compose-prod.sh```