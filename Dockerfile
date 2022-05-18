FROM python

WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app/

ENV PORT=8000

CMD python manage.py runserver 0.0.0.0:$PORT

