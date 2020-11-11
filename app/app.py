import flask
from flask import request, jsonify
import sqlite3
import requests
import os
import flask_monitoringdashboard as dashboard
import OpenWRT.GPIO as GPIO

PINS={
    "R0":  
    "R1":  
    "R2":  
    "R3":   
}
state={
    "R0":0,
    "R1":0,
    "R2":0,
    "R3":0,
}
gpio={}
def pin_init():
    for p in PINS:
        gpio[p]=GPIO.pin

app = flask.Flask(__name__)
app.config["DEBUG"] = True
dashboard.bind(app)


@app.route('/hello-world',mothods=['GET','POST'])
def hello_world():
    return "Hello World !!"



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
