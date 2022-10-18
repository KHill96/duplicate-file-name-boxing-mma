import os
# Globals
titles = []
duplicates = []

# Step 1
def grabFileNames():    
    fileList= os.listdir(r'PATH')
    fileList = fileList + os.listdir(r'PATH')
    fileList.remove('.DS_Store')
    findDuplicates(fileList)

# Step 2
def findDuplicates(fileList):
    fileList.remove('.DS_Store')
    print('Finding duplicates...')
    nameList = []
    for fileName in fileList:
        nameList = makeStringList(fileName)
        if nameList in titles:
            duplicates.append(fileName)
        else:
            titles.append(nameList)
        nameList = []
        


# Step 3
def makeStringList(inputString):
	# Remove extensions
	copyString = inputString
	copyString = inputString.replace('.mkv', '').replace('.mp4', '')
	
	names = copyString.split(' vs ')
	if containsNumber(names[1]):
		number = names[1][names[1].index(' ') + 1]
		names[1] = names[1][0:names[1].index(' ')]
		names.append(number)
	else:
		names.append('1')
  
	if 'Jr.' in names:
		names[names.index('Jr.') - 1] = names[names.index('Jr.') - 1] + ' Jr.'
		names.remove('Jr.')
	
	return names

def containsNumber(inputString):
    return any([char.isdigit() for char in inputString])


def main():
    grabFileNames()
    duplicates.sort(key=lambda x: x.lower())
    if len(duplicates) == 0:
        print("No Duplicates Found")
    else:
        for string in duplicates:
            print(f'Potential Duplicate: {string}')

    
if __name__ == '__main__':
	main()
