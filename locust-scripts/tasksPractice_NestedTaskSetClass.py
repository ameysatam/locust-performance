from locust import User,TaskSet, between, task

class UserBehavour(TaskSet):

    @task
    class CartModule(TaskSet):
        @task
        def carttask1(self):
            print("I am in Cart Module task 1")

        @task
        def carttask2(self):
            print("I am in Cart Module task 2")

    @task
    class ProductModule(TaskSet):
        @task
        def producttask1(self):
            print("I am in product Module task 1")

        @task
        def producttask2(self):
            print("I am in product Module task 2")

    @task
    class EctModule(TaskSet):
        @task
        def etctask1(self):
            print("I am in etc Module task 1")

        @task
        def etctask2(self):
            print("I am in etc Module task 2")

class MyUser(User):
    wait_time = between(1,2)
    tasks = [UserBehavourT]