import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(fileName):
	# get a list of dictionary objects from the file
	#Input: file name
	inFile = open(fileName, "r")
	line = inFile.readline()

	dictList = []
	header = line.split(",")

	headerFirstName = header[0]
	headerLastName = header[1]
	headerEmail = header[2]
	headerGrade = header[3]
	headerDob = header[4].rstrip("\n")

	line = inFile.readline()

	while line:
		list1 = line.split(",")
		fileDict = {}
		fileDict[headerFirstName] = list1[0]
		fileDict[headerLastName] = list1[1]
		fileDict[headerEmail] = list1[2]
		fileDict[headerGrade] = list1[3]
		fileDict[headerDob] = list1[4].rstrip("\n")

		dictList.append(fileDict)

		line = inFile.readline()

	inFile.close()
#Ouput: return a list of dictionary objects where
	return dictList

#the keys are from the first row in the data. and the values are each of the other rows

def mySort(data,col):
 	#Sort based on key/column
	dataByCol = sorted(data, key=lambda x:x[col])
	nameString = dataByCol[0]["First"] + " " + dataByCol[0]["Last"]
	return nameString
 	#Input: list of dictionaries and col (key) to sort on
 	#Output: Return the first item in the sorted list as a string of just: firstName lastName


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	classDict = {}
	for d in data:
		if d["Class"] in classDict:
			count = classDict[d["Class"]]
			classDict[d["Class"]] = count + 1
		else:
			classDict[d["Class"]] = 1
	return(sorted(classDict.items(), key = lambda x: x[1], reverse = True))


def findMonth(data):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	classDict = {}
	for d in data:
		birthMonth = d["DOB"].split("/")[0]
		if birthMonth in classDict:
			count = classDict[birthMonth]
			classDict[birthMonth] = count + 1
		else:
			classDict[birthMonth] = 1
	birthMonthList = (sorted(classDict.items(), key = lambda x: x[1], reverse = True))
	topBirthMonth = birthMonthList[0]
	return int(topBirthMonth[0][0])



def mySortPrint(data,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	for line in data:
		del line["DOB"]
		del line["Class"]

	dataByCol = sorted(data, key=lambda x:x[col])
	outFile = open(fileName, "w")
	for d in dataByCol:
		outFile.write(d["First"] + "," + d["Last"] + "," + d["Email"] + " \n")
	outFile.close()



def findAge(data):
	pass
# # def findAge(a):
# # Input: list of dictionaries
# # Output: Return the average age of the students and round that age to the nearest
# # integer.  You will need to work with the DOB and the current date to find the current
# # age in years.




# ################################################################
# ## DO NOT MODIFY ANY CODE BELOW THIS
# ################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))


# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
