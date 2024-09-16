import time
import requests

session = requests.Session()

def file_download(url,name):
    print(f" so‘rovi jo‘natildi...")
    response = session.get(url)
    # print(f"Ma'lumotlar kelib tushdi: {response.status_code}")
    with open(f"images/sync_{name}.jpg","wb") as file:
        file.write(response.content)

def main():
    file_download("https://picsum.photos/seed/picsum/200/300","1")
    file_download("https://picsum.photos/seed/picsum/200/300","2")
    file_download("https://picsum.photos/seed/picsum/200/300","3")
    file_download("https://picsum.photos/seed/picsum/200/300","4")
    file_download("https://picsum.photos/seed/picsum/200/300","5")
    file_download("https://picsum.photos/seed/picsum/200/300","6")
    file_download("https://picsum.photos/seed/picsum/200/300","7")
    file_download("https://picsum.photos/seed/picsum/200/300","8")
    file_download("https://picsum.photos/seed/picsum/200/300","9")
    file_download("https://picsum.photos/seed/picsum/200/300","10")

start_time = time.time()
main()
end_time = time.time()
print(end_time - start_time)