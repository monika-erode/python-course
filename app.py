import time
course = "Hello, World!"
print(course.upper())
print(len(course))
print(course[2:5])
print(course[-11:])
ticks = time.time()
print(ticks)

print("Number of ticks since 12:00am, January 1, 1970:", ticks)

print(time.time())

localtime = time.asctime(
    time.localtime(time.time())
)

print("Local current time :", localtime)