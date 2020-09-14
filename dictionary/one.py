'''
# syntax of the dictionary: d = {"key1":"value1","key2":"value2"}
# dict prequest data type in python

#dict is
# mutuable
# keys: duplicates not allowed
# values: duplicates allowed

d = {"S_Name":"Sebastien"}
print(d)
print(d['S_Name']) # {'S_Name': 'Sebastien'}

d1={"S_Name":"Sebastien", "Age":30}
for x in  d1:
    print("Key: ",x, "value:",d1[x])    # Key:  S_Name value: Sebastien
                                        # Key:  Age value: 30

d1["s_loc"]="Hyd"
print(d1) # {'S_Name': 'Sebastien', 'Age': 30, 's_loc': 'Hyd'}

d1["s_loc"]="USA" #replace value in the s_loc 

#del d1 --> delete the dictionary, object does not exist anymore
#d.clear() --> clear the dictionary, but the object still exists
#items --> print(d1.items())
#keys --> print(d1.keys())
#values --> print(d1.values())
#update --> d.update({"loc","Paris"})
#pop --> d1.pop('key value') --> remove key value pair and returns the value only.
#remove --> remove a key value pair without returning anything

a = d1.pop('s_loc')
print(a) # USA
print(d1) # {'S_Name': 'Sebastien', 'Age': 30}


d = { }
print(type(d)) # <class 'dict'>
print(d) # {}

# Dict accessing 

d = { "s_Name":"Narasimha", "s_Age":37}
print(d)
print(d['s_Name']) # Narasimha
print(d['s_Age']) # 37

# dict copy
e=d.copy()
print(e) # {'s_Name': 'Narasimha', 's_Age': 37}

print(d.items()) # dict_items([('s_Name', 'Narasimha'), ('s_Age', 37)])
print (d.keys()) # dict_keys(['s_Name', 's_Age'])
print (d.values()) # dict_values(['Narasimha', 37])
'''

d = { "s_Name":"Narasimha", "s_Age":37}
#d.remove('s_Name') remove function does not exist
d.pop('s_Age')
print(d) # {'s_Name': 'Narasimha'}


