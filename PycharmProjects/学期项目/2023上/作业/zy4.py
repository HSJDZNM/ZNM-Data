import time
a = time.asctime(time.localtime(time.time()))
while True:
    print(f"本地时间:{a}")
    time.sleep(0.5)