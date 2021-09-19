## tmob

**testing** (you need to have memcached installed locally)

python manage.py runsrever --settings=api.testing

**docker**

docker-compose build

docker-compose up

docker exec -it [container] sh

python manage.py migrate

python manage.py createsuperuser
