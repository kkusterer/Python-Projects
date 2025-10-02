import os
import time
import random

# ----------------------
# Physical constants
# ----------------------
EV_TO_J = 1.602176634e-19       # electronvolt to joules
MEV_TO_J = EV_TO_J * 1e6        # Mega electronvolt to joules
J_TO_KWH = 1.0 / 3.6e6          # joules to kilowatt-hour
J_TO_TON_TNT = 1.0 / 4.184e9    # joules to tons of TNT
J_TO_GRAM_TNT = 1.0 / 4184.0    # joules to grams of TNT
AVOGADRO = 6.02214076e23        # atoms/mole

# ----------------------
# Atom being simulated
# ----------------------
atom_name = "Uranium-235 (U-235)"

# ----------------------
# User inputs
# ----------------------
initial_neutrons = int(input("Starting neutrons [default 1]: ") or 1)

max_generations = int(input("Number of generations [default 10]: ") or 10)
    #Fewer than 5 → small chain reaction, minimal growth.
    #More than 15 → energy numbers explode quickly (millions of times higher than real reactor scale).

fission_probability = float(input("Fission probability [default 0.7]: ") or 0.7)

scale_moles = float(input("Scale simulation to how many moles? [default 1]: ") or 1)
    #0.001 mole → ~1e21 atoms → ~hundreds of kWh → safe to simulate.    
    #1 mole → ~6e23 atoms → millions of kWh → matches typical textbook energy examples.
    #10+ moles → extreme energies → only for theory, not real-life lab.
    #Classroom demo	0.001 – 0.01 moles
    #Realistic reactor fuel	1 mole
    #Bomb-scale (theoretical) 10+ moles

# parameters

neutrons_per_fission_min = 2
neutrons_per_fission_max = 3
energy_per_fission_MeV = 200

#variables
neutrons = initial_neutrons
total_fissions = 0
total_energy_MeV = 0.0
generation = 0

start_time = time.perf_counter()


while generation < max_generations and neutrons > 0:
    fissions_this_gen = 0
    new_neutrons = 0

    for _ in range(int(neutrons)):
        if random.random() < fission_probability:
            fissions_this_gen += 1
            new_neutrons += random.randint(neutrons_per_fission_min, neutrons_per_fission_max)

    total_fissions += fissions_this_gen
    total_energy_MeV += fissions_this_gen * energy_per_fission_MeV
    neutrons = new_neutrons
    generation += 1

    
    os.system("cls" if os.name == "nt" else "clear")
    print(f"--- Generation {generation} ---")
    print(f"Atom simulated        : {atom_name}")
    print(f"Fission probability   : {fission_probability}")
    print(f"Active neutrons       : {int(neutrons):,}")
    print(f"Fissions this gen     : {fissions_this_gen:,}")
    print(f"Total fissions so far : {total_fissions:,}")
    print(f"Total energy (MeV)    : {total_energy_MeV:,.2f}")
    time.sleep(0.15)


if total_fissions == 0:
    print("\nNo fissions occurred in the simulation.")
    scale_factor = 0
    scaled_total_fissions = 0
    scaled_total_energy_MeV = 0
    total_energy_J = 0
    total_energy_kWh = 0
    total_energy_tons_TNT = 0
    total_energy_grams_TNT = 0
    moles_fissioned = 0
else:
    scale_factor = (AVOGADRO * scale_moles) / total_fissions
    scaled_total_fissions = total_fissions * scale_factor
    scaled_total_energy_MeV = total_energy_MeV * scale_factor

    total_energy_J = scaled_total_energy_MeV * MEV_TO_J
    total_energy_kWh = total_energy_J * J_TO_KWH
    total_energy_tons_TNT = total_energy_J * J_TO_TON_TNT
    total_energy_grams_TNT = total_energy_J * J_TO_GRAM_TNT
    moles_fissioned = scaled_total_fissions / AVOGADRO

energy_if_one_mole_J = AVOGADRO * energy_per_fission_MeV * MEV_TO_J
end_time = time.perf_counter()

os.system("cls" if os.name == "nt" else "clear")
print("\n--- Simulation finished ---")
print(f"Atom simulated          : {atom_name}")
print(f"Fission probability     : {fission_probability}")
print(f"Generations simulated   : {generation}")
print(f"Simulation scaled to    : {scale_moles} mole(s)")
print(f"Total fissions (scaled) : {scaled_total_fissions:,.6g}")
print(f"Total energy (MeV)      : {scaled_total_energy_MeV:,.6g} MeV")
print(f"Total energy (J)        : {total_energy_J:.6e} J")
print(f"Total energy (kWh)      : {total_energy_kWh:.6e} kWh")
print(f"Total energy (TNT)      : {total_energy_tons_TNT:.6e} tons")
print(f"Total energy (g TNT)    : {total_energy_grams_TNT:.6e} g")
print(f"Moles fissioned         : {moles_fissioned:.6e} mol")
print(f"If 1 mole fissioned ->  : {energy_if_one_mole_J:.6e} J (~{energy_if_one_mole_J * J_TO_KWH:.6e} kWh)")
print(f"Elapsed time            : {end_time - start_time:.4f} seconds")
