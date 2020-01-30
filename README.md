# officially_public
It's public official data and it's going to be more public

# To load data

# To build a (Dockerized) website:
docker build -t officially_public .
docker run --detach=false --publish=8000:80 --env-file .env.prod officially_public
