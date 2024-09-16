import asyncio
import time
import requests

session = requests.Session()

async def file_download(url,name):
    print(f" so‘rovi jo‘natildi...")
    response = session.get(url)
    with open(f"images/async_{name}.jpg","wb") as file:
        file.write(response.content)

async def main():
    await asyncio.gather(
        file_download("https://picsum.photos/seed/picsum/200/300","1"),
        file_download("https://picsum.photos/seed/picsum/200/300","2"),
        file_download("https://picsum.photos/seed/picsum/200/300","3"),
        file_download("https://picsum.photos/seed/picsum/200/300","4"),
        file_download("https://picsum.photos/seed/picsum/200/300","5"),
        file_download("https://picsum.photos/seed/picsum/200/300","6"),
        file_download("https://picsum.photos/seed/picsum/200/300","7"),
        file_download("https://picsum.photos/seed/picsum/200/300","8"),
        file_download("https://picsum.photos/seed/picsum/200/300","9"),
        file_download("https://picsum.photos/seed/picsum/200/300","10"),
    )
start = time.time()
asyncio.run(main())
print(time.time() - start)
