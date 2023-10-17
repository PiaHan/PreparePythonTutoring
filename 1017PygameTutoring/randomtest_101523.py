import random
print(random.random())
print(random.randint(1,10))
print(random.randrange(0,10,2))

print("----------*****-----------")

li = [10, 20, 30, 40, 50]
print(li)
print(random.choice(li))
print(random.sample(li, 2))
random.shuffle(li)
print(li)