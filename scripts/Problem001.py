import sys

# Check if the user inserted any agument
if len(sys.argv) > 1:
	# Get the max number as argument
	maxNumber = int(sys.argv[1])
	# Aux loop
	i = 1
	# Variable to get the result
	total = 0
	# Loop through each number until reaches maxNumber
	while i < maxNumber:
		# If is divisible by 3 or 5
		if i % 3 == 0 or i % 5 == 0:
			# Add the number to the total
			total += i
		# Iterate 1 more
		i += 1
	# Ouput the result
	print("Your result is: " + str(total))
else:
	# Output an error if the user didn't inserted any argument
	print("No max value was introduced as argument!")
