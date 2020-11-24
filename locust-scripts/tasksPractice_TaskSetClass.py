from locust import between, task, User, TaskSet

class UserBehavior(TaskSet):
    @task()
    def loginURL(self):
        print("I am in LoginUrl")

    @task()
    def clickProduct(self):
        print("I am in click Product")

class MyUser(User):
    wait_time = between(1,2)
    tasks = [UserBehavior]