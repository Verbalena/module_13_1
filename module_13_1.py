# Задача "Асинхронные силачи"
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    interval_sek = 12/power  # задержка (коофициент 12)
    for elem in range(1, 6):
        print(f'Силач {name} поднял {elem} шар')
        await asyncio.sleep(interval_sek)
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Григорий Русаков', 4))
    task_2 = asyncio.create_task(start_strongman('Иван Поддубный', 6))
    task_3 = asyncio.create_task(start_strongman('Пётр Крылов', 8))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())

