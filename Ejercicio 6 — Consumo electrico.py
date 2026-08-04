consumption = [19, 22, 25, 27, 24, 21]

avg = sum(consumption) / len(consumption)

for index, value in enumerate(consumption):
    if value > avg:
        print(f"Hour {index}: {value} kWh")

# Output:
# Hour 1: 22 kWh
# Hour 2: 25 kWh
# Hour 3: 27 kWh
# Hour 4: 24 kWh