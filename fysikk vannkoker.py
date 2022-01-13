T1 = 20 # Room temperature before (celsius)
T2 = 44 # Water temperature before (celsius)
T3 = 30 # Kettle temperature after (celsius)
m = 0.2 # Mass (amount of water in kg)
c = 4183 # Specific heat capacity (water, J/kgK)

dT = T2 - T3 # Difference between water and kettle temperature
k_Q = c*m*dT # Heat trasferred to kettle from water (J)
k_C = k_Q/dT # Heat capacity of kettle (J/K)

print(f"Heat capacity of kettle (J/K): {k_C}")

T1 = 8 # Water in kettle temperature before (celsius)
T2 = 100 # Water in kettle temperature after (celsius)
m = 1 # Mass (amount of water in kg)
t = 235 # Time elapsed (from T1 to T2, seconds)
c = 4183 # Specific heat capacity (water, J/kgK)

dT = T2 - T1 # Difference in water tempereature before and after
w_Q = c*m*dT # Heat trasferred to water from input (J)
w_C = w_Q/dT # Heat capacity of water (J/K)

sC = k_C + w_C # Heat capacity of system (kettle + water)
sQ = sC*dT # Heat of system based on difference in temperature (J)

print(f"Heat capacity of system (kettle + water, J/K): {sC}\nHeat of system based on difference in temperature (J): {sQ}")

W = 1920 # Work of kettle (J) 1920-2280

COP = sQ/W # Coefficient of Performance

print(f"Coefficient of Performance: {COP}")