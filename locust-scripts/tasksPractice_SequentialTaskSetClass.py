from locust import User, between, task, SequentialTaskSet



class MyUser(User):
    wait_time = between(1,2)

    @task
    class UserBehaviour(SequentialTaskSet):

        @task
        def doingTask1(self):
            print("Doing Task 1")

        @task
        def doingTask2(self):
            print("Doing Task 2")

        @task
        def doingTask3(self):
            print("Doing Task 3")