FROM python


WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]

