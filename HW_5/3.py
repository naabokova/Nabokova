# Создайте асинхронную функцию fetch_multiple_urls(urls), которая:
#  - Делает конкурентные GET-запросы к списку URL (используйте aiohttp или httpx).
#  - Возвращает ответы в том же порядке, что и URL. 

# urls = ["https://example.com", "https://google.com"]
# results = await fetch_multiple_urls(urls)  # [response1, response2]


import asyncio
import aiohttp

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = session.get(url)
            tasks.append(task)

        results  = await asyncio.gather(*tasks)
        
        contents = []
        for result in results:
            content = await result.text()  
            contents.append(content)
            await result.release()  
            
        return contents
     
        
async def main():
    urls = ["https://example.com", "https://google.com"]
    pages  = await fetch_multiple_urls(urls)
    
    print(f"{urls}")
            

asyncio.run(main())