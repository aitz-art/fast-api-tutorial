
FROM python:3.9


WORKDIR /dist


COPY ./requirements.txt /dist/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /dist/requirements.txt


COPY ./app /dist/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
