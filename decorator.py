

def kundan(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using")
    return mfx

def add(a,b):
    print(a+b)

# @greet
def hello():
    print("Hello World!")

# add()
# hello()
# greet(hello())
kundan(add)(1,2)