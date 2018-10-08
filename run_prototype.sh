export FLASK_APP=prototype
export FLASK_ENV=development
export FLASK_DEBUG=true
export PYTHONPATH=/home/pi/Production/flask-service

flask run --host=0.0.0.0 --port=20080

#waitress-serve --port=8080 --call 'prototype:create_app'
