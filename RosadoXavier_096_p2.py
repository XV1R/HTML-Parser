# Filename: project_2.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME:Xavier A. Rosado Lebron
# STUDENT ID:802195719
# SECTION:096

"""Parse the contents of an HTML file and output the internal resources used.

We are looking for tags of interest: a, script, link, and img.
Within each tag of interest we're looking for a particular attribute of
interest (href for a & link, src for script & img).
A list is created for each type of tag, storing all of the internal
resources referenced by tags of that type.
Finally, the results are stored in an output file.

Input:  The file index.html will be used as an input file
Output: The results will be stored in a file named index_resources.txt
"""




def load_data():
	"""Returns the contents of index.html in a list, or None if an error occurs."""
	try:
		fh = open('index.html')
	except:
		lstOfLines = None
	else: # Only gets executed if no exception was raised
		lstOfLines = fh.readlines()
		fh.close()
	return lstOfLines

#find start of tag
#add all tags into one collective list TODO
def get_tag_of_interest(line):
	#dummy value
	tagstart = None
    #parses through lines, looking for the tags we're tasked with finding
	#if it finds one, assigns tagstart to begin parsing through said line
	#we only need one tagstart variable since we're looping through the lines in main
	"""this code is clean"""
	if '<a' in line:
		tagstart = line.find('<a')
	elif '<link' in line:
		tagstart = line.find('<link')
	elif '<script' in line:
		tagstart = line.find('<script')
	elif '<img' in line:
		tagstart = line.find('<img')
	endtag = line.find('>',tagstart)
	wholetag = line[tagstart:endtag+1]
	return wholetag

# if it detects that the tag is an online resource(http or https), it proceeds to ignore it
#parse through the tag we previously got
#depending on the tag, find if it has an attribute; if not, ignore it
#if it has http/https, ignore it. not a local resouce
def get_attr_of_interest(wholetag):
	if "http:" in wholetag or "https:" in wholetag:
		return None
				#verify if the tag is href or src. if it's none of them, return nothing
	else:
		atrstart = None
		if wholetag.startswith('<a ') or wholetag.startswith('<link'):
			if 'href=' in wholetag:
				parse_start = wholetag.find('href=')
				#BONO?
				try:
					atrstart = wholetag.find('"',parse_start)+1
				except:
					atrstart = wholetag.find("'",parse_start)+1
			else:
				return None
		elif wholetag.startswith('<script') or wholetag.startswith('<img'):
			if 'src=' in wholetag:
				 parse_start = wholetag.find('src=')
				 try:
					 atrstart = wholetag.find('"',parse_start)+1
				 except:
					 atrstart = wholetag.find("'",parse_start)+1

				
			else:
				return None
		else:
			return None
	atend = wholetag.find('"',atrstart)
	attr_interest = wholetag[atrstart:atend]
	return attr_interest


#These variables are defined in main
#outFH = the output file which were writing to
#sectionName = the name of the lists which we'll be writing
#listOfResources = the list full of attributes to be used when we call this function
#if the list is empty, proceed to not print it out
def write_results(outFH,sectionName,listOfResources):
	if len(listOfResources) > 0:
		outFH.write(sectionName+'\n')
		listOfResources.sort()
		for x in listOfResources:
			outFH.write(x+'\n')
	else:
		return None

	"""Write the resources of a particular section to an already opened file."""


def main():
	linesInFile=load_data()
	if linesInFile is None:
		print('ERROR: Could not open index.html!')
		exit()
	else:
		#lists we'll be using
		css=[]
		js=[]
		images=[]
		hyperlinks=[]
		#run all the functions using only one loop
		for line in linesInFile:
			wholetag=get_tag_of_interest(line)
			if wholetag==None:
				continue
			else:
				attr_interest=get_attr_of_interest(wholetag)
				if attr_interest==None:
					continue
				else:
					if wholetag.startswith('<a'):
						listOfResources=hyperlinks
						hyperlinks.append(attr_interest)
					elif wholetag.startswith('<script'):
						listOfResources=js
						js.append(attr_interest)
					elif wholetag.startswith('<link'):
						listOfResources=css
						css.append(attr_interest)
					elif wholetag.startswith('<img'):
						listOfResources=images
						images.append(attr_interest)
		#this shouldn't be looped, as we  only want to open and close once.
		outFH=open('index_resources.txt', 'w')
		if len(css) > 0:
			write_results(outFH,'CSS:',css)
		if len(js) > 0:
			write_results(outFH,'JavaScript:',js)
		if len(images) > 0:
			write_results(outFH,'Images:',images)
		if len(hyperlinks) > 0:
			write_results(outFH,'Hyperlinks:',hyperlinks)
	outFH.close()
				




if __name__ == '__main__':
    main()
