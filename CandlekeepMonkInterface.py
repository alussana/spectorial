import CandlekeepMonkSkills

def candlekeepMonk(tomesAreOpen = None):
    # CandlekeepMonkSkills.generateLibrary()
    if tomesAreOpen == None:
        print("\n Candlekeep Monk:")
        print(" \"Greetings. Just one moment and I'll help you with your quest.\"")
        print(" *Opens a tome and summons the Internet planar portal*")
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
    indexesData, indexesList = CandlekeepMonkSkills.listKnowledge(objType)
    for index in enumerate(indexesList):
        print(*index)
    objTypeInput = input("\n --> : ")

    objType = indexesList[int(objTypeInput)]
    indexesData, indexesList = CandlekeepMonkSkills.listKnowledge(objType)
    indexesData_count = int(indexesData["count"])
    print("\n Candlekeep Monk:")
    if indexesData_count <= 40:
        print(f" \"Very well, {objType}. Here is what I have.\"\n")
        for index in enumerate(indexesList):
            print(*index)
    else:
        print(f" \"Let me see... I've got {indexesData_count} results for {objType}.")
        print(" Do you know its name already? If not, try to use the first letters only.\"")
    objNameInput = input("\n --> : ")

    while type(objNameInput) != int:
        try:
            objNameInput = int(objNameInput)
        except:
            indexesDataRefined = CandlekeepMonkSkills.searchKnowledge(indexesData, objNameInput)
            print()
            for item in indexesDataRefined.items():
                print(*item)
            objNameInput = input("\n --> : ")

    objName = indexesList[objNameInput]
    objIndex = CandlekeepMonkSkills.findObjIndex(objType, objName)
    objData = CandlekeepMonkSkills.getObjData(objType, objIndex)
    
    print("\n Candlekeep Monk:")
    print(" \"Here is what you asked for. Use it wisely.\"\n")
    print("     _______________________________________________________________________________________")
    print("    /\                                                                                      \\")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________________________________________/")
    print()
    CandlekeepMonkSkills.displayTomes(objType, objData)
    print("     _______________________________________________________________________________________")
    print("    /\                                                                                      \\")
    print("(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("    \/______________________________________________________________________________________/")
    print()
    candlekeepMonk(tomesAreOpen)

if __name__ == '__main__':
    candlekeepMonk()
