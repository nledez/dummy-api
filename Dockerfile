FROM python:3.7.5

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
