# TODO: Install the frontend dependency package into the app folder inside the container.

FROM python:3.11

RUN useradd --create-home appuser

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./src /app/src 

RUN chown -R appuser:appuser /app
USER appuser

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]