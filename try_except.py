astr="hello"
try:
    istr=float(astr)
except:
    istr=-1
print("result",istr)

#%%
astr="12325"
try:
    istr=int(astr)
except:
    istr="hi"
print(istr)