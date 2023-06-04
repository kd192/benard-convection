import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Ra.csv')  # Load Rayleigh number data from CSV file

# Sort DataFrame by time
df = df.sort_values(by='time')

plt.figure(figsize=(10, 6))  # Set the size of the figure
plt.scatter(df['time'], df['Ra'], label='Data', s=0.5)  # Plot time vs Ra using scatter plot

plt.axhline(1700, color='g', linestyle='--', label='Ra=1700')  # Add horizontal line at Ra=1700
plt.axhline(50000, color='r', linestyle='--', label='Ra=50000')  # Add horizontal line at Ra=50000

plt.xlabel('time')  # Label for x-axis
plt.ylabel('Ra')  # Label for y-axis
plt.title('Ra vs Time')  # Title of the plot
plt.legend()  # Add legend
plt.grid(True)  # Add grid
plt.show()  # Display the plot
