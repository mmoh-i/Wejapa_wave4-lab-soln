#Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower

# Write your code here
# HINT: create a dictionary from flowers.txt
import json
def file_dict_opener(filename):

	commands = {}
	with open(filename) as fh:
		for line in fh:
			line = line.replace(':',' ')
			command, description = line.strip().split(maxsplit=1)
			commands[command] = description.strip()
			json.dumps(commands, indent=2, sort_keys=True)
	return commands

file =file_dict_opener('flowers.txt')
print('Enter your First [space] Last name only :')
def name_all_caps(name):
	return name.upper()
name =name_all_caps(input())

for i in file.keys():
	name[0] == i
	print(' Unique flower name with the first letter: ' + file[name[0]])
	break
	


        