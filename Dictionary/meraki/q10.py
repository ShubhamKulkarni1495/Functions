dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}

count=0
for i in dict:
    a=dict[i]
    for j in a:
        count+=1
print("total count:",count)