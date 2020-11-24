from locust import User, task, between

class MyUser(User):

    wait_time = between(1,2)

    @task(2)
    def addToCart(self):
        print("I am adding to cart")


    @task(4)
    def viewProduct(self):
        print("I am viewing product")logging out from the URL"