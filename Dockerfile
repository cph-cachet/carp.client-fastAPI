FROM python:3.7

MAINTAINER Alban Maxhuni, PhD <almax@dtu.dk>

# Set the working directory to /carp_fastapi
WORKDIR /carp_fastapi

# update
RUN apt update && apt upgrade -y

# install
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install uvicorn

# install the dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy the current directory contents into the container at /carp_fastapi
ADD . /carp_fastapi

COPY . /carp_fastapi

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--reload", "--port", "8091"]