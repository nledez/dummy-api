FROM python:3.7.5

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./
COPY check.sh ./

RUN chmod 555 /check.sh

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
