# To build container: docker build --progress plain . -t app
# To run container: docker run -it -p 8000:8000 app
FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip && \
    pip install pipenv

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

COPY Pipfile Pipfile.lock ./

RUN pipenv sync -d

COPY . .

EXPOSE 8000

CMD /var/app/.venv/bin/uvicorn main:app --host 0.0.0.0
