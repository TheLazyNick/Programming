import datetime
start = datetime.datetime.now()

print("Hello World")
    
    
"""Calcuation of time"""
end = datetime.datetime.now()
total = end-start
print("Execution time in Seconds:",total.seconds)
print("Execution time in Miliseconds:",total.microseconds)
