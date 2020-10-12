FROM python:3.8.6-slim-buster

COPY install-packages.sh .
RUN chmod +x ./install-packages.sh
RUN ./install-packages.sh

WORKDIR /cinephile

ADD requirements.txt /cinephile/requirements.txt
RUN pip install -r requirements.txt

ADD . /cinephile
RUN pip install -e .

ENV LOG_LEVEL=WARNING
ENV CACHE_URL=redis://host.docker.internal:6379/0


ENV PYTHONUNBUFFERED=1

CMD ["python", "cinephile/app.py"]