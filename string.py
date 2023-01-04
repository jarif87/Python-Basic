print("hello")
x="this is a good place"
print(x.upper())
print(x.lower())
print(x[: 4])
print(x[: : -1])
y="this is a good place"
print(y.swapcase())
print(y.title())
#%%
z="i hate you"
z.isupper()
#%%
print(z.islower())
#%%
print(z.isalpha())
#%%
v="bangladesh"
print(v.isalpha())
#%%
print(v.isalnum()) 
#%%
print(v.isspace())
#%%
b="bangladeshismymothertounge"
print(b.isspace())
#%%
print(b.find("i",1,10)) # return -1 if char not present in the string
c="this is a string"
print(c.find("i",0,6))
#%%
print(c.rfind("i")) #check from reverse

#%%
print(c.index("i",0,10))
#%%
#print(c.index("w")) return error if char notn present in the string
print(c.count("a"))
#%%
c="this is a string"
print(c.replace("is","horse"))
print(c)
#%%
w="this is a string"
print(c.replace("is","horse",1)) 
#%%
w="this is a string"
print(w.ljust(30,"p")) # start from string(end)
#%%
print(w.rjust(30,"*")) # start from begaining
#%%
print(w.center(30,"%")) #start from start and end
#%%
print(w.zfill(40)) #adding (0) from the begaing
#%%
s="------this is a-----string-----"
print(s.strip("-")) # remove from first and last
print(s.lstrip("-")) # remove from first
print(s.rstrip("-")) # remove from last

#%%
k="bangladesh is a poor country"
print(k.split())
#%%
print(k.split("poor"))
print(k.split("p"))
print(k.split(","))
#%%
print(k.partition("a"))
print(k.rpartition("c"))
#%%
m="shakib al hasan is a good crickter"
print(m.startswith("s"))
print(m.endswith("tes"))
#%%
list_0=["mango","apple","banana","pine-apple","guava"]
print("".join(list_0))
print(" ".join(list_0))
print(",".join(list_0))















































