import os
# assign directory
directory = 'tests'
 
tests = []
count = 0
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and f != "tests/.DS_Store":
        #tests.append(f)
        count = count + 1

print(count)


#with open('readme.txt', 'w') as f:
    #f.write('\n'.join(tests))