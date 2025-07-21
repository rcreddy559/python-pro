fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

states_of_india = ["Andhra Pradesh", "Bihar", "Goa", "Karnataka", "Maharashtra", "Punjab", "Tamil Nadu", "Uttar Pradesh", "West Bengal"]

states_of_india.reverse()
print(f"States of India in reverse order: {states_of_india}")

reversed_states = states_of_india[::-1]
print(f"Reversed states of India: {reversed_states}")

states_of_india.sort()
print(f"States of India in alphabetical order: {states_of_india}")

states_of_india.append("Kerala")
print(f"States of India after appending 'Kerala': {states_of_india}")

states_of_india.insert(0, "Assam")
print(f"States of India after inserting 'Assam' at the beginning: {states_of_india}")

no_of_states = len(states_of_india)
print(f"Total number of states in India: {no_of_states}")

# replace 'Karnataka' with 'Telangana'
index_of_karnataka = states_of_india.index("Karnataka")
states_of_india[index_of_karnataka] = "Telangana"
print(f"States of India after replacing 'Karnataka' with 'Telangana': {states_of_india}")

# replace 'Bihar, Goa' with 'Jharkhand'
index_of_bihar = states_of_india.index("Bihar")
index_of_goa = states_of_india.index("Goa")
states_of_india[index_of_bihar] = "Jharkhand"
states_of_india.remove("Goa")

for state in states_of_india:
    print(f"State: {state.split()}")


two_word_states = [state for state in states_of_india if len(state.split()) == 2]
print(two_word_states)

