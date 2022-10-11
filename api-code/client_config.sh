#!/bin/bash
apt -y update
apt -y install git
apt -y install python3-pip
pip3 install "fastapi[all]"
apt -y install uvicorn
cd /home/ubuntu
git clone https://github.com/Danielcourvoisier/cloudsys-lab1-client.git
export SERVER_IP=34.65.95.230
export SERVER_PORT=8080
export APP_PORT=8080
cd /home/ubuntu/cloudsys-lab1-client/
uvicorn main:app --host 0.0.0.0 --port $APP_PORT