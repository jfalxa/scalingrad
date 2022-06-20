#!/bin/bash

cd web
npm run dev &

cd ../api
python manage.py runserver

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT