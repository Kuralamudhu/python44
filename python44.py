hy=input()
count=0
for i in range(len(hy)):
  if(hy[i].isdigit() or hy[i].isalpha() or hy[i]==(" ")):
    continue
  else:
    count+=1
print(count)
