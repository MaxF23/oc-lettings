FROM python


WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip \
    pip3 install virtualenv \
    virtualenv venv \
    pip3 install -r requirements.txt

ADD . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

