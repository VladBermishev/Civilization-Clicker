import requests as req
import xml.etree.ElementTree as ET


class CoordinatesGetter:
    api_key = "a9268c02-4dcd-44e3-9d81-c9dbac061aec"

    def __init__(self):
        self.payload = {
                        "apikey": CoordinatesGetter.api_key,
                        "geocode": ""
                        }

    def GetCoordinates(self, countryName):
        self.payload["geocode"] = countryName
        responce = req.get("https://geocode-maps.yandex.ru/1.x/", params=self.payload)
        xmlTree = ET.fromstring(responce.content.decode("utf-8"))
        pathToPoint = ["GeoObjectCollection", "featureMember", "GeoObject", "Point", "pos"]
        index = 0
        while index != len(pathToPoint):
            found = False
            for elem in xmlTree:
                if pathToPoint[index] in elem.tag:
                    found = True
                    xmlTree = elem
                    break
            if found:
                index += 1
            else:
                raise Exception("Cant get coords of {}, cause failure while parsing XML-responce".format(countryName))
        longitude, latitude = map(float, xmlTree.text.split(' '))
        return longitude, latitude
