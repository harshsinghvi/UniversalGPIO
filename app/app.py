import flask
from flask import request, jsonify
import sqlite3
import requests
import os
import flask_monitoringdashboard as dashboard
import OpenWRT.GPIO as GPIO

PINS={
    "R0": 2,
    "R1": 3,
    "R2": 14,
    "R3": 15
}

relay_state={
    "R0":0,
    "R1":0,
    "R2":0,
    "R3":0,
}
gpio={}

def pin_init():
    for p in PINS:
        gpio[p]=GPIO.setup(PINS[p],GPIO.OUTPUT,reverse_state=True,initial_state=0)


app = flask.Flask(__name__)
app.config["DEBUG"] = True
dashboard.bind(app)

@app.route('/hello-world',mothods=['GET','POST'])
def hello_world():
    return "Hello World !!"

@app.route('/status',methods=['GET'])
def status():
    return relay_state
@app.route('/status<relay>',methods=['GET'])
def relay_status(relay)
    if relay in PINS:
        return relay_state[relay]
    else:
        return "Bad Request",400
@app.route('/set/<relay>/<state>',mothods=['GET','POST'])
def relay_set(relay,state):
    if (state == 1 or state == 0) and (relay in PINS):
        gpio[relay].write(state)
        relay_state[relay]=state
        return "OK"
    return "Bad Request",400
@app.route('/set',methods=['GET','POST'])
def set():
    if 'relay' in request.args and 'status' in request.args:
        gpio[request.args["relay"]].write(request.args['state'])
        relay_state[request.args['relay']]=request.args['state']
        return "OK"
    else:
        return "Bad Request",400
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    pin_init()
    app.run(host="0.0.0.0",port=5000)
