# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Riley Hebert
#               Triston Maresh
#               Malcolm Ferguson
#               Marissa Bosher
# Section:      504
# Assignment:   Topic 11 passport checker 1
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
validFile = open("valid_passports.txt", 'w')
myString = ''
count = 0
for wee in processed:
    if (("byr" in wee[0]) and ("iyr" in wee[0]) and ("eyr" in wee[0]) and ("hgt" in wee[0]) and ("ecl" in wee[0]) and ("pid" in wee[0]) and ("cid" in wee[0])):
        # if the id is valid, append it to the string
        myString += f"{wee[1]}\n\n"    
        count += 1

#print(myString)
print(f"There are {count} valid passports")
validFile.write(myString)    
validFile.close()
myFile.close()
# close file

#cid:151 hcl:#c0946f 
#ecl:brn hgt:66cm iyr:2013 pid:694421369 
#byr:1980 eyr:2029 
# 
#cid:66 hcl:#efcc98 pid:791118269 iyr:2013 