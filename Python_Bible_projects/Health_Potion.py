import random

health = 50 

# Difficulty = 1, 2, 3 (easy, normal, hard)
difficulty = 3

potion_health = int(random.randint(25, 50) / difficulty)
health = health + potion_health
print(health)

