#the purpose of this test is to read in a list of values from the physioData
#and then do something with it

f = open('./set-a-text/a01.csv', 'r')

for line in f:
    print line,