import time
import os
import math
size = math.floor((os.get_terminal_size().columns)/2)
def line(i,a,b):
    print(i*' '+a+((2*(size-i))-2)*' '+b)
    time.sleep(0.015)
while True:
    for i in range(size):
        line(i,'\\','/')
    for i in reversed(range(size)):
        line(i,'/','\\')