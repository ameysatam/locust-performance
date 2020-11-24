from locust import HttpUser,task, between

class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "http://demo.guru99.com/test/newtours"
    @task
    def launch_URL(self):
        self.client.get("/reservation.php")
