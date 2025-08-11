# Создайте асинхронную функцию fetch_multiple_urls(urls), которая:
#  - Делает конкурентные GET-запросы к списку URL (используйте aiohttp или httpx).
#  - Возвращает ответы в том же порядке, что и URL. 

# urls = ["https://example.com", "https://google.com"]
# results = await fetch_multiple_urls(urls)  # [response1, response2]


import asyncio
import aiohttp

async def fetch_multiple_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def fetch_multiple_urls(urls):
    tasks = []
    for url in urls:
            tasks.append(fetch_multiple_url(url))



async def main():
    urls = ["https://example.com", "https://google.com"]
    results = await fetch_multiple_urls(urls)  # [response1, response2]
    print()

asyncio.run(main())