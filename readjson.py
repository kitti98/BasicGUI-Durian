import json

def readjson():
    with open('data.json',encoding='utf-8') as file:
        data = json.load(file)
        print(type(data))
        print(data[0]['point'])
    return data

def writejson(data):
    json_object = json.dumps(data,ensure_ascii=False,indent=4)
    with open('fruit.json','w',encoding='utf-8') as file:
        file.write(json_object)

data = {'125132359':['Banana',100,5],
        '125132360':['Durian',150,99],
        '125132361':['Apple',200,10],
        '125132362':['แก้วมังกร',300,20]
        }

writejson(data)

