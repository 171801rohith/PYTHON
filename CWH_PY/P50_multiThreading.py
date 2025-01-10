# MultiThreading in Python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    return f"Slept for {sec} seconds"

# # Normal Code
# # time1 = time.perf_counter()
# # func(3)
# # func(2)
# # func(1)
# # time2 = time.perf_counter()
# # print(f"Time taken: {time2 - time1} seconds")

# # Same usind threads
# t1 = threading.Thread(target=func, args=[3])
# t2 = threading.Thread(target=func, args=[2])
# t3 = threading.Thread(target=func, args=[1])

# time1 = time.perf_counter()
# t1.start()
# # t1.join() # Wait for t1 to finish
# t2.start()
# # t2.join()
# t3.start()
# # t3.join()

# # t1.join()
# # t2.join()
# # t3.join()
# time2 = time.perf_counter()
# print(f"Time taken: {time2 - time1} seconds")

def PoolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 2)
        # future2 = executor.submit(func, 3)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future3.result())
        # print(future2.result())
        agrs = [2, 1, 4, 5]
        results = executor.map(func, agrs)
        for result in results:
            print(result)


# PoolingDemo()

def func2(sec):
    for i in range(1, 50):
        print(f"{threading.current_thread().name} : {i}")
        time.sleep(sec)
    

t1 = threading.Thread(target=func2, args=[0])
t2 = threading.Thread(target=func2, args=[0])

t1.start()
t2.start()