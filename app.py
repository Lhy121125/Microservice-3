from flask import Flask,request
from send_email import *
import requests
import json

app = Flask(__name__)

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

@app.route("/notify")
async def notify():
    data = json.loads(request.json)
    student_id = data['something']
    url = '/api/students/'+student_id+'/applications'
    response = requests.get(url)
    data_r = response.json()
    dates = data_r['something']
    email = 'a@b.com'
    publish(email,"Your Application Deadlines",dates)
    return "Success"

@app.route("/status")
def get_status():
    data = json.loads(request.json)
    student_id = data['something']
    url = '/api/students/'+student_id+'/applications'
    response = requests.get(url)
    return response.json()






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)