# Remember to put the files and the py file in the same directory 

firstcode = 'firstcode.txt'
short_story = 'shortStory.txt'

files_available = [firstcode , short_story, 'others']

print('This is a pagiarism checker. You can estimate the extent of similarity between two files of text.')
print('We will be using the help of the python data structure \'sets\' to complete this task\n')

print('Available files to choose from: \n' )
for file in files_available:
    print(file)

print('\n')

source = input('Name of your source file: \n')

if source not in files_available:
    print( 'Invalid file')

if source == 'others':
    source = input('Name of your source file: \n')



print('Available files to choose from: \n' )
for file in files_available:
    print(file)
    
print('\n')

destination = input('File that you want to check: \n')

if destination not in files_available:
    print( 'Invalid file')

if destination == 'others':
    dsetination = input('Name of your source file: \n')



def plagiarism_check(reference_file, file_to_be_checked):
    file1 = open(reference_file, "r")
    file2 = open(file_to_be_checked, "r")

    reference_set = {}
    temp1 = file1.readline()

    #challenge: replace the while loop below with a helper function 
    
    while temp1:
        temp1 = temp1.replace("\n", '')
        temp1.lower()
        temp1 = temp1.split()
        if not reference_set:
            reference_set = set(temp1)
        else:
            for word in temp1:
                reference_set.add(word)
        temp1 = file1.readline()
    #reference_set = helper(temp1, reference_set, file1)

    to_check_set = {}
    temp2 = file2.readline()

    #to_check_set = helper(temp2, to_check_set, file2)

    #challenge: replace the while loop below with a helper function
    
    while temp2:
        temp2 = temp2.replace("\n", '')
        temp2.lower()
        temp2 = temp2.split()
        if not to_check_set:
            to_check_set = set(temp2)
        else:
            for word in temp2:
                to_check_set.add(word)
        temp2 = file2.readline()

    similarities = reference_set.intersection(to_check_set)
    
    percentage_of_similarity  = len(similarities)/len(to_check_set)*100
    
      
    if percentage_of_similarity > 75:
        print('Percentage similarity:' , percentage_of_similarity, '. Your text file is too similar to the source file!')
    else:
        print('Percentage simlarity:' , percentage_of_similarity , '. You Passed the Plagiarism test!')    


plagiarism_check(source, destination)
