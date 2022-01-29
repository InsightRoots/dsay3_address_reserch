import requests

zipcode = "0287111"
# これをインプットに変更
# zipcode = input("郵便番号は？")

#  url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" + "{zipcode}"
url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# requwstsでアクセスして照会、get()で情報を取得して、一旦変数responseに保存。
response = requests.get(url)
# それを実行
print(response)
print(response.text)
# →これでは、ジェイソンのテキストそのままなので、それを変更
print(type(response.json()))
# dict→それはつまり、辞書的に使える。天気問題と同じ。

# print(response.json()['message'])
print((response.json()))
# デバッグで式の構造を詳細に調べた上で、テストができる。
print((response.json())["results"][0]["address1"])
print((response.json())["results"][0]["address2"])
print((response.json())["results"][0]["address3"])
# ↑Printが複数あるので、置き換える。

# dic = response.json()
response = requests.get(url)
results = response.json()["results"]

# 質問、インライン化ってなにか、なぜインライン化をするのか、どうやってインライン化(Ctrl+Alt+N) をするのか

pref_name = results[0]["address1"]
city_name = results[0]["address2"]
town_name = results[0]["address3"]

address = f"{pref_name}{city_name}{town_name}"
print(address)
