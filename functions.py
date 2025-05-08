while(True):
 username=input("name: ")
 try:
  if int(username)==1:
   print("correct")
   break
  else:
   print("wrong")
 except:
  print("password format invalid")