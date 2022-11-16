# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Riley Hebert
#               Triston Maresh
#               Malcolm Ferguson
#               Marissa Bosher
# Section:      504
# Assignment:   Topic 11 passport checker 2
# Date:         14 November, 2022
#
# open file
myFile = open(input("Enter the name of the file: "))
#myFile = open("scanned_passports.txt", 'r')

# use .split("\n\n") to give us a list of each seperate ID
myIDs = myFile.read().split("\n\n") # splitting up the IDs, each one is split by 2 newline characters in a row
processed = []
for anID in myIDs:
    # .split(" ")
    myList = []

    myData = []
    myLines = anID.split("\n")
    for line in myLines:
        for item in line.split(" "):
            myData.append(item)
    
    myDict = {}
    for pair in myData:
        myKey = pair.split(":")[0] # splits the pair up by the colon, assigns the first value to myKey
        myValue = pair.split(":")[1]
        myDict[myKey] = myValue
    
    myList.append(myDict)
    myList.append(anID)
    processed.append(myList)


# processed is now filled with many dictionaries

# open a new file
validFile = open("valid_passports2.txt", 'w')
myString = ''
count = 0
for wee in processed:
    # note: wee in this case is a list
    # this list contains a dictionary (at index 0) and the original string of each ID (at index 1)
    
    isValid = False # ids are false by default, that is unless and until the code evaluates otherwise

    # if the id has all the fields
    if (("byr" in wee[0]) and ("iyr" in wee[0]) and ("eyr" in wee[0]) and ("hgt" in wee[0]) and ("ecl" in wee[0]) and ("pid" in wee[0]) and ("cid" in wee[0])):
        myDict = wee[0]
        byr = myDict["byr"]
        iyr = myDict["iyr"]
        eyr = myDict["eyr"]
        hgt = myDict["hgt"]
        ecl = myDict["ecl"]
        pid = myDict["pid"]
        cid = myDict["cid"]

        # need to check if the value is valid
        # we will use a series of if statements to determine is the value for the given key is valid

        # byr - 4 digits, between 1920 and 2005, inclusive
        # iyr - 4 digits, between 2012 and 2022, inclusive
        # eyr - 4 digits, between 2022 and 2032, inclusive
        # hgt - number folloed by either cm or in
            # if cm, number must be between 150 and 193, inclusive
            # if in, number must be between 59 and 76, inclusive
        # ecl - exactly one of the following: amb, blu, brn, gry, grn, hzl, oth
        # pid - 9 digit number including leading zeros
        # cid - 3 digit number, NOT INCLUDING leading zeros


    if (isValid):
        myString += f"{wee[1]}\n\n"    
        count += 1

#print(myString)
print(f"There are {count} valid passports")
validFile.write(myString)    
validFile.close()
myFile.close()
# close file