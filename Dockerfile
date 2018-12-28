FROM python:3.7-alpine

RUN addgroup -g 1000 -S dummy && \
    adduser -u 1000 -S dummy -G dummy

WORKDIR /home/dummy/code
COPY ./ .

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev

RUN python -m venv python3
RUN source ./python3/bin/activate
RUN ./python3/bin/pip install -r requirements.txt
#RUN pip install -r requirements.txt

CMD ["./python3/bin/python", "app.py"]
