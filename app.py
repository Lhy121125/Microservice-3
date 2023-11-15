from flask import Flask
from send_email import publish

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, from Docker!\nWe will use this to deploy application service!"

@app.route("/email")
async def send_email():
    publish("dz2506@columbia.edu","test from docker","test email")
    return {"message":"Success"}
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)