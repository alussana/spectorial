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
    for entry in indexesData['results']:
        if entry['name'].startswith(objName) or entry['index'].startswith(objName):
            indexesDict[i] = entry['name']
        i = i + 1
    return indexesDict

def displayTomes(objType, objData):
    if objType == 'classes':
        print(f"\t{objData['name']} Class Features\n")
        print(f"\tHit Dice: 1d{objData['hit_die']} per {objData['name']} level")
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
        print(f"\t{objData['full_name']}\n")
        lines = pprint.pformat(objData['desc']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

    elif objType in ['alignments', 'conditions', 'damage-types', 'magic-items', 'magic-schools', 'subclasses', 'traits', 'feats', 'skills', 'weapon-properties']:
        print(f"\t{objData['name']}\n")
        lines = pprint.pformat(objData['desc']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

    elif objType == 'languages':
        print(f"\t{objData['name']}\n")
        print(f"\tType: {objData['type']}")
        print("\tTypical Speakers:", end=' ')
        print(*objData['typical_speakers'], sep=', ')
        if objData.get('script', None) is not None:
            print(f"\tScript: {objData['script']}")

    elif objType == 'equipment-categories':
        for index in objData['equipment']:
            print(f"\t{index['name']}")

    elif objType == 'features':
        print(f"\t{objData['name']}\n")
        print(f"\tClass: {objData['class']['name']}")
        print(f"\tLevel: {objData['level']}\n")
        lines = pprint.pformat(objData['desc']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

    elif objType == 'races':
        print(f"\t{objData['name']}")

        print(f"\n\tSize:")
        lines = pprint.pformat(objData['size_description']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

        print(f"\n\tSpeed: {objData['speed']}ft")

        print(f"\n\tAge:")
        lines = pprint.pformat(objData['age']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

        print(f"\n\tLanguages: ")
        lines = pprint.pformat(objData['language_desc']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

        print(f"\n\tAlignment: ")
        lines = pprint.pformat(objData['alignment']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

        print(f"\n\tTraits:")
        for trait in objData['traits']:
            print(f"\t{trait['name']}")
        print(f"\n\tAbility Bonuses:")
        for bonus in objData['ability_bonuses']:
            print(f"\t{bonus['ability_score']['name']}: {bonus['bonus']}")

    elif objType == 'spells':
        print(f"\t{objData['name']}\n")
        print(f"\tLevel: {objData['level']}\n")
        print(f"\tRange: {objData['range']}")

        print('\tComponents: ', end='')
        print(*objData['components'], sep=', ')
        if 'M' in objData['components']:
            print(f"\tMaterials: {objData['material']}")

        print(f"\tCasting Time: {objData['casting_time']}")
        print(f"\tDuration: {objData['duration']}")
        print(f"\tRequires concentration: {objData['concentration']}")
        print(f"\tIs ritual: {objData['ritual']}")
        print(f"\tSchool: {objData['school']['name']}\n")

        lines = pprint.pformat(objData['desc']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")
        lines = pprint.pformat(objData['higher_level']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

        print(f"\n\tClasses: ", end='')
        classes = []
        for index in objData['classes']:
            classes.append(index['name'])
        print(*classes, sep=', ')
        print(f"\t")

    elif objType == 'backgrounds':
        print(f"\t{objData['name']}\n")
        print(f"\t{objData['feature']['name']}\n")
        lines = pprint.pformat(objData['feature']['desc']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

        print(f"\n\tStarting Proficiencies:")
        for proficiency in objData['starting_proficiencies']:
            print(f"\t{proficiency['name']}")

        print(f"\n\tStarting Equipment:")
        for equipment in objData['starting_equipment']:
            print(f"\t{equipment['equipment']['name']} x {equipment['quantity']}")
        for equipment in objData['starting_equipment_options']:
            print(f"\t{equipment['from']['equipment_category']['name']}")

    elif objType == 'rule-sections':
        lines = pprint.pformat(objData['desc']).replace('\\n', '').split('\n')
        for line in lines:
            print(f"\t{line[2:-1]}")
        print(len(objData['desc'].split('\n')))

    elif objType == 'equipment':
        print(f"\t{objData['name']}")
        print(f"\t{objData['equipment_category']['name']}\n")
        properties = [property['name'] for property in objData['properties']]

        if objData['equipment_category']['index'] == 'armor':
            print(f"\tArmor Class: {objData['armor_class']['base']}", end='')
            if objData['armor_class']['dex_bonus']:
                print(" + DEX modifier", end='')
            print()
            print(f"\tMinimum Strength Required: {objData['str_minimum']}")
            print(f"\tStealth Disadvantage: {objData['stealth_disadvantage']}")

        elif objData['equipment_category']['index'] == 'weapon':
            print(f"\t{objData['category_range']}\n")

            print(f"\tDamage:")
            damage = objData['damage']
            print(f"\t{damage['damage_dice']} {damage['damage_type']['name']}")
            if 'Versatile' in properties:
                damage = objData['two_handed_damage']
                print(f"\t{damage['damage_dice']} {damage['damage_type']['name']} (versatile)")

            print(f"\n\tRange: {objData['range']['normal']}", end='')
            if objData['weapon_range'] == 'Ranged':
                print(f"/{objData['range']['long']}", end='')
            print()

            if 'Thrown' in properties:
                t_range = objData['throw_range']
                print(f"\tThrow Range: {t_range['normal']}/{t_range['long']}")

        if len(properties) > 0:
            print("\tProperties:", end=' ')
            print(*properties, sep=', ', end='\n\n')

        if len(objData['contents']) > 0:
            print(f"\tContents:")
            for content in objData['contents']:
                print(f"\t{content['item']['name']} x {content['quantity']}")
            print()

        print(f"\tCost: {objData['cost']['quantity']} {objData['cost']['unit']}")
        if objData.get('weight', None) is not None:
            print(f"\tWeight: {objData['weight']}")
        if objData.get('quantity', None) is not None:
            print(f"\tQuantity: {objData['quantity']}")

        print()
        lines = pprint.pformat(objData['desc']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

    elif objType == 'rules':
        print(f"\t{objData['name']}\n")
        print(f"\tRule sections to read:")
        for section in objData['subsections']:
            print(f"\t - {section['name']}")

    elif objType == 'monsters':
        print(f"\t{objData['name']}")
        print(f"\t{objData['size']} {objData['type']}, {objData['alignment']}")

        print(f"\n\tCR {objData['challenge_rating']} ({objData['xp']} XP)")
        print(f"\tArmor Class: {objData['armor_class'][0]['value']}")
        print(f"\tHit points: {objData['hit_points']}")
        if len(objData['speed']) > 0:
            print('\tSpeed:', end=' ')
            for speed in objData['speed'].items():
                print(f"{speed[0]}: {speed[1][:-1]}", end=', ')

        print('\n\t____________________________________________________________________________________')
        print(f"\n\tSTR\tDEX\tCON\tINT\tWIS\tCHA")
        print(f"\t{objData['strength']}\t{objData['dexterity']}\t{objData['constitution']}\t{objData['intelligence']}\t{objData['wisdom']}\t{objData['charisma']}")
        print(f"\t({(objData['strength'] - 10) // 2})\t({(objData['dexterity'] - 10) // 2})\t({(objData['constitution'] - 10) // 2})\t({(objData['intelligence'] - 10) // 2})\t({(objData['wisdom'] - 10) // 2})\t({(objData['charisma'] - 10) // 2})")
        print('\t____________________________________________________________________________________')

        if len(objData['proficiencies']) > 0:
            print(f"\n\tProficiencies:")
            for proficiency in objData['proficiencies']:
                print(f"\t - {proficiency['proficiency']['name']} +{proficiency['value']}")
        print()

        if len(objData['condition_immunities']) > 0:
            condition_immmuities = [condition['name'] for condition in objData['condition_immunities']]
            print('\tCondition Immunities:', end=' ')
            print(*condition_immmuities, sep=', ')
        if len(objData['damage_immunities']) > 0:
            print('\tDamage Immunities:', end=' ')
            print(*objData['damage_immunities'], sep=', ')
        if len(objData['damage_resistances']) > 0:
            print('\tDamage Resistances:', end=' ')
            print(*objData['damage_resistances'], sep=', ')
        if len(objData['damage_vulnerabilities']) > 0:
            print('\tDamage Vulnerabilities:', end=' ')
            print(*objData['damage_vulnerabilities'], sep=', ')

        if len(objData['senses']) > 0:
            print('\tSenses:', end=' ')
            senses = [f"{sense[0]}: {sense[1]}" for sense in objData['senses'].items()]
            print(*senses, sep=', ')

        if len(objData['languages']) > 0:
            print(f"\tLanguages: {objData['languages']}")
        print('\t____________________________________________________________________________________')

        if len(objData['actions']) > 0:
            print("\n\tACTIONS")
        for action in objData['actions']:
            print(f"\n\t{action['name']}")
            lines = pprint.pformat(action['desc']).replace('\\n', '')[:-1].split('\n')
            for line in lines:
                print(f"\t{line[1:-1]}")

        if len(objData['legendary_actions']) > 0:
            print("\n\tLEGENDARY ACTIONS")
        for action in objData['legendary_actions']:
            print(f"\n\t{action['name']}")
            lines = pprint.pformat(action['desc']).replace('\\n', '')[:-1].split('\n')
            for line in lines:
                print(f"\t{line[1:-1]}")

        if len(objData['special_abilities']) > 0:
            print("\n\tSPECIAL ABILITIES")
        for ability in objData['special_abilities']:
            print(f"\n\t{ability['name']}")
            lines = pprint.pformat(ability['desc']).replace('\\n', '')[:-1].split('\n')
            for line in lines:
                print(f"\t{line[1:-1]}")
            if ability.get('usage', None) is not None:
                print(f"\tUsage - {ability['usage']['times']} {ability['usage']['type']} {ability['usage']['rest_types']}")

    elif objType == 'subraces':
        print(f"\t{objData['race']['name']}: {objData['name']}\n")
        lines = pprint.pformat(objData['desc']).split('\n')
        for line in lines:
            print(f"\t{line[2:-2]}")

        if len(objData['ability_bonuses']) > 0:
            print(f"\n\tAbility Score Increase: ")
        for bonus in objData['ability_bonuses']:
            print(f"\t - {bonus['ability_score']['name']} +{bonus['bonus']}")

        if len(objData['racial_traits']) > 0:
            print(f"\n\tRacial Traits: ")
        for trait in objData['racial_traits']:
            print(f"\t - {trait['name']}")

        if len(objData['starting_proficiencies']) > 0:
            print(f"\n\tStarting Proficiencies: ")
        for proficiency in objData['starting_proficiencies']:
            print(f"\t - {proficiency['name']}")

        if len(objData['languages']) > 0:
            print(f"\n\tLanguages: ")
        for language in objData['languages']:
            print(f"\t - {language['name']}")

        if objData.get('language_options', None) is not None:
            print(f"\n\tChoose {objData['language_options']['choose']} language(s) from the following:", end='\n')
        for option in objData['language_options']['from']['options']:
            print(f"\t{option['item']['name']}")
    
    elif objType == 'proficiencies':
        print(f"\t{objData['name']}")
        print(f"\tType: {objData['type']}")
        print(f"\tReference: {objData['reference']['name']}")
