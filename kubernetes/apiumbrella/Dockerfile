FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y gnupg
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 367404D553B42995
RUN echo "deb http://dl.bintray.com/nrel/api-umbrella-ubuntu bionic main" | tee /etc/apt/sources.list.d/api-umbrella.list
RUN apt-get update
# RUN sh -c 'echo -e "2\n" | apt-get install -y api-umbrella'
