#list contians the multiplication table of 7 . wap to convert it to vertical sring of same numbers.
table =[str(i*7 )for i in range(1,11)]# stored table in list as a string

vstr="\n".join(table) # used join for joining lista value or data each other with unique symbole
print(vstr)
