# encoding = utf-8
import time
time.sleep(2)
a = time.time() # 1587088527.5939999
print(a)
print(type(a)) # 1587088527.5939999
b = time.ctime()
print(b)
c = time.strftime("%Y %M %d %H_%M_%S")
print(c)