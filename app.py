from flask import Flask,request
from send_email import *

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

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)