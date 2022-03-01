FROM python:3.9
FROM nikolaik/python-nodejs:latest

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y
RUN git clone -b master https://github.com/nodejs/node /root/node
WORKDIR /root/node
RUN apt-get -y install curl gnupg 
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash - 
RUN apt-get -y install nodejs 
RUN npm install
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN npm start
RUN mkdir /app/
COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

CMD python3 main.py
