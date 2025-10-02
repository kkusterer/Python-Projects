import os
import time

neutrons_to_add = int(input("how meany neutrons to add: "))

neutron_num = neutrons_to_add

Fission_produts = int(neutrons_to_add) + 2

start_time = time.perf_counter()

while neutron_num < 1000:

    time.sleep(.1)

    Fission_produts += 2

    neutron_num += 3

    os.system("clear")

    print(f"number of neutrons: {neutron_num}")

    print(f"number of Fission produts : {Fission_produts}")

end_time = time.perf_counter()

print(f"done with nn {neutron_num}\nfp : {Fission_produts}")

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.4f} seconds")
        