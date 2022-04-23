import CandlekeepMonkSkills

def candlekeepMonk(tomesAreOpen = None):
    #CandlekeepMonkSkills.generateLibrary()
    if tomesAreOpen == None:
        print("\n Candlekeep Monk:")
        print(" \"Greetings. Just one moment and I'll help you with your quest.\"")
        print(" *Opens a tome and summons the Internet plane portal*")
        tomesAreOpen = CandlekeepMonkSkills.openTheTomes()
        print("\n Candlekeep Monk:")
        if tomesAreOpen == False:
            print(" \"My apoligies. It seems that I cannot retrieve the books you are looking for.\"")
            print(" \"Did you check your internet connection?\"\n")
            #exit()
        else:
            print(" \"Here we are. What kind of knowledge are you looking for?\"\n")
    else:
        print("\n Candlekeep Monk:")
        print(" \"Do you need something else?\"")
        answerInput = input("\n --> [y/n]: ")
        if answerInput != 'y' and answerInput != 'yes':
            print("\n Candlekeep Monk:")
            print(" \"Farewell.\"\n")
            exit()
        print("\n Candlekeep Monk:")
        print(" \"How may I assist you?\"\n")
    objType = ""
    indexesData, indexesDict, objDictPprint = CandlekeepMonkSkills.listKnowledge(objType)
    print(objDictPprint)
    objTypeInput = input("\n --> : ")
    objType = indexesDict[int(objTypeInput)]
    indexesData, indexesDict, objDictPprint = CandlekeepMonkSkills.listKnowledge(objType)
    indexesData_count = int(indexesData["count"])
    print("\n Candlekeep Monk:")
    if indexesData_count <= 40:
        print(f" \"Very well, {objType}. Here is what I have.\"\n")
        print(objDictPprint)
    else:
        print(f" \"Let me see... I've got {indexesData_count} results for {objType}.")
        print(" Do you know its name already? If not, try to use the first letters only.\"")
    objNameInput = input("\n --> : ")
    while type(objNameInput) != int:
        try:
            objNameInput = int(objNameInput)
        except:
            indexesDataRefinedPprint = CandlekeepMonkSkills.searchKnowledge(indexesData, objNameInput)
            print()
            print(indexesDataRefinedPprint)
            objNameInput = input("\n --> : ")
    objName = indexesDict[objNameInput]
    objIndex = CandlekeepMonkSkills.findObjIndex(objType, objName)
    objData, objDataPprint = CandlekeepMonkSkills.getObjData(objType, objIndex)
    print("\n Candlekeep Monk:")
    print(" \"Here is what you asked for. Use it wisely.\"\n")
    print("     _______________________________________________________________________________________")
    print("    /\                                                                                      \\")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________________________________________/")
    print()
    toprint = objDataPprint.split("\n")
    for line in toprint:
        print("      " + line)
    print("     _______________________________________________________________________________________")
    print("    /\                                                                                      \\")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________________________________________/")
    print()
    candlekeepMonk(tomesAreOpen)

if __name__ == '__main__':
    candlekeepMonk()