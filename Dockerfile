FROM python:3.10.7
WORKDIR /index
COPY . /index
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./app.py
