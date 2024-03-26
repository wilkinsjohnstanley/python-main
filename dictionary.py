#dictionary_name={key:value}
phonebook={'Chris':'555-111', 'Kate':'666-222'}
#del phonebook['Chris']
#print(phonebook)
#multiple datatypes is okay
grades = {'Chris':[76, 92, 100], 'Kate':[95, 60]}
#print(grades)
for key in phonebook:
    print(key, phonebook[key])