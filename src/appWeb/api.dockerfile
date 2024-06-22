FROM python:latest AS flask_app
WORKDIR /flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY ./App/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./App /flask/
CMD ["flask", "run"]