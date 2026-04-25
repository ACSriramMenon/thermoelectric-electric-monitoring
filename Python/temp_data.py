import time
import random

while True:
    volt = random.uniform(0.5, 3.5)

    try:
        print(f"Voltage:{volt:.2f}", flush=True)
    except:
        break
    time.sleep(1)