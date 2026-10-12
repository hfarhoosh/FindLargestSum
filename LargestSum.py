
inputString = input("Enter  a comma seprated list of numbers: ")
#numbers = list(map(int, inputString.split(",")))
numbers = inputString.split(",")
arrayLen = len(numbers)
largestSum = (int)(numbers[0])
print("you entered " , arrayLen, " numbers\n")
for countNumbersToAdd in range(1,arrayLen):
	print("starting the loop for countNumbersToAdd = ", countNumbersToAdd, "Current max=[", largestSum, "]")
	for i in range(0,arrayLen - countNumbersToAdd +1):
		currSum = (int)(numbers[i])
		print("Calculating sum from element ", i, ".currSum[ ", currSum, "]")
		for j in range(i+1 , i+countNumbersToAdd):
			currSum += (int)(numbers[j])
			print("  Adding element ", j, " to element", i, ".  currSum[ ", currSum, "]")
#			print("type of currSum = ", type(currSum) , ". Type of largestSum = " , type(largestSum)) 
		if (currSum > largestSum):
			oldSum = largestSum
			largestSum = currSum
			print("******* Changing largestSum from " , oldSum , "to ", largestSum, " ***************")

