import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import transforms

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
mass_sun = 1.989e30  # Sun's mass in kg
mass_earth = 5.972e24  # Earth's mass in kg
mass_moon = 7.34767309e22  # Moon's mass in kg
distance_sun_earth = 1.496e11  # Distance from Earth to Sun in meters (1 AU)
distance_earth_moon = 3.844e8  # Distance from Earth to Moon in meters

# Initial conditions (positions and velocities)
earth_position = np.array([distance_sun_earth, 0.0], dtype=np.float64)  # Earth's position in meters
earth_velocity = np.array([0.0, 29780.0], dtype=np.float64)  # Earth's velocity in m/s (approx orbital velocity)

moon_position = earth_position + np.array([distance_earth_moon, 0.0], dtype=np.float64)  # Moon's position relative to Earth
moon_velocity = earth_velocity + np.array([0.0, 1022.0], dtype=np.float64)  # Moon's velocity relative to Earth

sun_position = np.array([0.0, 0.0], dtype=np.float64)  # Sun's position at the origin

# Time step and simulation duration
dt = 60 * 60  # Time step in seconds (1 hour)
num_steps = 10000  # Number of time steps

# Function to compute the gravitational force between two masses
def gravitational_force(m1, m2, r):
    return G * m1 * m2 / np.linalg.norm(r)**2 * r / np.linalg.norm(r)

# Simulation loop
earth_positions = []
moon_positions = []
earth_rotations = []  # For storing the Earth rotation angle
moon_rotations = []  # For storing the Moon rotation angle

# Calculate positions for a few steps (enough for the animation)
for _ in range(num_steps):
    # Distance vectors
    earth_to_sun = sun_position - earth_position
    earth_to_moon = moon_position - earth_position
    sun_to_moon = moon_position - sun_position

    # Gravitational forces
    F_sun_earth = gravitational_force(mass_sun, mass_earth, earth_to_sun)
    F_earth_moon = gravitational_force(mass_earth, mass_moon, earth_to_moon)
    F_sun_moon = gravitational_force(mass_sun, mass_moon, sun_to_moon)

    # Accelerations (F = ma => a = F / m)
    a_earth = F_sun_earth / mass_earth - F_earth_moon / mass_earth  # Earth's acceleration
    a_moon = F_earth_moon / mass_moon - F_sun_moon / mass_moon  # Moon's acceleration

    # Update velocities and positions
    earth_velocity += a_earth.astype(np.float64) * dt  # Ensure addition is done with float64
    moon_velocity += a_moon.astype(np.float64) * dt  # Ensure addition is done with float64
    earth_position += earth_velocity * dt
    moon_position += moon_velocity * dt

    # Calculate rotation angles (simple model: 1 rotation per day)
    earth_rotation = (earth_rotations[-1] + 360 / 86400) % 360 if earth_rotations else 0  # Earth's rotation (1 full rotation per day)
    moon_rotation = (moon_rotations[-1] + 360 / 2360600) % 360 if moon_rotations else 0  # Moon's rotation (1 full rotation per month)

    # Store positions and rotations for plotting
    earth_positions.append(earth_position.copy())
    moon_positions.append(moon_position.copy())
    earth_rotations.append(earth_rotation)
    moon_rotations.append(moon_rotation)

# Convert position arrays to numpy arrays for plotting
earth_positions = np.array(earth_positions)
moon_positions = np.array(moon_positions)

# Plotting and Animation setup
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Distance (m)')

# Plot Sun at the origin
sun = ax.scatter([sun_position[0]], [sun_position[1]], color='yellow', s=200, label="Sun")

# Plot Earth and Moon initially (empty)
earth_plot, = ax.plot([], [], 'bo', label="Earth")
moon_plot, = ax.plot([], [], 'go', label="Moon")

ax.legend()
ax.set_title("Earth, Sun, and Moon Gravitational Simulation")

# Function to update the animation at each frame
def update(frame):
    # Get the current Earth and Moon positions
    earth_plot.set_data(earth_positions[frame, 0], earth_positions[frame, 1])
    moon_plot.set_data(moon_positions[frame, 0], moon_positions[frame, 1])

    # Rotate Earth and Moon by updating the plot markers
    earth_rotation_matrix = np.array([[np.cos(np.radians(earth_rotations[frame])), -np.sin(np.radians(earth_rotations[frame]))],
                                      [np.sin(np.radians(earth_rotations[frame])), np.cos(np.radians(earth_rotations[frame]))]])
    
    moon_rotation_matrix = np.array([[np.cos(np.radians(moon_rotations[frame])), -np.sin(np.radians(moon_rotations[frame]))],
                                      [np.sin(np.radians(moon_rotations[frame])), np.cos(np.radians(moon_rotations[frame]))]])

    earth_position_rotated = earth_rotation_matrix @ earth_positions[frame]
    moon_position_rotated = moon_rotation_matrix @ moon_positions[frame]

    # Apply rotation transformation
    earth_plot.set_data(earth_position_rotated[0], earth_position_rotated[1])
    moon_plot.set_data(moon_position_rotated[0], moon_position_rotated[1])

    return earth_plot, moon_plot

# Create the animation
ani = FuncAnimation(fig, update, frames=len(earth_positions), interval=50, blit=False)

plt.show()
