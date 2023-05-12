
import time
import os
from datetime import datetime
from locust import HttpUser, task, between
import math
import logging


logging.basicConfig(level=logging.INFO, filename='log.txt', format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class CaseA(HttpUser):
   wait_time = between(1, 5)
   LOGGER = logging.getLogger(__name__)


   @task
   def hello_world(self):
       seed = {
           'clientStart' : round(datetime.utcnow().timestamp(), 3)
       }
       response = self.client.post("/", json=seed)
       response.raise_for_status()
       result = response.json()       
       CaseA.LOGGER.info(result)

   def on_start(self):
       print('start')


   def on_stop(self):
       print('stop')



