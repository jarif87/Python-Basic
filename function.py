#%%
def add():
    a=10
    b=9
    print(a+b)
add()
# %%
def add(a,b):
 
    print(a+b)
add(0,8)
# %%
add(3,5)
# %%
def addition(a,b):
    c=a+b
    return c
u=addition(10,40)

# %%
print(f"sum is {u}")
# %%
def add(a,b):
 
    c=a+b
    return c
x=add(0,8)
# %%
print(x)

# %%
def math(a,b,c=19): # default arguments
    
    x=a+b+c
    return x
math(1,2)
    
# %%
def math(a,b,c=19): # keyword  arguments
    
    x=a+b+c
    return x
math(a=10,b=6,c=99)

# %%
  # variable length arguments
def variable_length_arguments(*args):
    print(args)
variable_length_arguments(1,2,3,4,5,5,6,"bangla")
    
                                                                                            
# %%
def my_func(a,b,c):
    print(a,",",b,",",c)
m=["bangla","english","hindi"]
my_func(*m)
# %%
m="cat"
my_func(*m)
# %%
def my_fun(**kwargs):
    print(kwargs)
my_fun(bangla=10,english=60,math=90)
# %%
def my_fun(**kwargs):
    for i in kwargs:
        if kwargs [i]>40:
            print(i)
    # print(kwargs)
my_fun(bangla=10,english=60,math=90)

# %%
def my_func(arg):
    arg.append("hi")
    print(arg)
n=[1,2,3,4,5,"bangla"]
my_func(n)

# %%




