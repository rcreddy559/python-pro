import random;

rand_int = random.randint(1, 20)
print(f"Random integer between 1 and 20: {rand_int}")

random_ = random.random()
print(f"Random float between 0.0 and 1.0: {random_.fromhex('0x1.0p-1')}")

random_choice = random.choice(['apple', 'banana', 'cherry'])
print(f"Random choice from list: {random_choice}" )

random_sample = random.sample(range(100), 3)
print(f"Random sample of 3 unique numbers from 0 to 99: {random_sample}")

random_shuffle = [1, 2, 3, 4, 5]
print(f"Original list before shuffle: {random_shuffle}")
random.shuffle(random_shuffle)
print(f"Randomly shuffled list: {random_shuffle}")

random_seed = random.seed(42)
print("Random seed set to 42. This will ensure reproducibility of random numbers.") 
