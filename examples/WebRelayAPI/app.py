import flask
from flask_cors import CORS
from flask import request, jsonify,render_template
import os
import OpenWRT.GPIO as GPIO

PINS={
    "R1": 2,
    "R2": 3,
    "R3": 14,
    "R4": 15
}

relay_state={
    "R1":0,
    "R2":0,
    "R3":0,
    "R4":0,
}
gpio={}

def pin_init():
    for p in PINS:
        gpio[p]=GPIO.setup(PINS[p],GPIO.OUTPUT,reverse_state=True,initial_state=0)
def gpio_cleanup():
        for p in PINS:
            gpio[p].cleanup()

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/hello-world',methods=['GET','POST'])
def hello_world():
    return "Hello World !!"

@app.route('/status',methods=['GET'])
def status():
    return relay_state
@app.route('/status/<relay>',methods=['GET'])
def relay_status(relay):
    if relay in PINS:
        return str(relay_state[relay])
    else:
        return "Bad Request",400

@app.route('/set',methods=['GET','POST'])
def set():
    if 'relay' in request.args and 'state' in request.args:
        gpio[request.args["relay"]].write(int(request.args['state']))
        relay_state[request.args['relay']]=int(request.args['state'])
        return "OK"
    else:
        return "Bad Request",400       
@app.route('/set/<relay>/<state>',methods=['GET','POST'])
def relay_set(relay,state):
    if (int(state)==1 or int(state)==0) and (relay in PINS):
        gpio[relay].write(int(state))
        relay_state[relay]=int(state)
        return "OK"
    return "Bad Request",400
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    try:
        pin_init()
        app.run(host="0.0.0.0",port=5000)
    except KeyboardInterrupt:
        exit()