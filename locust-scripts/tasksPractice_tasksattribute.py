from locust import User, between, task, events

def user_login(userclass):
    print("I am in userlogin")

def buyitems(userclass):
    print("I am in buy items")

class SignIn(User):
    wait_time = between(1,2)

    def on_start(self):
        print("I am in on start")
    tasks = [user_login, buyitems]