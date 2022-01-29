import requests

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060"

# requwstsでアクセスして照会、get()で情報を取得して、一旦変数responseに保存。
response = requests.get(url)
# それを実行
print(response)
print(response.text)
