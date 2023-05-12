
import time
import os
from datetime import datetime
from locust import HttpUser, task, between
import math
import logging

format = '%(asctime)s %(filename)s %(lineno)s : %(message)s'

custom_logger = logging.getLogger("locust")
    
custom_logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

null_handler = logging.NullHandler()

custom_logger.addHandler(file_handler)
custom_logger.addHandler(console_handler)
#custom_logger.addHandler(null_handler)

class CaseA(HttpUser):
    wait_time = between(1, 5)    

    @task
    def hello_world(self):
        seed = {
            'clientStart': round(datetime.utcnow().timestamp(), 3)
        }
        response = self.client.post("/", json=seed)
        response.raise_for_status()
        result = response.json()        
        custom_logger.debug(result)

    def on_start(self):        
        print('start request')

    def on_stop(self):
        print('stop')
