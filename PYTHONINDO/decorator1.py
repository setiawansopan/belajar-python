def smart_devide(func):
    def inner(a,b):
        print('saya akan membagi',a,'dan ',b)
        if b == 0:
            print('tidakbisa dibagi dengan 0')
            return
        
        return func(a,b)
    return inner

@smart_devide
def devide(a,b):
    return a/b

devide(2,5)