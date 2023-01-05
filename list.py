#%%
a=[1,2,3,4,5,"banga"]
print(a)

#%%
a.append("america")
print(a)
#%%
m=["british","anika","fariha","saniya_mirza","popy"]
a.extend(m)
print(a)

#%%
a.append(m)
print(a)
#%%
a.insert(1,"physics")
print(a)
#%%
b=a
#%%
# =============================================================================
# del a
# =============================================================================
print(b)
#%%
del b[0] #based on index
print(b)
#%%
del b[: 4]
print(b)
#%%
print(b.pop())
#%%
print(b.pop(0)) #based on index

#%%
c=["british","anika","fariha","saniya_mirza","popy"]
print(c)
#%%
c.remove("anika")
print(c)
#%%
c.reverse()
print(c)
#%%
j=[1,3,5,6,8,9,10,2,4,7]
print(j.sort())
#%%
j=[1,3,5,6,8,9,10,2,4,7]
print(j.sort(reverse=True))
#%%

j=[1,3,5,6,8,9,10,2,4,7]

print(j.index(5,0,5))
#%%
print(j.count(10))