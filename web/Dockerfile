FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /neoprospectaProject
WORKDIR /neoprospectaProject
ADD requirements.txt /neoprospectaProject/
RUN pip install -r requirements.txt
ADD . ../neoprospectaProject/
