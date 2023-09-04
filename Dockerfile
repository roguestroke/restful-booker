FROM python

WORKDIR /restful-booker-api-tests

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD python api.py