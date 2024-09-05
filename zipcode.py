import requests
import pprint

# アクセスする先のURL
end_point = "https://zipcloud.ibsnet.co.jp/api/search"

# ユーザーに郵便番号を入力
zip_code = input("郵便番号を入力してください。 > ")

#　パラメータに郵便番号をセット
param = {
    "zipcode": zip_code
}

#　リクエストして、返ってきた結果をresponseに格納
response = requests.get(end_point, params=param)
#response = requests.get("https://zipcloud.ibsnet.co.jp/api/search")

# print(response.text)

dict_data = response.json()

# pprint.pprint(dict_data)

print(dict_data.keys())

# print(dict_data["results"])

print(dict_data["results"][0]["address1"])
print(dict_data["results"][0]["address2"])
print(dict_data["results"][0]["address3"])

#順番に確認して
