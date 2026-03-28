import psutil
import time
import os

THRESHOLD = 75

def check_resources():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return cpu, memory

def trigger_scaling():
    print("Threshold exceeded. Triggering cloud scaling...")
    os.system("python3 scale_to_cloud.py")

while True:
    cpu, mem = check_resources()
    print(f"CPU: {cpu}%, Memory: {mem}%")

    if cpu > THRESHOLD or mem > THRESHOLD:
        trigger_scaling()
        break

    time.sleep(5)