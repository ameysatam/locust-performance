from locust import User, task, between, events

@events.test_start.add_listener
def script_start(**kwargs):
    print("I am connecting to DB")

@events.test_stop.add_listener
def script_stop(**kwargs):
    print("I am disconnecting from DB")

class MyUser(User):

    wait_time = between(1,3)

    def on_start(self):
        print("I am logging in")

    @task
    def doing_work(self):
        print("I am doing work")

    def on_stop(self):
        print("I am logging out")