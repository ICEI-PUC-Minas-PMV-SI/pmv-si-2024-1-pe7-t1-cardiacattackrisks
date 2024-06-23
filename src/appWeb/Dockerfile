FROM python:latest AS flask_app
WORKDIR /flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /flask/
ENTRYPOINT ["gunicorn", "app:app"]