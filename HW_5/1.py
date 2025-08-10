# Напишите асинхронную функцию fetch_url(url), которая:
#  - Имитирует HTTP-запрос (используйте asyncio.sleep(1) вместо реального запроса).
#  - Возвращает "данные" с URL (например, f"Data from {url}").

# Запустите параллельно запросы к 5 разным URL и соберите результаты.

# Ожидаемый результат:
# Все запросы выполняются параллельно, общее время ~1 секунда (а не 5 секунд).



import asyncio

async def fetch_url(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
   results = await asyncio.gather(
        fetch_url("url1"),
        fetch_url("url2"),
        fetch_url("url3"),
        fetch_url("url4"),
        fetch_url("url5"),
    )
   for result in results:
    print(result)

asyncio.run(main())