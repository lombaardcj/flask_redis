# To run locust first install locust
```bash
pip install locust
```

Then run the locust file:
```bash
locust -f load_testing/locustfile.py
```
Then open the browser and go to http://localhost:8089

Then enter the number of users and spawn rate and start swarming

# Using Apache Benchmarking
```bash 
### Install Apache Benchmarking
sudo apt-get install apache2-utils

### Run Apache Benchmarking
ab -n 1000 -c 10 http://localhost:8083/
```
