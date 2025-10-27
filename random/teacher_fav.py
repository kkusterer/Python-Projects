import csv

with open("fav_data.csv" ,"r") as file:
        reader = csv.DictReader(file)
        counts ={}
        for row in reader:
                fav = row["Teachers"]
                if fav in counts:
                        counts[fav] += 1
                else:
                        counts[fav] = 1

for fav in sorted(counts, key=counts.get, reverse=True):
        print(f"{fav}: {counts[fav]}")
