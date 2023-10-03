FROM  osgeo/gdal:ubuntu-small-3.6.3

RUN apt-get update && apt-get install -y python3-pip default-libmysqlclient-dev build-essential

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir  -r /app/requirements.txt

COPY ./ /app/

WORKDIR /app/source/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py crontab add && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
