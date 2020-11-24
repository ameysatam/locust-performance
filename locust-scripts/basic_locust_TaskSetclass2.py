from locust import User, TaskSet, task, between

class MyUser(User):

    wait_time = between(1,2)

    @task()
    class UserBehavior(TaskSet):

        @task()
        def addToCart(self):
            print("I am adding to cart")

        @task()
        def viewProduct(self):
            print("I am viewing product")
