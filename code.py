nameset = {"Oliver","Noah","Liam","Elijah"}   #creating a set of names

name = input("Enter a name you want to insert : ")
if name not in nameset:     # this checks if the name already exists
  nameset.add(name)         # in set we need to use add to insert an element
  print("Element Added")  
  print(nameset)            # printing elements or names of the set 
else:
  print("Entered name is alreay in the set")


# If you need to enter many names without running again and again

"""
def Insertname():
  name = input("Enter a name you want to insert : ")
  if name not in nameset:     # this checks if the name already exists
    nameset.add(name)         # in set we need to use add to insert an element
    print("Element Added")  
    print(nameset)            # printing elements or names of the set 
  else:
    print("Entered name is alreay in the set")
  ans = input('Do you want to insert again : ')
  if ans =='y' or ans=='Y':  #This is for entering name again
    Insertname();
  else:
    print("Thankyou")
Insertname();
"""
