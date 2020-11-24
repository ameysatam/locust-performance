from locust import HttpUser,task, between, SequentialTaskSet

class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "http://demo.guru99.com/V1"
    @task
    class UserBehaviour(SequentialTaskSet):
        @task
        def launch_URL(self):
            with self.client.get("/index.php", name='launch', catch_response = True) as resp1:
                print("response1: " + resp1.text)
        @task
        def launch_URL(self):
            with self.client.post("/index.php", name='login', data={"uid": "mngr295846",
                                                               "password": "erUhYne",
                                                               "btnLogin": "LOGIN"}, catch_response = True) as resp2:
                print('response1: ' + resp2.text)