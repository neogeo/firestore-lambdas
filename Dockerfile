FROM ubuntu

WORKDIR build

RUN apt-get update
RUN apt-get install python-pip --assume-yes
RUN apt-get install zip --assume-yes

CMD ./create-lambda-zip.sh
