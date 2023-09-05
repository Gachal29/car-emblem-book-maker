import os
import requests
import time
from bs4 import BeautifulSoup


images_dir_path = "emblem_images"
current_files = os.listdir(".")
if images_dir_path not in current_files:
  os.mkdir(images_dir_path)

website_url = "https://cobby.jp/car-emblem.html"

res = requests.get(website_url)
soup = BeautifulSoup(res.content, "html.parser")

targets = soup.find_all(class_="left-img")
print("画像の読み込みを開始します。")
for target in targets:
  img_elem = target.find("img")

  img_src = img_elem.get("src")
  filename = img_elem.get("alt")

  # 経過の表示
  print(f"filename:{filename} img_src:{img_src}")

  try:
    img_res = requests.get(img_src)
    with open(f"./{images_dir_path}/{filename}.jpg", "wb") as f:
      f.write(img_res.content)
  except Exception as e:
    print("画像が読み込めませんでした。")

  time.sleep(20)

print("画像の読み込みが完了しました。")

