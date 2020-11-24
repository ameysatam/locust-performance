from locust import User, task, between, events

class UserLogin(User):
    wait_time = between(1,2)

    @events.test_start.add_listener
    def script_start(**kwargs):
        print("I am in test_start")

    @events.test_stop.add_listener
    def script_stop(**kwargs):
        print("I am in test_end")

    def on_start(self):
        print("I am performing on start")

    def on_stop(self):
        print("I am performing on stop")

    @task(4)
    def firsttask(self):
        print("I am performing first task")

    @task(1)
    def secondtask(self):
        print("I am performing second task")
