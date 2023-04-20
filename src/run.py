#!env/bin/python3
from app import flaskapp

#flaskapp.run(host="0.0.0.0", threaded=True, debug=True)
flaskapp.run(port=8080, debug=True)

#Use this for login SQL injection- ' OR '1'='1
# Use this for Search SQL injection- ' OR 1=1 --
