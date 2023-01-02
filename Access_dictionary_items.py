#%%
dict1={1:"anika",2:"fariha",3:"mango",4:"egg"}
dict1
# %%
dict1[2]
# %%
dict1[4]
# %%
dict2={1:"anika",2:"fariha",3:"mango",4:"egg",5:{1:"bangla",2:"physics",3:"chemistry","name":"Rakul Preet"}}
# %%
print(dict2)
# %%
dict2[5]
# %%
dict2[5][2]
# %%
dict2[5]["name"]
# %%
dict2={1:"anika",2:"fariha",3:"mango",4:"egg",5:{1:"bangla",2:"physics",3:"chemistry","name":"Rakul Preet"}}
# %%
dict2.get(5)
# can't access multiple value (nested dictionary can't access with get.item() only single value can access)
# %%
dict2.get(5)
# %%
