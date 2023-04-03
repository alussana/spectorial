import urllib.request
import os
import json
import pprint

dndapiurl = 'https://www.dnd5eapi.co/api/'

def generateLibrary():
    objType = ''
    _, indexesList = listKnowledge(objType)
    try:
        for index in indexesList:
            objType = index
            _, indexesList_i = listKnowledge(objType)

            for index_i in indexesList_i:
                objName = index_i
                objIndex = findObjIndex(objType, objName)
                objData = getObjData(objType, objIndex)
    except Exception as e:
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
       print(f"Candlekeep Monk:\n\"Mage hand-ing the tome of {objType}...\"")
       downloadObjData(objType, objIndex)
    objFile = open(objFileName)
    objTextData = objFile.read()
    objFile.close()
    objData = json.loads(objTextData)
    return(objData)

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

        if objType == 'api':
            indexesList = list(indexesData.keys())
        else:
            indexesList = []
            for entry in indexesData['results']:
                try:
                    indexesList.append(entry['name'])
                except:
                    indexesList.append(entry['class'])
        return indexesData, indexesList
    except:
        print(f'It seems that I cannot retrieve this page, I\'m afraid.')

def searchKnowledge(indexesData, objName):
    indexesDict = {}
    i = 0
    print(indexesData['results'])
    for entry in indexesData['results']:
        if entry['name'].startswith(objName) or entry['index'].startswith(objName):
            indexesDict[i] = entry['name']
        i = i + 1
    return indexesDict
    
def displayTomes(objType, objData):
    # print(objData)
    if objType == 'classes':
        print(f"\t{objData['name']} Class Features\n")
        print(f"\tHit Dice: 1d{objData['hit_die']} per barbarian level")
        print("\n\tProficiencies:")
        for proficiency in objData['proficiencies']:
            print(f"\t{proficiency['name']}")
        print("\n\tSkill Choices:")
        for choice in objData['proficiency_choices']:
            print(f"\t{choice['desc']}")
        print("\n\tStarting Equipment:")
        for equipment in objData['starting_equipment']:
            print(f"\t{equipment['equipment']['name']} x {equipment['quantity']}")
        for equipment_options in objData['starting_equipment_options']:
            print(f"\t{equipment_options['desc']}")
    elif objType == 'ability-scores':
        print(f"\t{objData['full_name']}")
        print(f"\t{list(pprint.pformat(objData['desc']))}")
    else:
        print(objData)