from locust import User,TaskSet, between, task

class UserBehavour(TaskSet):

    @task(2)
    class CartModule(TaskSet):
        @task(4)
        def carttask1(self):
            print("I am in Cart Module task 1")

        @task(2)
        def carttask2(self):
            print("I am in Cart Module task 2")

        @task(1)
        def stopping(self):
            print("I am stopping")
            self.interrupt()

    @task(4)
    class ProductModule(TaskSet):
        @task(4)
        def producttask1(self):
            print("I am in product Module task 1")

        @task(2)
        def producttask2(self):
            print("I am in product Module task 2")

        @task(1)
        def stopping(self):
            print("I am stopping")
            self.interrupt()

class MyUser(User):
    wait_time = between(1,2)
    tasks = [UserBehavour]