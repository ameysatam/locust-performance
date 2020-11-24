from locust import User, task, between, constant, constant_pacing
from datetime import datetime

class MyWebUser(User):

    wait_time = between(2,3)
    weight = 3

    @task
    def login_URL(self):
        print("I am login into Web URL")

class MyMobileUser(User):

    wait_time = between(2,3)
    weight = 1

    @task
    def login_URL(self):
        print("I am login into Mobile URL")
