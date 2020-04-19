import urllib.request
import random
import string
import time
import concurrent.futures
import uuid
import hashlib
import sys
idlist = []
searched = []
in_id = ""

print("寄付はこちら（btc）：1Btxw93oqsfyfs6Hdmcoceky5UczRoxzik")
def randomname(n, m):
    if m == 1:
        return ''.join(random.choices(string.digits, k=n))  # 数字ID
    elif m == 2:
        return ''.join(random.choices(string.digits + "_", k=n))  # 数字とアンダーバー
    elif m == 3:
        # 数字とアンダーバーとアスキー文字
        return ''.join(random.choices(string.ascii_letters + string.digits + "_", k=n))


def twitter_acc(url):
    try:
        _id = url
        url = "https://twitter.com/"+url
        t_url = urllib.request.urlopen(url)
        searched.append(_id)
        t_url.close()
    except:
        idlist.append(_id)
        searched.append(_id)
        with open("idlist.txt", 'a') as f:
            f.write(str(_id)+'\n')


while 1:
    mode = input(f"【種類を選択】1:数字IDを検索　2:数字とアンダーバーを検索　3:数字とアルファベット　0:ソフトを終了＞＞")
    if mode == "0":
        sys.exit()
    if mode not in ["1", "2", "3", "0"]:
        print("不適切な数値が指定されました。")
        continue
    break
while 1:
    idlen = int(input(f"IDの長さを指定（５～１５）＞＞"))
    if idlen < 5 or idlen > 15:
        print("数値が範囲外です。")
        continue
    break
while 1:
    waittime = float(input(f"取得する待機時間を指定してください。(0.5~10)>>"))
    if waittime < 0.5 or waittime > 10:
        print("数値が範囲外です。")
        continue
    break
with open("idlist.txt", 'a') as f:
    f.write("種類設定:"+str(mode)+",長さ:"+str(idlen)+'\n')
print("処理を停止する場合は、[x]を押すか、プロセスを停止させてください。検索結果はidlist.txtに保存されます。")
while 1:
    s = randomname(idlen, int(mode))
    if in_id != "":
        if in_id not in s:
            continue
    if s in searched:
        pass
    else:
        twitter_acc(s)
        time.sleep(waittime)
