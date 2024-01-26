'''
time module in first of module1.py file
time module its a in-build module in python
time module import as a import function, 
 from m import m/* function and etc
'''

import time

# you try now() function

now = time.time()
print(now)

a = time.localtime()
print(a)
print(a[0])

time.sleep(2)
print("Hey1")
time.sleep(2)
print("Hey2")