import os
import urllib.error
import urllib.request

import requests
from bs4 import BeautifulSoup

print('ふたばちゃんねるのスレッドのURL(末尾.htm)を入力してください。')  # リンク入力
url = str(input("↓URLHERE↓\n"))
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
print('---------------------------------------------------------------------')

print('https://と2chan.netの間の文字を入力してください。')  # may/jun/dec対策
name = str(input("※https://hoge.2chan.net なら hoge を入力。\n"))
print('---------------------------------------------------------------------')

check = 0
while check < 5:  # 動画ファイル保存チェック
    video = str(input("動画ファイルを保存しますか？( 1 = 保存する | 0 = 保存しない )\n"))
    if video == str(1) or video == str(0):
        break
    else:
        print('不正な値が渡されました。正しく入力してください')

title = soup.find("title")
print('---------------------------------------------------------------------')
print('Access to ' + url + ' / ' + title.text)
print('---------------------------------------------------------------------')

# ChangeDirectory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))  # プログラムで稼働させる場合は必要

# フォルダ生成処理
new_dir_path = './画像'
os.makedirs(new_dir_path, exist_ok=True)
new_dir_path = './画像/' + str(title.text)
os.makedirs(new_dir_path, exist_ok=True)

# 定義


def download_picture(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def dl_directory(url, dst_dir):
    download_picture(url, os.path.join(dst_dir, os.path.basename(url)))


dst_dir = new_dir_path
video = int(video)
n = 0

for i in soup.select('a[href]'):
    m = str(i).split('href="')[1].split('" target=')[0]

    if video == 0:  # 動画を保存しない場合
        if 'javascript' in str(m) or 'php' in str(m) or 'www' in str(m) or 'htm' in str(m) or 'mp4' in str(m) or 'としあき' in str(m) or 'なー' in str(m):
            pass
        else:
            n += 1
            link = 'https://' + name + '.2chan.net' + m
            dl_directory(link, dst_dir)
            print('https://' + name + f'.2chan.net{m}')
            print('画像ファイルを保存しました。' + f'{n / 2}' + '個目')
            print('---------------------------------------------------------------------')

    elif video == 1:  # 動画を保存する場合
        if 'javascript' in str(m) or 'php' in str(m) or 'www' in str(m) or 'htm' in str(m) or 'としあき' in str(m) or 'なー' in str(m):
            pass
        else:
            n += 1
            link = 'https://' + name + '.2chan.net' + m
            dl_directory(link, dst_dir)
            print('https://' + name + f'.2chan.net{m}')
            print('画像/動画ファイルを保存しました。' + f'{n / 2}' + '個目')
            print('---------------------------------------------------------------------')

print('DLされた画像は、この実行ファイルと同じディレクトリの「画像」フォルダ内に入ってます。')
print('※DL時リンクが2重で表記されることがありますが、仕様です。実際は問題ありません。')
print('---------------------------------------------------------------------')
input('Enterを押すとプログラムを終了します。')
