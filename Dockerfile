FROM python:3.7.2-alpine3.9
WORKDIR /app
COPY . /app
ENV MYSQLHOST=localhost
ENV MYSQLUSERNAME=dev
ENV MYSQLPASSWORD=dev123
ENV MYSQLDB=dev
ENV MYSQLPORT=3306
ENV APPHOST=0.0.0.0
ENV APPPORT=5000
ENV APPDEBUG=False
RUN apk add mariadb-dev gcc python3-dev libc-dev
RUN pip install -r requirements.txt
CMD ["python", "app.py" ]
