#!/bin/bash
apt -y update
apt -y install git
apt -y install python3-pip
pip3 install "fastapi[all]"
apt -y install uvicorn
cd /home/ubuntu
git clone https://github.com/Danielcourvoisier/cloudsys-lab1-server.git
export BUCKET_URL=https://storage.googleapis.com/cloudsys-lab1-bucket/test.json
export APP_PORT=8080
cd /home/ubuntu/cloudsys-lab1-server/
uvicorn main:app --host 0.0.0.0 --port $APP_PORT
