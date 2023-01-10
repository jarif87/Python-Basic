#%%
a={1,2,3,4,"english",(10,40)}
print(a)
# %%
a={1,2,3,4,5}
b={6.7,7,8,9,10,1,2}
print(a.intersection(b))
# %%
a.intersection_update(b)
# %%
print(a)
# %%
print(a.difference(b))
# %%
a.difference_update(b)
# %%
print(a)
# %%
a={1,2,3,4,5}
b={6.7,7,8,9,10,1,2}
# %%
print(a.union(b))
# %%
a.update(b)
print(a)
# %%
print(a.symmetric_difference(b))
# %%
a.symmetric_difference_update(b)
print(a)
# %%
a={1,2,3,4,5}
b={6.7,7,8,9,10,1,2}
# %%
print(a.isdisjoint(b))
# %%
print(a.issubset(b))
# %%
print(a.superset(b))
# %%
a={1,2,3,4,5}
b={6.7,7,8,9,10,1,2}
a.add(99)
print(a)
# %%
a.discard(5)
print(a)
# %%
a={1,2,3,4,5,5,5,5,5,5,5}
b={6.7,7,8,9,10,1,2}

# %%
a.discard(5)
# %%
print(a)
# %%
a.remove(2)
print(a)
# %%
a.clear()
print(a)
# %%
b.pop()
print(b)
# %%
