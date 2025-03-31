import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi

def plot_smith_chart():
    fig, ax = plt.subplots(figsize=(6,6))
    
    # Smith Chart Circles
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    
    # Outer Circle (Unit Circle)
    theta = np.linspace(0, 2 * pi, 500)
    ax.plot(np.cos(theta), np.sin(theta), 'k', linewidth=1)  # Outer boundary

    # Resistance Circles (Constant R)
    R_values = [0.2, 0.5, 1, 2, 5]  # Common normalized resistance values
    for R in R_values:
        x = (1 - R) / (1 + R)
        r = 1 / (1 + R)
        circle = plt.Circle((x, 0), r, color='blue', fill=False, linestyle="--", linewidth=0.7)
        ax.add_patch(circle)
    
    # Reactance Circles (Constant X)
    X_values = [0.5, 1, 2, 5]  # Common normalized reactance values
    for X in X_values:
        # Upper half-plane (positive reactance)
        x = 1
        y = 1 / X
        r = 1 / X
        ax.plot(x - r * np.cos(theta), y - r * np.sin(theta), 'r', linestyle="--", linewidth=0.7)
        
        # Lower half-plane (negative reactance)
        y = -1 / X
        ax.plot(x - r * np.cos(theta), y - r * np.sin(theta), 'r', linestyle="--", linewidth=0.7)
    
    # Axis Formatting
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Smith Chart", fontsize=14)
    ax.grid(False)
    
    plt.show()

# Call function to plot Smith Chart
plot_smith_chart()