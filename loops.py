#%%
n=10
while n>20:
    print(n)
    n +=1
# %%
n=10
while n<20:
    print(n)
    n +=1

# print(n)
print("End")

# %%
# n=10
# while n>0:
#     print(n)
#     n -=1

# # print(n)
# print("End")
# %%
n=10
while n<20:
    print(n)
    n +=1

# print(n)
print("End")
# %%
for i in [1,2,3,4,5,6]:
    print(i)
print("End")

# %%
friends=["anika","rakib","shakib","tamim","angelina"]
for friend in friends:
    print("happy birthday idiots",friend)
print("end")
# %%
#find_large_number

large_number=-1

for i in [1,2,3,4,5,6,0]:
    if i>large_number:
        large_number=i
        
print(f"largest number is {large_number}")

print("End")

# %%
list1 = []
 
# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))
 
# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)
     
# print maximum element
print("Largest element is:", max(list1))

# %%
