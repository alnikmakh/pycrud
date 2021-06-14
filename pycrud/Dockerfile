FROM python:3.8.3-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y --no-install-recommends netcat && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /django
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod +x /django/entrypoint.sh
ENTRYPOINT ["/django/entrypoint.sh"]