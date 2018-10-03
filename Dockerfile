FROM python:3.5.6
MAINTAINER Vinod Kurpad "vikurpad@microsoft.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
COPY natgeo.h5 .
WORKDIR /app
RUN pip install -r requirements.txt
ENV KERAS_BACKEND=tensorflow
ENTRYPOINT ["python"]
CMD ["app.py"]