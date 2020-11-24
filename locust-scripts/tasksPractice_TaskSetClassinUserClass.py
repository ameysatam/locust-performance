from locust import User, between, task, TaskSet

class MyUser(User):
    wait_time = between(1,2)

    @task
    class UserBehavior(TaskSet):
        @task
        def userLogin(self):
            print("I am in User Login")

        @task
        def clickElement(self):
            print("I am in click Element")
    