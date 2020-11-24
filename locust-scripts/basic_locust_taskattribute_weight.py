from locust import User, task, between

def addToCart(userclass):
    print("I am adding to cart")

def viewProduct(userclass):
    print("I am viewing product")

class MyUser(User):

    wait_time = between(1,2)
    # tasks = [addToCart, viewProduct]
    tasks = {addToCart:3, viewProduct:6}