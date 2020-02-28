FROM python:3
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update; apt-get install -y sqlite3 libsqlite3-dev
ADD . /
RUN ./init_db.sh
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
