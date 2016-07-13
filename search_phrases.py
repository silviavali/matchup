import re
import os
from timeit import Timer



file = 'file.txt' #replace the file name that contains the text you want to find the phrases from 
pattern_list = ["(.*)some_phrase_you_want_to_search_for(.*)",   "(.*)some_phrase_you_want_to_search_for(.*)"] #insert the phrases/words you want to find from your file here
variable_list = ["(.*)some_phrase_you_want_'to_search_for'(.*)"] #insert the phrases/words you want to find from your file here when the result you want to have is between single quotes
version = ["some_phrase_you_want_to_search_for_123"] #insert the phrase here you want to look for from the file and to extract numerical values from it (ex. Version:         4.2.6.00.03)
matched_phrases = [] #list for found phrases from find_matching_line function 



#--------------------------------------------------------------------------------------------------------------------------
#--------------------------GET MATCHING PHRASES without line number from your text file------------------------------------
def find_match(file, pattern_list):	
	
	hitcount = 0 # to count found matches
	list_found = [];  #for found matches
	text_file = open(file, "r")
	lines = text_file.readlines()
	
	for pattern in pattern_list:
		#print pattern
		for line in lines:

			if re.match(pattern, line):
				hitcount = hitcount  + 1
				list_found.append(line)
				
		text_file.close()
		 
	return list_found;

#--------------------------------------------------------------------------------------------------------------------------
#-----------------------------GET MATCHING PHRASES with line number displayed from your text file--------------------------
def find_matching_line(file, pattern_list):	
	
	hitcount = 0 # to count found matches
	text_file = open(file, "r")
	lines = text_file.readlines()
	list_found = [];  #for found matches

	for pattern in pattern_list:
		
		for linenum, line in enumerate(lines, start = 1):	

			if re.match(pattern, line):
				hitcount = hitcount  + 1
				found = str(linenum) + line
				list_found.append(found)

		text_file.close()
		 
	return list_found;


#--------------------------------------------------------------------------------------------------------------------------
#--------------GET phrases in the file from the variable_list displayed between quotes ------------------------------------


def get_variables(variable_lines):  #from find_matching_line results separate the variable names defined in the application
	
	variable_list_found = [];
	
	for line in variable_lines:
		#print line,
		found = re.findall(r"'([^'']*)'", line)
		variable_list_found.append(found);
	print variable_list_found
	
	return variable_list_found


#--------------------------------------------------------------------------------------------------------------------------
#-----------------------------Extract numerical values from the searched phrase--------------------------------------------

def get_digits(version):
	
	version_check = ""
	#print version
	
	for i in version:
		if i.isdigit():
			version_check += i
		
	return version_check



print 'Found phrases from the file with their line numbers'
print '--------------------------------------------------------------------------------------------------------------------------'
matched_phrases = find_matching_line(file, pattern_list)  #finds all  vulnerabilities with their line number in the source code

for match in matched_phrases:
	print match


print 'Found numerical values from the phrases searched for from the file '
print '--------------------------------------------------------------------------------------------------------------------------'
matched_version = str(find_match(file, version))  #finds all  vulnerabilities with their line number in the source code
checked_version = get_digits(matched_version)
print checked_version	



	
print 'Values between single quotes found from file'
print '--------------------------------------------------------------------------------------------------------------------------'
found_variable_lines = find_matching_line(file, variable_list) #finds all the lines of variable declarations
get_variables(found_variable_lines)












