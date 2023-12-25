import time
for i in range(1, 10):
    print(f"\n")
    for j in range(1, 10):
        if j <= i:
            print(f"{i}*{j}={i * j}\t", end="")
            time.sleep(0.5)
