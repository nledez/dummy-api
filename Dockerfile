FROM python:3.10

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./
COPY summary.html ./
COPY check.sh ./

RUN chmod 555 /check.sh

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
