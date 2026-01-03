#function to remove any word form list
def rem(l,word):
    n=[]
    for item in l:
        if(item==word):
            l.remove(word)

        else:
         n.append(item.strip(word))
    return n

l=["apple","hi","ushant","wow","a"]
#l.remove("apple")
print(rem(l,"a"))
