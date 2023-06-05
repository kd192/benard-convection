import os
import numpy as np
import pandas as pd
import subprocess 
from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile
from PyFoam.RunDictionary.TimeDirectory import TimeDirectory


#Ra = g * β * ΔT * L³ / (ν * α)

# Specify the directory of the OpenFOAM case
case_dir = ""

# Specify characteristic length
L =   # Characteristic length

# Specify gravity acceleration
g = 9.81  # m/s^2

# Specify the thermal expansion coefficient
beta = 0.00366 # See "/constant/transportProperties"

# Load the transport properties
print("Loading transport properties...")
transport_properties = ParsedParameterFile(os.path.join(case_dir, "constant/transportProperties"))

# Extract the density and dynamic viscosity
rhoRef = 1.225  # See "/constant/transportProperties"
nu = 0.000015  # See "/constant/transportProperties"

# Specify the thermal diffusivity
Pr = 10.000000 # See "/constant/transportProperties"
alpha =  0.022 # m^2/s

# Create a DataFrame to store the Rayleigh number for each time step
df = pd.DataFrame(columns=['time', 'Ra'])

print("Processing time directories...")
# Loop over the time directories
for time_dir in sorted(os.listdir(case_dir)):
    if time_dir.isdigit() and time_dir != "0":
        print(f"Processing directory: {time_dir}")
        # Load the temperature field
        T = ParsedParameterFile(os.path.join(case_dir, time_dir, "T"))
        T_field = np.array(T['internalField'])
        if T_field.ndim == 1:
            Delta_T = T_field.max() - T_field.min()
        else:
            Delta_T = T_field[:,0].max() - T_field[:,0].min()
        # Compute the Rayleigh number
        Ra = g * beta * Delta_T * L**3 / (nu * alpha)
        # Append to the DataFrame
        df = df._append({'time': float(time_dir), 'Ra': Ra}, ignore_index=True)

print("Saving results to CSV file...")
# Save the DataFrame to a CSV file
df.to_csv("Rayleigh_number.csv", index=False)

print("Done.")