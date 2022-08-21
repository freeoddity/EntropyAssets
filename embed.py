import os
import base64
import json
owd = os.getcwd()
eventAssetPath = os.path.join(owd,"EventAssets")
gashaAssetPath = os.path.join(owd,"gashaAssets")

embedded_assets = []
for (root,dirs,files) in os.walk(eventAssetPath):
    for file in files:
        file_path = os.path.join(root,file)
        file_data = open(file_path,"rb").read()
        b64_data = str(base64.b64encode(file_data).decode())
        dict_key_folder = root.split("\\")[4]
        dict_key = f"{dict_key_folder}/{file}"
        embedded_asset = {dict_key:b64_data}
        embedded_assets.append(embedded_asset)
embedded_banners = []
for (root,dirs,files) in os.walk(gashaAssetPath):
    for file in files:
        file_path = os.path.join(root,file)
        file_data = open(file_path,"rb").read()
        b64_data = str(base64.b64encode(file_data).decode())
        dict_key_folder = root.split("\\")[4]
        dict_key = f"{dict_key_folder}/{file}"
        embedded_asset = {dict_key:b64_data}
        embedded_banners.append(embedded_asset)
with open("EmbeddedEvents.json","w+")as f:
    json.dump(embedded_assets,f,indent=4)
with open("EmbeddedGashaAssets.json","w+")as f:
    json.dump(embedded_banners,f,indent=4)
    
