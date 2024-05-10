FROM python:3.12.3

SHELL ["/bin/bash", "-c"]

# set enviroment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update
RUN apt -qy install openssh-client
RUN apt -qy install dos2unix


EXPOSE 80
EXPOSE 8000

WORKDIR /content

COPY . .

RUN pip install -r requirements.txt

CMD ["py","manage.py","runserver"]
