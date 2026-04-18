import time
import random

while True:
    temp = random.uniform(25, 60)
    volt = random.uniform(0.5, 3.5)

    try:
        print(f"Temperature:{temp:.2f},Voltage:{volt:.2f}", flush=True)
    except:
        break
    time.sleep(1)