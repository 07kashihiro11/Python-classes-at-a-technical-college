# # https://weather.tsukumijima.net/
# # 今日の日付（2023-01-01とか）

# # 今日の天気（晴れとか）

# # 今日の風

# # 最高気温

# # 最低気温

# # を出力してみましょう。

# # 早くできた人は、明日の降水確率を出力してみましょう。（00 ~ 24まで数値を平均した数）

# import requests
# import json
# from datetime import datetime


# end_point = "https://weather.tsukumijima.net/api/forecast"

# city_id_mapping = {
#     "佐賀県": "410020"
# }

# city = input("都市名を指定してください　> ")

# param = {
#     "city": city
# }

# #　リクエストして、返ってきた結果をresponseに格納
# response = requests.get(end_point, params=param)
# #response = requests.get("https://zipcloud.ibsnet.co.jp/api/search")

# # print(response.text)

# # （例・佐賀県 伊万里 = 410020 ）

# dict_data = response.json()

# # print(dict_data.keys())

# # print(dict_data['publicTime'])

# # print(dict_data['forecasts'])

# # print(dict_data['forecasts'][0]['date'])...今日の日付

# # print(dict_data['forecasts'][0]['detail']['weather'])...今日の天気（晴れとか）

# # print(dict_data['forecasts'][0]['detail']['wind'])...今日の風

# # print(dict_data['forecasts'][0]['temperature']['max'])...最高気温

# print(dict_data['forecasts'][0]['temperature']['max'])

# # print(dict_data['forecasts'][0]['chanceOfRain']['T06_12'])...最低気温

"""weather_api.py"""
import requests
import pprint

end_point = "https://weather.tsukumijima.net/api/forecast&quot;"

city_name = input("osaka、hyogo、どっちですか？？ > ")

city_dict = {
    "osaka": 270000,
    "hyogo": 280010
}
param = {
"city": city_dict[city_name]
}
response = requests.get(end_point, params=param)
dict_data = response.json()
# pprint.pprint(dict_data)
pprint.pprint(dict_data["forecasts"][0]["date"])
# print(dict_data["forecasts"][1]["chanceOfRain"]["T00_06"])
# print(dict_data["forecasts"][1]["chanceOfRain"]["T06_12"])
# print(dict_data["forecasts"][1]["chanceOfRain"]["T12_18"])
# print(dict_data["forecasts"][1]["chanceOfRain"]["T18_24"])
chanceOfRainOfKey = dict_data["forecasts"][1]["chanceOfRain"]
print("降水確率の辞書型→", chanceOfRainOfKey)
# chanceOfRainList = [
# chanceOfRainOfKey["T00_06"],
# chanceOfRainOfKey["T06_12"],
# chanceOfRainOfKey["T12_18"],
# chanceOfRainOfKey["T18_24"],
# ]
# print("降水確率をリストに格納",chanceOfRainList)
# for i in range(len(chanceOfRainList)):
# chanceOfRainList[i] = int(chanceOfRainList[i].replace("%", ""))
# print("降水確率をリストに格納し直した",chanceOfRainList)
chanceOfRainList = []
for data in chanceOfRainOfKey.values():
    print(data)
chanceOfRainList.append(int(data.replace("%", "")))
print("数字になったリスト", chanceOfRainList)
print((sum(chanceOfRainList) / len(chanceOfRainList)))
