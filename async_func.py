import asyncio
import time

async def download_file(file):
    print(f"{file} yuklanmoqda...")
    await asyncio.sleep(2)  # 2 soniya kutish
    print(f"{file} yuklandi!")

async def main():
    await asyncio.gather(
        download_file("file1.txt"),
        download_file("file2.txt"),
        download_file("file3.txt"),
    )
start = time.time()
asyncio.run(main())
print(time.time() - start)
