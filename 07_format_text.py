class Person:
    def __init__(self):    
        self.name = "momo"
        self.age = "3.5"


text = {
    "name":"eric",
    "age":"36"
}



print("测试一下，替换的文字是：{0}".format("23"))

print("hi, I am {person[name]}, i am {person[age]}".format(person=text))

momo = Person()
print("hi, I am {momo.name}, i am {momo.age}".format(momo=momo))
