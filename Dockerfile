FROM python

WORKDIR /restful-booker-tests

COPY . .

RUN pip install -r requirements.txt
