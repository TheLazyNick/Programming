# importing the random module
import random
import math
import datetime
import time
start = datetime.datetime.now()


# prints a float between 0 and 1
# print(random.random())
OTP = []
for i in range(6):
   number = str(int(math.floor(random.random()*10)))
   OTP.append(number)

print("".join(OTP))


"""Calcuation of time"""
end = datetime.datetime.now()
total = end-start

print("Execution time in Seconds:", total.seconds)
print(total)
