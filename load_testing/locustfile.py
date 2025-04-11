from locust import HttpUser, task, between

class FastAPITestUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between requests (1 to 5 seconds)
    host = "http://127.0.0.1:8083"  # Base URL of your FastAPI app

    @task
    def read_root(self):
        self.client.get("/")  # Test the root endpoint

    @task
    def health_check(self):
        self.client.get("/health")  # Test the health check endpoint