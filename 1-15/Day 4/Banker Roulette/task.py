friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

random_1 = random.randint(0, len(friends)-1)
print(friends[random_1])

print(random.choice(friends))