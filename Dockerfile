FROM python:3.9.7

COPY ./app /app

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 80

ENTRYPOINT ["flask"]

CMD ["run", "--host", "0.0.0.0", "--port", "80"]