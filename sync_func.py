import time

def file_download(file):
    print(f"{file} yuklanmoqda...")
    time.sleep(2)
    print(f"{file} yuklandi!")

start = time.time()
file_download("file1.txt")
file_download("file2.txt")
file_download("file3.txt")

print(time.time() - start)