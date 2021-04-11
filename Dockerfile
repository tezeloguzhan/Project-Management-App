FROM python:3

WORKDIR /Project-Management-App

ADD . /Project-Management-App

EXPOSE 5000

COPY requirements.txt ./

RUN python3 -m pip install --user --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"] 



