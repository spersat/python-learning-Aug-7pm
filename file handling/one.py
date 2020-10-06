'''
f=open('abc.txt','w')    # open a file, if not existing create the file, by default mode is set to r
print(f.name)           # provide the name of the file
print(f.mode)           # provide on which mode the file has been opened
print(f.closed)         # return boolean of file is closed
print(f.readable())     # returns boolean True if file is readable
print(f.writable())     # returns boolean True if file is writable
print('****************')
f.close()               #close the file
print(f.closed)
'''

f=open('abcd.txt','w')
list1 = ['SmallSmallSmallSmallSmallSmallSmallSmall \n','MediumMediumMediumMediumMediumMedium \n', 'Large Large Large Large Large Large Large Large Large \n']
f.write(list1)
f.close()
