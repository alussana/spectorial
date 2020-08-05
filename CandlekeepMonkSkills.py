import urllib.request
import os
import json
import pprint

dndapiurl = "https://www.dnd5eapi.co/api/"

def downloadObjData(objType, objIndex):
    os.makedirs(objType, exist_ok=True)
    objFileName = objType + "/" + objIndex
    urllib.request.urlretrieve(dndapiurl + objFileName, objFileName)
    objFile = open(objFileName)
    objTextData = objFile.read()
    objFile.close()
    objData = json.loads(objTextData)
    objFile = open(objFileName, "w")
    print(json.dumps(objData, sort_keys=True, indent=4), file=objFile)
    objFile.close()

def downloadIndexes(objType):
    os.makedirs("indexes", exist_ok=True)
    indexesFileName =  "indexes/" + objType
    urllib.request.urlretrieve(dndapiurl + objType + "/", indexesFileName)
    indexesFile = open(indexesFileName)
    indexesTextData = indexesFile.read()
    indexesFile.close()
    indexesData = json.loads(indexesTextData)
    indexesFile = open(indexesFileName, "w")
    print(json.dumps(indexesData, sort_keys=True, indent=4), file=indexesFile)
    indexesFile.close()

def getIndexes(objType):
    indexesFileName =  "indexes/" + objType
    if os.path.isfile(indexesFileName) == False:
        downloadIndexes(objType)
    indexesFile = open(indexesFileName)
    indexesTextData = indexesFile.read()
    indexesFile.close()
    indexesData = json.loads(indexesTextData)
    return(indexesData)
    
def findObjIndex(objType, objName):
    indexesFileName =  "indexes/" + objType
    if os.path.isfile(indexesFileName) == False:
        downloadIndexes(objType)
    indexesFile = open(indexesFileName)
    indexesTextData = indexesFile.read()
    indexesFile.close()
    indexesData = json.loads(indexesTextData)
    for entry in indexesData["results"]:
        try:
            if entry["name"] == objName:
                objIndex = entry["index"]
                return(objIndex)
        except:
            if entry["class"] == objName:
                objIndex = entry["index"]
                return(str(objIndex))

def getObjData(objType, objIndex):
    objFileName = objType + "/" + objIndex
    if os.path.isfile(objFileName) == False:
       downloadObjData(objType, objIndex)
    objFile = open(objFileName)
    objTextData = objFile.read()
    objFile.close()
    objData = json.loads(objTextData)
    return(objData, pprint.pformat(objData))

def openTheTomes():
    os.makedirs("indexes", exist_ok=True)
    indexesFileName =  "indexes/api"
    try:
        urllib.request.urlretrieve(dndapiurl, indexesFileName)
        indexesFile = open(indexesFileName)
        indexesTextData = indexesFile.read()
        indexesFile.close()
        indexesData = json.loads(indexesTextData)
        indexesFile = open(indexesFileName, "w")
        print(json.dumps(indexesData, sort_keys=True, indent=4), file=indexesFile)
        indexesFile.close()
        return(True)
    except:
        return(False)

def listKnowledge(objType):
    if objType == "":
        objType = "api"
    indexesData = getIndexes(objType)
    indexesDict = {}
    i = 0
    if objType == "api":
        for key in indexesData.keys():
            indexesDict[i] = key
            i = i + 1
    else:
        for entry in indexesData["results"]:
            try:
                indexesDict[i] = entry["name"]
            except:
                indexesDict[i] = entry["class"]
            i = i + 1
    return(indexesData, indexesDict, pprint.pformat(indexesDict))

def searchKnowledge(indexesData, objName):
    indexesDict = {}
    i = 0
    for entry in indexesData["results"]:
        if entry["name"].startswith(objName) or entry["index"].startswith(objName):
            indexesDict[i] = entry["name"]
        i = i + 1
    return(pprint.pformat(indexesDict))
    