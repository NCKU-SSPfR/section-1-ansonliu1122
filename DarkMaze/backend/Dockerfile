# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt


COPY ./src /app/src
COPY ./test /app/test
COPY ./python3.11 /app/python3.11

RUN useradd --create-home appuser
RUN chown -R appuser:appuser /app
USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]