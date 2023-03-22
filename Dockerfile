FROM python:3.11

RUN mkdir /app

ADD templates /app/

WORKDIR /app

#Copy files to image
COPY requirements.txt ./requirements.txt
COPY Makefile ./Makefile
COPY app.py ./app.py

RUN mkdir /templates


COPY templates/index.html ./templates/

COPY . .
# Installation of the dependecies
RUN make install

ENTRYPOINT ["python", "main.py"]

