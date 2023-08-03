import requests
import json

def pedir_token():
    url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
    data = {
        "aaaUser" : {
            "attributes" : {
                "name" : "admin",
                "pwd" : "!v3G@!4@Y"
            }
        }
    }

    cabecera = {
        "Content-Type": "application/json"
    }

    requests.packages.urllib3.disable_warnings()

    respuesta = requests.post(url, data= json.dumps(data), headers=cabecera , verify=False)

    respuesta_json = respuesta.json()

    # print(respuesta_json)
    token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    # print("token: "+token)
    return token


print("+++++++++++++++++++++++++++")
token = pedir_token()
print("+++++++++++++++++++++++++++")
print("token: "+token)

# GET http://apic-ip-address/api/class/topSystem.json
url2 = "https://sandboxapicdc.cisco.com/api/class/topSystem.json"
header2 = {"content-type" : "application/json"}
API_Cooke = {"APIC-Cookie" : pedir_token()}
respuesta1 = requests.get(url2,headers=header2 , cookies=API_Cooke, verify=False)
print(respuesta1.json())

for i in range(0,int(respuesta1.json()["totalCount"])):
    print(respuesta1.json()["imdata"][i]["topSystem"]["attributes"]["address"])