import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요..")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():
    # 동시에 태스크를 실행하여 동시성 프로그램을 만듦
    # 병렬적으로 수행되는 것은 아님. 동시성으로 수행됨
    result = await asyncio.gather(
        delivery("A", 1),
        delivery("B", 2),
        delivery("C", 3),
    )

    print(result)
    # task1 = asyncio.create_task(delivery("A", 2)) # 예약 일정을 만들 수 있음
    # task2 = asyncio.create_task(delivery("B", 1))
    # await task2 # await delivery("A", 2) 와 같음
    # await task1


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())  # coroutine 함수를 실행하고 결과를 반환하는 쓰는 함수
    end = time.time()
    print(end - start)
