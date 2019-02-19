FROM python:3
WORKDIR /app
COPY . /app
ENV MYSQLHOST=localhost
ENV MYSQLUSERNAME=dev
ENV MYSQLPASSWORD=dev123
ENV MYSQLDB=dev
ENV APPHOST=0.0.0.0
ENV APPPORT=5000
ENV APPDEBUG=False
RUN pip install -r requirements.txt
CMD ["python", "app.py" ]
