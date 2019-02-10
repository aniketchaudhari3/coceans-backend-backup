import time
import requests
start = time.time()
b  = requests.get("https://www.indeed.co.in/jobs?q=software+developer&l=pune")
b  = requests.get("https://www.indeed.co.in/jobs?q=software+developer&l=pune")
end = time.time()
print(end - start)
