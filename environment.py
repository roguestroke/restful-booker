import os


class Environment:
    TEST = 'test'
    PROD = 'prod'

    URLS = {
        TEST: 'http://localhost:3001',
        PROD: 'https://restful-booker.herokuapp.com'
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.TEST

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


ENV_OBJECT = Environment()
