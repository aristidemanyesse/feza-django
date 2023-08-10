FROM ubuntu:22.04

RUN apt update \
&& apt-get install -y cron nano fuseiso \
&& apt-get install -y default-libmysqlclient-dev  -y \
&& apt install python3-pip -y --fix-missing
RUN apt-get install binutils libproj-dev gdal-bin -y

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

COPY ./requirements.txt /code/
COPY ./start.sh /code/
WORKDIR /code

RUN pip3 install -r requirements.txt

COPY ./applications /code/

EXPOSE 8000

USER root

RUN chmod +x ./start.sh

ENTRYPOINT ["./start.sh"]

# docker build -t hub.jool-tech.com/library/fenopjerci-server:1.0 .
# docker run hub.jool-tech.com/library/fenopjerci-server:2.8 .
# docker push hub.jool-tech.com/library/fenopjerci-server:1.0 
