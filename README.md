# Scalingo multi app template

## Development

### Run the full stack

- Install docker and docker-compose
- Run `docker-compose build`
- Run `docker-compose up -d`

You can now access the app at http://localhost:8000

### Frontend

To avoid errors in your local environment:

- Install nodejs on your system
- Run `cd web`
- Run `npm install`

### API

To avoid errors in your local environment:

- Install python and pipenv on your system
- Install mariadb/mysql client lib on your system
- Run `cd api`
- Run `pipenv install --dev`

## Production

- Follow this guide for more details https://scalingo.com/blog/monorepo
- On scalingo, create 3 apps: `api`, `web` and `server` and sync them with your repo
- For each of these, add to its env variables `PROJECT_DIR=[dir of the app source code]` so scalingo knows where to start building
- On the `api` app, setup a MySQL addon and make sure that in your env you have `DATABASE_URL` setup to point to that db
- Then, push your changes to the right upstream in order to make scalingo deploy your new code
