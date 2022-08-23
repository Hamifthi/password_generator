#!/bin/bash

set -e


if [ "$1" == "rest" ]
then
    exec uvicorn main:app --host 0.0.0.0 --port 8000

elif [ "$1" == "test" ]
then
    exec python -m pytest

else
    exec "$@"
fi