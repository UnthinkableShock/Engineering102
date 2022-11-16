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
    validity = 0
    
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
        try: # try-except pair to catch the cases where byr is not a valid integer
            byr = int(byr) 
            
            if (len(str(byr)) == 4 and byr >= 1920 and byr <= 2005):
                validity += 1 # only adds to validity if byr is both a valid integer and the right length and if it is between the given limits
        except:
            validity += 0
            
        # iyr - 4 digits, between 2012 and 2022, inclusive
        try: # try-except pair to catch the cases where byr is not a valid integer
            iyr = int(iyr) 
            if (len(str(iyr)) == 4 and iyr >= 2012 and iyr <= 2022):
                validity += 1 # only adds to validity if byr is both a valid integer and the right length and if it is between the given limits
        except:
            validity += 0
        
        # eyr - 4 digits, between 2022 and 2032, inclusive
        try: # try-except pair to catch the cases where byr is not a valid integer
            eyr = int(eyr) 
            if (len(str(eyr)) == 4 and eyr >= 2022 and eyr <= 2032):
                validity += 1 # only adds to validity if byr is both a valid integer and the right length and if it is between the given limits
        except:
            validity += 0

        # hgt - number followed by either cm or in
            # if cm, number must be between 150 and 193, inclusive
            # if in, number must be between 59 and 76, inclusive
        try:
            if ("cm" in hgt and len(hgt) == 5):
                myHeight = int(hgt[0:3])
                if (myHeight >= 150 and myHeight <= 193):
                    validity += 1
            if ("in" in hgt and len(hgt) == 4):
                myHeight = int(hgt[0:2])
                if (myHeight >= 59 and myHeight <= 76):
                    validity += 1
        except:
            validity += 0

        # ecl - exactly one of the following: amb, blu, brn, gry, grn, hzl, oth
        try:
            if (ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth"):
                validity += 1
        except:
            validity += 0

        # pid - 9 digit number including leading zeros
        try:
            int(pid)
            if (len(pid) == 9):
                validity += 1
        except:
            validity += 0

        # cid - 3 digit number, NOT INCLUDING leading zeros
        try:
            cid = str(int(cid))
            if (len(cid) == 3):
                validity += 1
        except:
            validity += 0


    if (validity == 7):
        myString += f"{wee[1]}\n\n"  
        count += 1

#print(myString)
print(f"There are {count} valid passports")
validFile.write(myString)    
validFile.close()
myFile.close()
# close file