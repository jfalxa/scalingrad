#!/bin/bash

cd web
npm run build

cd ../api
gunicorn core.wsgi --log-file -
