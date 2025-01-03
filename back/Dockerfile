FROM python:3.11-slim as base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APPDIR=/opt/app
WORKDIR $APPDIR
FROM base as poetry

ENV POETRY_VERSION=1.4.0
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get install -y gcc && apt-get install -y curl
RUN curl --retry 10 --max-time 2 -sSL https://install.python-poetry.org | python3 -

FROM poetry as requirements-builder

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM base as final

RUN apt-get update && apt-get install -y git && pip install --upgrade pip

WORKDIR $APPDIR

COPY --from=requirements-builder $APPDIR/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --index-url https://nexus.intechs.by/repository/pypi-proxy/simple -r requirements.txt
COPY . .
COPY gunicorn.conf.py .
CMD bash -c "python manage.py migrate && gunicorn core.wsgi"
