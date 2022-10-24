import requests
import json

urlStart = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll("FIQ02")), file=fp)

def getAll(dataset):
    url = urlStart + dataset + urlEnd
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    getAllAsFile("FIQ02")
