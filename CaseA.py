
import time
import os
from datetime import datetime
from locust import HttpUser, task, between
import math
class CaseA(HttpUser):
   wait_time = between(1, 5)


   @task
   def hello_world(self):
       seed = {
           'clientStart' : round(datetime.utcnow().timestamp(), 3)
       }
       response = self.client.post("/", json=seed)
       response.raise_for_status()
       result = response.json()
       print(result)


   def on_start(self):
       print('start')


   def on_stop(self):
       print('stop')



