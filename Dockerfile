FROM python:3
WORKDIR /app
COPY . /app
ENV MYSQLHOST=localhost
ENV MYSQLUSERNAME=dev
ENV MYSQLPASSWORD=dev123
ENV MYSQLDB=dev
ENV APPHOST=localhost
ENV APPPORT=5000
ENV APPDEBUG=True
RUN pip install -r requirements.txt
CMD [ "app.py" ]
