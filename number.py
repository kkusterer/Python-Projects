combinations = []

for i in range(100):
    middle_part = str(i).zfill(3)
    combination = f"{middle_part}"
    combinations.append(combination)

for combo in combinations:
    print(combo)
