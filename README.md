# xperta.dk

This is the main website for xperta

It's made in django.

## Development
To run the website in dev mode do the follwing.

Create a .env.dev file in the root directory containing the following:

```
DEBUG=1
SECRET_KEY=
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

Remember to fill in SECRET_KEY

Next run the following commands to build the container and run it.

```
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up -d
```

To view the logs run the following

```
docker-compose -f docker-compose.dev.yml logs -f
```

## Production

The production website contains traefik as a reverse proxy, and TLS termination.

And NGINX in front of the django site, to handle requets and staticfiles.

To run the website in prod mode do the follwing.

Create a .env.prod file in the root directory containing the following:

```
DEBUG=0
SECRET_KEY=
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
RECIPIENT_ADDRESS=
```

Remember to fill in all the fields.

Next run the following commands to build the container and run it.

```
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d
```