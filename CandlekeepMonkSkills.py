import urllib.request
import os
import json
import pprint

dndapiurl = 'https://www.dnd5eapi.co/api/'

def generateLibrary():
    tomesAreOpen = openTheTomes()
    objType = ''
    indexesData, indexesDict, objDictPprint = listKnowledge(objType)
    for i in indexesDict.keys():
        try:
            objType = indexesDict[i]
            indexesData_i, indexesDict_i, objDictPprint_i = listKnowledge(objType)
        except:
            pass
        for j in indexesDict_i.keys():
            try:
                objName = indexesDict_i[j]
                objIndex = findObjIndex(objType, objName)
                objData, objDataPprint = getObjData(objType, objIndex)
            except:
                pass

def downloadObjData(objType, objIndex):
    try:
        os.makedirs(f'library/{objType}', exist_ok=True)
        objLocalName = f'library/{objType}/{objIndex}'
        objFileName = objType + '/' + objIndex
        urllib.request.urlretrieve(dndapiurl + objFileName, objLocalName)
        objFile = open(objFileName)
        objTextData = objFile.read()
        objFile.close()
        objData = json.loads(objTextData)
        objFile = open(objFileName, 'w')
        print(json.dumps(objData, sort_keys=True, indent=4), file=objFile)
        objFile.close()
    except:
        print(f'It seems that I cannot retrieve this page, I\'m afraid.')

def downloadIndexes(objType):
    try:
        os.makedirs('library/indexes', exist_ok=True)
        indexesFileName =  f'library/indexes/{objType}'
        urllib.request.urlretrieve(dndapiurl + objType + '/', indexesFileName)
        indexesFile = open(indexesFileName)
        indexesTextData = indexesFile.read()
        indexesFile.close()
        indexesData = json.loads(indexesTextData)
        indexesFile = open(indexesFileName, 'w')
        print(json.dumps(indexesData, sort_keys=True, indent=4), file=indexesFile)
        indexesFile.close()
    except:
        print(f'It seems that I cannot retrieve this page, I\'m afraid.')

def getIndexes(objType):
    indexesFileName =  f'library/indexes/{objType}'
    if os.path.isfile(indexesFileName) == False:
        downloadIndexes(objType)
    indexesFile = open(indexesFileName)
    indexesTextData = indexesFile.read()
    indexesFile.close()
    indexesData = json.loads(indexesTextData)
    return(indexesData)
    
def findObjIndex(objType, objName):
    indexesFileName =  f'library/indexes/{objType}'
    if os.path.isfile(indexesFileName) == False:
        downloadIndexes(objType)
    indexesFile = open(indexesFileName)
    indexesTextData = indexesFile.read()
    indexesFile.close()
    indexesData = json.loads(indexesTextData)
    for entry in indexesData['results']:
        try:
            if entry['name'] == objName:
                objIndex = entry['index']
                return(objIndex)
        except:
            if entry['class'] == objName:
                objIndex = entry['index']
                return(str(objIndex))

def getObjData(objType, objIndex):
    objFileName = f'library/{objType}/{objIndex}'
    if os.path.isfile(objFileName) == False:
       downloadObjData(objType, objIndex)
    objFile = open(objFileName)
    objTextData = objFile.read()
    objFile.close()
    objData = json.loads(objTextData)
    return(objData, pprint.pformat(objData))

def openTheTomes():
    os.makedirs('library/indexes', exist_ok=True)
    indexesFileName =  'library/indexes/api'
    try:
        urllib.request.urlretrieve(dndapiurl, indexesFileName)
        indexesFile = open(indexesFileName)
        indexesTextData = indexesFile.read()
        indexesFile.close()
        indexesData = json.loads(indexesTextData)
        indexesFile = open(indexesFileName, 'w')
        print(json.dumps(indexesData, sort_keys=True, indent=4), file=indexesFile)
        indexesFile.close()
        return(True)
    except:
        return(False)

def listKnowledge(objType):
    try:
        if objType == '':
            objType = 'api'
        indexesData = getIndexes(objType)
        indexesDict = {}
        i = 0
        if objType == 'api':
            for key in indexesData.keys():
                indexesDict[i] = key
                i = i + 1
        else:
            for entry in indexesData['results']:
                try:
                    indexesDict[i] = entry['name']
                except:
                    indexesDict[i] = entry['class']
                i = i + 1
        return(indexesData, indexesDict, pprint.pformat(indexesDict))
    except:
        print(f'It seems that I cannot retrieve this page, I\'m afraid.')

def searchKnowledge(indexesData, objName):
    indexesDict = {}
    i = 0
    for entry in indexesData['results']:
        if entry['name'].startswith(objName) or entry['index'].startswith(objName):
            indexesDict[i] = entry['name']
        i = i + 1
    return(pprint.pformat(indexesDict))
    