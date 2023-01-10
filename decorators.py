#%%
def my_func(arg):
    print("hi")
    print("hello")
    print(arg)
    
my_func(45)
# %%
name="Fariha"
def this_is_my_decorator(function_1):
    def wrap_function(arg):
        if name.startswith("F"):
            
            function_1(arg)
    return wrap_function
    
@this_is_my_decorator
def my_func(arg):
    print("hi")
    print("hello")
    print(arg)
    
my_func(45)
# %%
#Generator

def func():
    i=0
    while  True:
        yield i
        i=i+1
a=func()
print(type(a))
print(a)
print(next(a))
print(next(a))
print(next(a))

# %%
print(next(a))

# %%
