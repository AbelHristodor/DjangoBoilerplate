FROM python:3.6

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    wget \
    gettext \
    libxmlsec1-dev \
    && rm -rf /vat/lib/apt/lists/*

ENV DOCKERIZE_VERSION v0.4.0
RUN wget --no-verbose https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
WORKDIR /usr/src/app

RUN pip3 install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /usr/src/app

CMD ["./scripts/run_app.sh"]