# Microservice-3
Microservice 2 deploying with DockerHub

To install docker on ec2: ```sudo yum install docker```<br>
To start docker first time: ```sudo service docker start``` <br>
To pull the docker container from dockerhub: ```sudo docker pull <username>/<repo name>```<br>
Build docker image on EC2 that specify version: ```sudo docker build -t hl3648/microservice-3:amd64 .```<br>
Run docker image on EC2 that specify version: ```sudo docker run -p 5001:5001 hl3648/microservice-3:amd64```<br>
Note: REMEMBER to set the inbound rule for port 5001
