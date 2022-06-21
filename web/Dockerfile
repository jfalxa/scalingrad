# setup environment
FROM node:latest as env

ARG HOST
ENV HOST $HOST

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

# start dev env
FROM env as dev
CMD ["npm", "run", "dev"]
