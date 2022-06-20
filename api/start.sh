#!/bin/bash

gunicorn core.wsgi --log-file -
