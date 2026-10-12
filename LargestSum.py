# This program reads a list of comma-separated numbers from the standard input and then
# adds n number of adjacent entered numbers where 1<= n <= number of entered digits (all)

# Ask user to enter a list of comma-separated numbers 
inputString = input("Enter  a comma seprated list of numbers: ")
#numbers = list(map(int, inputString.split(",")))

#extract numbers
numbers = inputString.split(",")

arrayLen = len(numbers)
largestSum = (int)(numbers[0])
print("you entered " , arrayLen, " numbers\n")

#itereat through values of n (number of adjacent numbers to add)
for countNumbersToAdd in range(1,arrayLen):
	print("starting the loop for countNumbersToAdd = ", countNumbersToAdd, "Current max=[", largestSum, "]")

	# start walking through the list of numbers
	for i in range(0,arrayLen - countNumbersToAdd +1):
		# initiate the sum to this element of the list and then walk through the remainder of 
		# the list and add up n number of numbers together and each time update the largestSum
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

