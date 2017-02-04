import random

city = [line.strip() for line in open('cities.txt')]
team = [line.strip() for line in open('memes.txt')]

for i in range(10):
    print(str(random.choice(city) + ' ' + str(random.choice(team))))