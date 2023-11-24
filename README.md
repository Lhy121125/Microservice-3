# Microservice-3
Microservice 2 deploying with DockerHub

To install docker on ec2: ```sudo yum install docker```<br>
To start docker first time: ```sudo service docker start``` <br>
To pull the docker container from dockerhub: ```sudo docker pull dz2506/microservice-3-server```<br>
Build docker image on EC2 that specify version: ```sudo docker build -t dz2506/microservice-3-server:latest .```<br>
Run docker image on EC2 that specify version: ```sudo docker run -p 5001:5001 dz2506/microservice-3-server:latest```<br>
Note: REMEMBER to set the inbound rule for port 5001


GET```/notify/<id>``` Will send an email to the id's email.
GET```/status/<id>``` Will return status of this user's application.
POST```/email``` Will send a custom email to the specified address.

The app is now running on <ec2-3-85-14-246.compute-1.amazonaws.com:5001>