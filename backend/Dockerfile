FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

RUN apt-get update -y && apt-get -y install cron && apt-get -y install vim && apt-get -y install dos2unix

# Install dependencies.
RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code

# Copy project code.
COPY . /code/

RUN touch /var/log/cron.log

RUN dos2unix /code/docker-entrypoint.sh && dos2unix /code/cronbash.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*
RUN chmod +x /code/docker-entrypoint.sh
RUN chmod +x /code/cronbash.sh
ENTRYPOINT ["/code/docker-entrypoint.sh"]