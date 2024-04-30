users=input()

letters=list(users.replace('{','').replace('}','').replace(' ','').split(','))


cheacker=[]

counter=0

for i in letters:
  if i=="":
    break
  elif i not in cheacker:
    cheacker.append(i)
  




print(len(cheacker))
