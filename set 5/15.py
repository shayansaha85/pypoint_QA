from datetime import datetime
import os

# method 1
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#method 2
os.system("time")