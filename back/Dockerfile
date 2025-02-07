# Base stage
FROM python:3.11-slim as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APPDIR=/opt/app

WORKDIR $APPDIR

# Poetry installation stage
FROM base as poetry

ENV POETRY_VERSION=1.4.0 \
    POETRY_HOME=/opt/poetry \
    PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && \
    apt-get install -y gcc curl && \
    curl --retry 10 --max-time 2 -sSL https://install.python-poetry.org | python3 -

# Requirements building stage
FROM poetry as requirements-builder

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Final stage
FROM base as final

RUN apt-get update && \
    apt-get install -y git && \
    pip install --upgrade pip

WORKDIR $APPDIR

COPY --from=requirements-builder $APPDIR/requirements.txt .
RUN pip install -r requirements.txt && \
    pip install --index-url https://nexus.intechs.by/repository/pypi-proxy/simple -r requirements.txt

COPY . .
COPY gunicorn.conf.py .

CMD ["bash", "-c", "python manage.py migrate && gunicorn core.wsgi"]