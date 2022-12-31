# https://docs.python.org/ko/3.7/library/concurrent.futures.html
import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session, url = params[0], params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com"] * 50

    # 스레드를 만드는 비용이 추가적으로 발생하여 시간이 더 걸릴 수도 있음
    # max_workers=1 : single thread
    # max_workers=N (N>1) : multi thread, 각각의 thread가 동시적으로 해당 함수를 처리. 메모리 점유율이 증가
    # 단, multi threading 이 python 에서는 병렬적으로 수행될 수 없음
    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))  # map은 generator 객체임
        # print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # max_workers=1: 27sec, max_workers=10: 3sec
