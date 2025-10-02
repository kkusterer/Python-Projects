import os
import time
import random

initial_neutrons = int(input("How many neutrons to start with: "))
max_generations = int(input("How many generations to simulate: "))
fission_probability = 0.7  
avg_neutrons_per_fission = (2, 3)
energy_per_fission = 200 

neutrons = initial_neutrons
total_fissions = 0
total_energy = 0.0
generation = 0

start_time = time.perf_counter()

while generation < max_generations and neutrons > 0:
    new_neutrons = 0
    fissions_this_gen = 0

    for _ in range(neutrons):
        if random.random() < fission_probability:
            fissions_this_gen += 1
            total_fissions += 1
            total_energy += energy_per_fission
            new_neutrons += random.randint(*avg_neutrons_per_fission)


    neutrons = new_neutrons
    generation += 1

    os.system("cls" if os.name == "nt" else "clear")
    print(f"--- Generation {generation} ---")
    print(f"Active neutrons     : {neutrons}")
    print(f"Fissions this gen   : {fissions_this_gen}")
    print(f"Total fissions      : {total_fissions}")
    print(f"Total energy (MeV)  : {total_energy}")
    time.sleep(0.2)

end_time = time.perf_counter()
os.system("cls" if os.name == "nt" else "clear")
print("\n--- Simulation finished ---")
print(f"Generations simulated: {generation}")
print(f"Total fissions       : {total_fissions}")
print(f"Total energy (MeV)   : {total_energy}")
print(f"Elapsed time         : {end_time - start_time:.4f} seconds")
