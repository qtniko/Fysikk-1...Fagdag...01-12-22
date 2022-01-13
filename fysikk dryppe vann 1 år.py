T1 = 5 # Cold water temperature (celsius)
T2 = 44.5 # Hot water temperature (celsius)
m = 249 # Mass (amount of water in g)
t = 0.5 # Time spent collecting dripping water (in hours)
c = 4183 # Specific heat capacity (water, J/kgK)
eP = 158.01 # Electricity price (øre per kWh)

ePkr = eP/100 # Electricity price (kroner per kWh)
dT = T2 - T1 # Difference between hot and cold water temperature
mYear = (24/t)*(m/1000)*365 # Water in 1 year (mass in kg)
Q = c*mYear*dT # Power required to heat up water for a year (J)
QkWh = Q/(3.6*10**6) # Power required to heat up water for a year (kWh)

price = QkWh / ePkr

print(price)