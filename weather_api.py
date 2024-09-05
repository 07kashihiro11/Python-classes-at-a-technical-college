import requests

end_point = "https://weather.tsukumijima.net/api/forecast"

city_name = input("osaka,hyogoどちらですか >")

city_dict = {
    "osaka": 270000,
    "hyogo": 280010
}

#辞書型を使って入力する文字列を変更する
param = {
    "city": city_dict[city_name]
}

response = requests.get(end_point, params=param)

dict_data = response.json()

print(dict_data['forecasts'][0]['date'])


print(dict_data['forecasts'][1]['chanceOfRain']['T00_06'])

print(dict_data['forecasts'][1]['chanceOfRain']['T06_12'])

print(dict_data['forecasts'][1]['chanceOfRain']['T12_18'])

print(dict_data['forecasts'][1]['chanceOfRain']['T18_24'])


chanceOfRainOfKey = dict_data["forecasts"][1]["chanceOfRain"]
print("降水確率の辞書型→", chanceOfRainOfKey)

chanceOfRainOfList = {
    chanceOfRainOfKey['T00_06'],
    chanceOfRainOfKey['T06_12'],
    chanceOfRainOfKey['T12_18'],
    chanceOfRainOfKey['T18_24']
    
}
print("降水確率をリストに格納", chanceOfRainOfList)

for i in range(len(chanceOfRainOfList)):
    chanceOfRainOfList[i]= int(chanceOfRainOfList.replace)
    
print((sum))



# chance0fRain0fList =[]
# for data in chanceOfRainOfKey.values():
#     print(data)
#     chanceOfRainOfList.append(int(data.replace("%", "")))
    
    

