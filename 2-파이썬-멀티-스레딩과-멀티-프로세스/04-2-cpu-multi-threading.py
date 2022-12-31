import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor

nums = [50, 63, 32]


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)

    total = 1

    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 23.83 차이가 없고 오히려 시간이 늘어났음. 굳이 multi threading을 할 필요가 없음.
