# Problem 1: Time Elapsed Since Task Started

import time

print('Please click "Enter" to start Timer ')
input()

startTime = time.time()

task = time.sleep(5)

timePassed = time.time() - startTime


# print(f'Time passed: {timePassed} seconds')
print(f"Time passed: {round(timePassed, 2)} seconds")
# round() gives a cleaner output hence its been used