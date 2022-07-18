file = open('Python\content.txt', 'r')
lines = file.readlines()
for line in lines:
    if 'ABC' in line:
        print('X| '+ line)
    else:
        print('0| '+ line)
        