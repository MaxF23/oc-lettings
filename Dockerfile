FROM python


WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

ADD . /app/

EXPOSE 8000

CMD ["pytest"]

