FROM nikolaik/python-nodejs:python3.7-nodejs12

# Install prereqs
RUN apt-get update
RUN apt-get -y install sudo
RUN apt-get -y install curl
RUN apt-get -y install software-properties-common
RUN apt-get -y install git

# Install Python dev dependencies
COPY ../requirements.txt ./
COPY ../requirements-dev.txt ./
RUN pip3 --default-timeout=1000 install -r requirements.txt
RUN pip3 --default-timeout=1000 install -r requirements-dev.txt
