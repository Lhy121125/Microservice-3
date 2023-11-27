from flask import Flask,request
from send_email import *
import requests
import json

app = Flask(__name__)
info_url= ''

@app.route('/')
def hello_world():
    return "Hello, from Docker!\nWe will use this to deploy application service!"

@app.route("/email", methods = ['GET','POST'])
async def send_email():
    if request.method == 'GET':
        publish("dz2506@columbia.edu","test from docker","test email")
        return {"message":"Success"}
    if request.method == 'POST':
        json_message = request.json
        publish_json(json_message)
        return {"message":"Success"}

@app.route("/notify/<id>")
async def notify(id):
    url = info_url+'/users/'+id
    response = requests.get(url)
    data_r = response.json()
    data_r = json.loads(data_r)
    email = data_r['email']
    name = data_r['name']
    url = info_url+'/applications/'+id
    response = requests.get(url)
    applications = response.json()
    publish(email,"Application Status for "+name,applications)
    return "Success"

@app.route("/status/<id>")
def get_status(id):
    url = info_url+'/applications/'+id
    response = requests.get(url)
    applications = response.json()
    return applications







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)