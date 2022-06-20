#!/bin/bash

cd ../api
gunicorn core.wsgi --log-file -
