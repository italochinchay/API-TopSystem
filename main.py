"""
import requests
import json

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

print(respuesta_json)

print("token: "+respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"])

"""
import conf

print(conf.usuario)
print(conf.clave)