import time
from queue import Queue
from random import random

queue = Queue()

def generate_request():
    request = random()
    queue.put(request)
    print(f"Request {request:.2f} created")

def process_request():
    if queue.empty():
        print("The queue is empty")
    else:
        request = queue.get()
        print(f"Request {request:.2f} processed")

def service():
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

service()