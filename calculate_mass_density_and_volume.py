# mdv = mass_density_volume
mdv = input("Choose one to calculate(m,d,v): ")

# check user input
if mdv == 'm':
    density = float(input("Density: "))
    volume = float(input("Volume: "))
    # for mass only
    result = density * volume
elif mdv == 'd':
    mass = float(input("Mass: "))
    volume = float(input("Volume: "))
    # for density only
    result = mass / volume
elif mdv == 'v':
    mass = float(input("Mass: "))
    density = float(input("Density: "))
    # for volume only
    result = mass / density
print("%.2f" % result)
