#%%
print("Hi")
x=7
def fun_lyrics():
    print("hi this is my function")
x=x+9
print(x)
fun_lyrics()
print("Yo this is bad")
# %%
def my_result(mark):
    if mark==80:
        print("A+")
    elif mark==70:
        print("A")
    elif mark==60:
        print("A-")
    else:
        print("This not your mark")

my_result(30)
# %%
def greet():
    return "hello"
print(greet(),"anika")
print(greet(),"fariha")
# %%
def greet(lang):
    if lang=="en":
        return "hola"
    elif lang=="es":
        return "hila"
    elif lang=="ef":
        return "babu"
    else:
        return "program end here"
greet("en")
# %%
greet("ef")
# %%
greet("525")

# %%




