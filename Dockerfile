#
FROM python:3.11-slim

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt
COPY ./src /code

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
ENTRYPOINT ["python"]
CMD ["main.py"]