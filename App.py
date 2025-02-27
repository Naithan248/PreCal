#!/usr/bin/env python3
"""
Precalculus Complete Guide - Interactive Python Script
=====================================================

This script provides an interactive way to explore precalculus concepts,
with special emphasis on trigonometry. It includes calculations, visualizations,
and explanations for key precalculus topics.

Requirements:
- Python 3.6+
- NumPy
- Matplotlib
- SymPy
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from sympy import symbols, solve, simplify, expand, factor, sin, cos, tan, pi, sympify
import sys
import os

class PrecalculusGuide:
    def __init__(self):
        self.topics = {
            "1": {"name": "Fundamentals", "function": self.fundamentals},
            "2": {"name": "Polynomial & Rational Functions", "function": self.polynomial_rational},
            "3": {"name": "Exponential & Logarithmic Functions", "function": self.exponential_logarithmic},
            "4": {"name": "Trigonometry", "function": self.trigonometry_menu},
            "5": {"name": "Analytic Geometry", "function": self.analytic_geometry},
            "6": {"name": "Vectors & Matrices", "function": self.vectors_matrices},
            "7": {"name": "Sequences & Series", "function": self.sequences_series},
            "8": {"name": "Introduction to Calculus", "function": self.intro_calculus},
            "9": {"name": "Exit", "function": sys.exit}
        }
        
        self.trig_topics = {
            "1": {"name": "Angle Measure", "function": self.angle_measure},
            "2": {"name": "Unit Circle", "function": self.unit_circle},
            "3": {"name": "Trigonometric Functions", "function": self.trig_functions},
            "4": {"name": "Graphs of Trig Functions", "function": self.trig_graphs},
            "5": {"name": "Inverse Trig Functions", "function": self.inverse_trig},
            "6": {"name": "Trigonometric Identities", "function": self.trig_identities},
            "7": {"name": "Solving Trig Equations", "function": self.solving_trig_equations},
            "8": {"name": "Law of Sines & Cosines", "function": self.law_sines_cosines},
            "9": {"name": "Return to Main Menu", "function": self.main_menu}
        }
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def press_enter_to_continue(self):
        """Wait for user to press Enter."""
        input("\nPress Enter to continue...")
        
    def main_menu(self):
        """Display the main menu."""
        self.clear_screen()
        print("=== PRECALCULUS COMPLETE GUIDE ===")
        print("\nSelect a topic to explore:")
        
        for key, topic in self.topics.items():
            print(f"{key}. {topic['name']}")
            
        choice = input("\nEnter your choice (1-9): ")
        
        if choice in self.topics:
            self.topics[choice]["function"]()
        else:
            print("Invalid choice. Please try again.")
            self.press_enter_to_continue()
            self.main_menu()
            
    def trigonometry_menu(self):
        """Display the trigonometry submenu."""
        self.clear_screen()
        print("=== TRIGONOMETRY ===")
        print("\nSelect a trigonometry topic to explore:")
        
        for key, topic in self.trig_topics.items():
            print(f"{key}. {topic['name']}")
            
        choice = input("\nEnter your choice (1-9): ")
        
        if choice in self.trig_topics:
            self.trig_topics[choice]["function"]()
        else:
            print("Invalid choice. Please try again.")
            self.press_enter_to_continue()
            self.trigonometry_menu()
    
    # Basic topic placeholders
    def fundamentals(self):
        self.clear_screen()
        print("=== FUNDAMENTALS ===")
        print("This section covers:")
        print("- Real numbers")
        print("- Cartesian coordinates")
        print("- Functions introduction")
        print("- Function operations")
        print("- Function transformations")
        # Additional content would go here
        self.press_enter_to_continue()
        self.main_menu()
        
    def polynomial_rational(self):
        self.clear_screen()
        print("=== POLYNOMIAL & RATIONAL FUNCTIONS ===")
        print("This section covers:")
        print("- Polynomials")
        print("- Rational functions")
        print("- Partial fractions")
        print("- Asymptotes")
        # Additional content would go here
        self.press_enter_to_continue()
        self.main_menu()
        
    def exponential_logarithmic(self):
        self.clear_screen()
        print("=== EXPONENTIAL & LOGARITHMIC FUNCTIONS ===")
        print("This section covers:")
        print("- Exponential functions")
        print("- Logarithmic functions")
        print("- Solving exponential and logarithmic equations")
        print("- Applications")
        # Additional content would go here
        self.press_enter_to_continue()
        self.main_menu()
        
    def analytic_geometry(self):
        self.clear_screen()
        print("=== ANALYTIC GEOMETRY ===")
        print("This section covers:")
        print("- Conics introduction")
        print("- Circles")
        print("- Ellipses")
        print("- Hyperbolas")
        print("- Parabolas")
        # Additional content would go here
        self.press_enter_to_continue()
        self.main_menu()
        
    def vectors_matrices(self):
        self.clear_screen()
        print("=== VECTORS & MATRICES ===")
        print("This section covers:")
        print("- Vectors")
        print("- Dot and cross products")
        print("- Matrices")
        print("- Matrix operations")
        print("- Determinants")
        print("- Systems of equations")
        # Additional content would go here
        self.press_enter_to_continue()
        self.main_menu()
        
    def sequences_series(self):
        self.clear_screen()
        print("=== SEQUENCES & SERIES ===")
        print("This section covers:")
        print("- Sequences")
        print("- Series")
        print("- Arithmetic sequences")
        print("- Geometric sequences")
        print("- Binomial theorem")
        # Additional content would go here
        self.press_enter_to_continue()
        self.main_menu()
        
    def intro_calculus(self):
        self.clear_screen()
        print("=== INTRODUCTION TO CALCULUS ===")
        print("This section covers:")
        print("- Limits")
        print("- Continuity")
        print("- Derivative preview")
        print("- Applications")
        # Additional content would go here
        self.press_enter_to_continue()
        self.main_menu()
    
    # Trigonometry detailed implementations
    def angle_measure(self):
        self.clear_screen()
        print("=== ANGLE MEASURE ===")
        print("\nDegrees vs. Radians:")
        print("- Degrees: A full circle is 360°")
        print("- Radians: A full circle is 2π radians")
        print("- Conversion: π radians = 180°")
        print("- Formula: radians = (degrees × π) / 180")
        
        print("\nImportant Angle Measurements:")
        angles = [
            ("0°", "0", "0"),
            ("30°", "π/6", "π/6"),
            ("45°", "π/4", "π/4"),
            ("60°", "π/3", "π/3"),
            ("90°", "π/2", "π/2"),
            ("180°", "π", "π"),
            ("270°", "3π/2", "3π/2"),
            ("360°", "2π", "2π")
        ]
        
        print(f"{'Degrees':<10}{'Radians':<12}{'Simplified':<15}")
        print("-" * 37)
        for deg, rad, simp in angles:
            print(f"{deg:<10}{rad:<12}{simp:<15}")
            
        print("\nArc Length:")
        print("- s = rθ (where s = arc length, r = radius, θ = angle in radians)")
        
        print("\nSector Area:")
        print("- A = (1/2)r²θ (where A = sector area, r = radius, θ = angle in radians)")
        
        # Interactive converter
        print("\n=== Angle Converter ===")
        try:
            choice = input("Convert (1) Degrees to Radians or (2) Radians to Degrees? ")
            if choice == "1":
                degrees = float(input("Enter angle in degrees: "))
                radians = degrees * math.pi / 180
                print(f"{degrees}° = {radians:.6f} radians = {self.format_radians(radians)}")
            elif choice == "2":
                radians = float(input("Enter angle in radians (as a multiple of π, e.g., 0.5 for π/2): "))
                pi_notation = self.format_radians(radians * math.pi)
                degrees = radians * 180
                print(f"{radians} = {pi_notation} = {degrees:.2f}°")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        self.press_enter_to_continue()
        self.trigonometry_menu()
        
    def format_radians(self, radians):
        """Format radians in terms of π."""
        if radians == 0:
            return "0"
        elif radians == math.pi:
            return "π"
        elif radians == -math.pi:
            return "-π"
        else:
            frac = radians / math.pi
            if frac == int(frac):
                return f"{int(frac)}π"
            else:
                # Find a simple fraction approximation
                for denom in range(1, 13):
                    for num in range(-12, 13):
                        if abs(frac - num/denom) < 1e-10:
                            if denom == 1:
                                return f"{num}π"
                            else:
                                return f"{num}π/{denom}"
                return f"{frac:.4f}π"
                
    def unit_circle(self):
        self.clear_screen()
        print("=== THE UNIT CIRCLE ===")
        print("\nBasic Concept:")
        print("- A unit circle has radius 1 and is centered at the origin (0, 0)")
        print("- Any point (x, y) on the unit circle satisfies x² + y² = 1")
        print("- For an angle θ in standard position:")
        print("  - x-coordinate = cos θ")
        print("  - y-coordinate = sin θ")
        
        print("\nUnit Circle Coordinates:")
        coordinates = [
            ("0°", "0", "(1, 0)"),
            ("30°", "π/6", "(√3/2, 1/2)"),
            ("45°", "π/4", "(√2/2, √2/2)"),
            ("60°", "π/3", "(1/2, √3/2)"),
            ("90°", "π/2", "(0, 1)"),
            ("120°", "2π/3", "(-1/2, √3/2)"),
            ("135°", "3π/4", "(-√2/2, √2/2)"),
            ("150°", "5π/6", "(-√3/2, 1/2)"),
            ("180°", "π", "(-1, 0)"),
            ("210°", "7π/6", "(-√3/2, -1/2)"),
            ("225°", "5π/4", "(-√2/2, -√2/2)"),
            ("240°", "4π/3", "(-1/2, -√3/2)"),
            ("270°", "3π/2", "(0, -1)"),
            ("300°", "5π/3", "(1/2, -√3/2)"),
            ("315°", "7π/4", "(√2/2, -√2/2)"),
            ("330°", "11π/6", "(√3/2, -1/2)"),
            ("360°", "2π", "(1, 0)")
        ]
        
        print(f"{'Degrees':<10}{'Radians':<10}{'Coordinates (cos θ, sin θ)':<30}")
        print("-" * 50)
        for deg, rad, coord in coordinates:
            print(f"{deg:<10}{rad:<10}{coord:<30}")
        
        # Visual unit circle
        try:
            print("\nWould you like to see a visual representation of the unit circle? (y/n)")
            choice = input()
            if choice.lower() == 'y':
                self.plot_unit_circle()
        except Exception as e:
            print(f"Unable to display plot: {e}")
        
        self.press_enter_to_continue()
        self.trigonometry_menu()
        
    def plot_unit_circle(self):
        """Plot the unit circle with key angles."""
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Draw the unit circle
        circle = plt.Circle((0, 0), 1, fill=False)
        ax.add_artist(circle)
        
        # Draw coordinate axes
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Set equal aspect ratio
        ax.set_aspect('equal')
        
        # Set limits
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        
        # Add labels
        ax.set_title('Unit Circle')
        ax.set_xlabel('cos θ')
        ax.set_ylabel('sin θ')
        
        # Add key points on the unit circle
        angles = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, 2*math.pi/3, 3*math.pi/4, 
                  5*math.pi/6, math.pi, 7*math.pi/6, 5*math.pi/4, 4*math.pi/3, 
                  3*math.pi/2, 5*math.pi/3, 7*math.pi/4, 11*math.pi/6]
        
        labels = ["0°", "30°", "45°", "60°", "90°", "120°", "135°", "150°", 
                  "180°", "210°", "225°", "240°", "270°", "300°", "315°", "330°"]
        
        for angle, label in zip(angles, labels):
            x = math.cos(angle)
            y = math.sin(angle)
            ax.plot(x, y, 'ro', markersize=5)
            ax.text(x*1.1, y*1.1, label, fontsize=9)
            ax.plot([0, x], [0, y], 'r--', alpha=0.3)
        
        plt.grid(True)
        plt.show()
    
    def trig_functions(self):
        self.clear_screen()
        print("=== TRIGONOMETRIC FUNCTIONS ===")
        print("\nThe Six Trigonometric Functions:")
        print("For an angle θ in standard position with point (x, y) on the terminal ray at distance r from origin:")
        
        functions = [
            ("Sine", "sin θ = y/r", "sin θ = y"),
            ("Cosine", "cos θ = x/r", "cos θ = x"),
            ("Tangent", "tan θ = y/x", "tan θ = y/x"),
            ("Cosecant", "csc θ = r/y", "csc θ = 1/y"),
            ("Secant", "sec θ = r/x", "sec θ = 1/x"),
            ("Cotangent", "cot θ = x/y", "cot θ = x/y")
        ]
        
        print(f"\n{'Function':<12}{'Definition':<18}{'Unit Circle (r=1)':<20}")
        print("-" * 50)
        for func, defn, unit in functions:
            print(f"{func:<12}{defn:<18}{unit:<20}")
            
        print("\nRight Triangle Definitions:")
        print("For a right triangle with angle θ:")
        
        rt_functions = [
            ("sin θ", "Opposite side / Hypotenuse"),
            ("cos θ", "Adjacent side / Hypotenuse"),
            ("tan θ", "Opposite side / Adjacent side"),
            ("csc θ", "Hypotenuse / Opposite side"),
            ("sec θ", "Hypotenuse / Adjacent side"),
            ("cot θ", "Adjacent side / Opposite side")
        ]
        
        print(f"\n{'Function':<8}{'Definition':<35}")
        print("-" * 43)
        for func, defn in rt_functions:
            print(f"{func:<8}{defn:<35}")
            
        print("\nDomains and Ranges:")
        domains_ranges = [
            ("sin θ", "All real numbers", "[-1, 1]"),
            ("cos θ", "All real numbers", "[-1, 1]"),
            ("tan θ", "All real numbers except θ = π/2 + nπ", "All real numbers"),
            ("csc θ", "All real numbers except θ = nπ", "(-∞, -1] ∪ [1, ∞)"),
            ("sec θ", "All real numbers except θ = π/2 + nπ", "(-∞, -1] ∪ [1, ∞)"),
            ("cot θ", "All real numbers except θ = nπ", "All real numbers")
        ]
        
        print(f"\n{'Function':<8}{'Domain':<40}{'Range':<25}")
        print("-" * 73)
        for func, domain, range_ in domains_ranges:
            print(f"{func:<8}{domain:<40}{range_:<25}")
            
        print("\nKey Identities:")
        print("- Reciprocal Identities: csc θ = 1/sin θ, sec θ = 1/cos θ, cot θ = 1/tan θ")
        print("- Quotient Identities: tan θ = sin θ/cos θ, cot θ = cos θ/sin θ")
        print("- Pythagorean Identities: sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, 1 + cot²θ = csc²θ")
        
        # Interactive trig calculator
        print("\n=== Trigonometric Function Calculator ===")
        try:
            # Get input angle
            angle_str = input("Enter an angle in degrees or radians (e.g., '45' or 'pi/4'): ")
            is_degrees = True
            
            # Check if input is in radians using π
            if 'pi' in angle_str.lower() or 'π' in angle_str:
                is_degrees = False
                angle_str = angle_str.lower().replace('π', 'pi')
                angle = float(eval(angle_str, {"pi": math.pi}))
            else:
                angle = float(angle_str)
                if not is_degrees:
                    angle_rad = angle
                else:
                    angle_rad = math.radians(angle)
            
            # Calculate trig values
            sin_val = math.sin(angle_rad)
            cos_val = math.cos(angle_rad)
            
            # Print results
            if is_degrees:
                print(f"\nValues for {angle}° ({angle_rad:.4f} radians):")
            else:
                print(f"\nValues for {angle_str} radians ({math.degrees(angle_rad):.2f}°):")
                
            print(f"sin = {sin_val:.6f}")
            print(f"cos = {cos_val:.6f}")
            
            # Handle special cases for tan, csc, sec, cot
            if abs(cos_val) < 1e-10:
                print("tan = undefined (division by zero)")
                print("sec = undefined (division by zero)")
            else:
                print(f"tan = {math.tan(angle_rad):.6f}")
                print(f"sec = {1/cos_val:.6f}")
                
            if abs(sin_val) < 1e-10:
                print("csc = undefined (division by zero)")
                print("cot = undefined (division by zero)")
            else:
                print(f"csc = {1/sin_val:.6f}")
                if abs(cos_val) < 1e-10:
                    print("cot = 0")
                else:
                    print(f"cot = {cos_val/sin_val:.6f}")
                    
        except Exception as e:
            print(f"Error in calculation: {e}")
            
        self.press_enter_to_continue()
        self.trigonometry_menu()
    
    def trig_graphs(self):
        self.clear_screen()
        print("=== GRAPHS OF TRIGONOMETRIC FUNCTIONS ===")
        
        print("\nSine Function:")
        print("- f(x) = sin x")
        print("- Domain: All real numbers")
        print("- Range: [-1, 1]")
        print("- Period: 2π")
        
        print("\nCosine Function:")
        print("- f(x) = cos x")
        print("- Domain: All real numbers")
        print("- Range: [-1, 1]")
        print("- Period: 2π")
        
        print("\nTangent Function:")
        print("- f(x) = tan x")
        print("- Domain: All real numbers except x = π/2 + nπ")
        print("- Range: All real numbers")
        print("- Period: π")
        print("- Vertical asymptotes at x = π/2 + nπ")
        
        print("\nTransformations of Trigonometric Functions:")
        print("For a function of the form f(x) = A sin(Bx - C) + D:")
        print("- |A| is the amplitude (for sine and cosine only)")
        print("- 2π/|B| is the period")
        print("- C/B is the phase shift (right if positive, left if negative)")
        print("- D is the vertical shift")
        
        # Interactive graph visualizer
        print("\n=== Trigonometric Function Visualizer ===")
        try:
            print("Which function would you like to visualize?")
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            print("4. Transformed Trig Function")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                self.plot_trig_function(np.sin, "Sine Function (sin x)")
            elif choice == "2":
                self.plot_trig_function(np.cos, "Cosine Function (cos x)")
            elif choice == "3":
                self.plot_trig_function(np.tan, "Tangent Function (tan x)", True)
            elif choice == "4":
                # Get parameters for transformed function
                try:
                    print("\nEnter parameters for f(x) = A sin(Bx - C) + D:")
                    A = float(input("A (amplitude): "))
                    B = float(input("B (affects period): "))
                    C = float(input("C (affects phase shift): "))
                    D = float(input("D (vertical shift): "))
                    
                    func_type = input("Function type (sin, cos, tan): ").lower()
                    if func_type == "sin":
                        base_func = np.sin
                        title = f"{A} sin({B}x - {C}) + {D}"
                    elif func_type == "cos":
                        base_func = np.cos
                        title = f"{A} cos({B}x - {C}) + {D}"
                    elif func_type == "tan":
                        base_func = np.tan
                        title = f"{A} tan({B}x - {C}) + {D}"
                    else:
                        print("Invalid function type. Using sine.")
                        base_func = np.sin
                        title = f"{A} sin({B}x - {C}) + {D}"
                    
                    # Create transformed function
                    def transformed_func(x):
                        return A * base_func(B * x - C) + D
                    
                    self.plot_trig_function(transformed_func, title, func_type == "tan")
                    
                except ValueError:
                    print("Invalid parameter. Please enter numeric values.")
            else:
                print("Invalid choice.")
                
        except Exception as e:
            print(f"Error in plotting: {e}")
            
        self.press_enter_to_continue()
        self.trigonometry_menu()
        
    def plot_trig_function(self, func, title, is_tan=False):
        """Plot a trigonometric function."""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if is_tan:
            # For tangent, use a smaller domain to show the asymptotes
            x = np.linspace(-2*np.pi, 2*np.pi, 1000)
            y = np.array([func(val) for val in x])
            
            # Filter out values that are too large
            mask = np.abs(y) < 10
            x_filtered = x[mask]
            y_filtered = y[mask]
            
            ax.plot(x_filtered, y_filtered)
            
            # Add asymptote lines
            for i in range(-2, 3):
                asymptote = np.pi/2 + i*np.pi
                ax.axvline(x=asymptote, color='r', linestyle='--', alpha=0.5)
                
            ax.set_ylim(-5, 5)
        else:
            # For sine and cosine, use a regular domain
            x = np.linspace(-2*np.pi, 2*np.pi, 1000)
            y = func(x)
            ax.plot(x, y)
            ax.set_ylim(-3, 3)
        
        # Add gridlines and labels
        ax.grid(True)
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Mark π values on x-axis
        pi_ticks = np.arange(-2*np.pi, 2.1*np.pi, np.pi/2)
        pi_labels = ["-2π", "-3π/2", "-π", "-π/2", "0", "π/2", "π", "3π/2", "2π"]
        ax.set_xticks(pi_ticks)
        ax.set_xticklabels(pi_labels)
        
        ax.set_title(title)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        
        plt.show()
    
    def inverse_trig(self):
        self.clear_screen()
        print("=== INVERSE TRIGONOMETRIC FUNCTIONS ===")
        
        print("\nDefinitions and Notation:")
        print("- arcsin x = sin⁻¹ x: The angle whose sine is x")
        print("- arccos x = cos⁻¹ x: The angle whose cosine is x")
        print("- arctan x = tan⁻¹ x: The angle whose tangent is x")
        print("- arccsc x = csc⁻¹ x: The angle whose cosecant is x")
        print("- arcsec x = sec⁻¹ x: The angle whose secant is x")
        print("- arccot x = cot⁻¹ x: The angle whose cotangent is x")
        
        print("\nDomains and Ranges:")
        domains_ranges = [
            ("arcsin x", "[-1, 1]", "[-π/2, π/2]"),
            ("arccos x", "[-1, 1]", "[0, π]"),
            ("arctan x", "All real numbers", "(-π/2, π/2)"),
            ("arccsc x", "(-∞, -1] ∪ [1, ∞)", "[-π/2, 0) ∪ (0, π/2]"),
            ("arcsec x", "(-∞, -1] ∪ [1, ∞)", "[0, π/2) ∪ (π/2, π]"),
            ("arccot x", "All real numbers", "(0, π)")
        ]
        
        print(f"\n{'Function':<10}{'Domain':<25}{'Range':<25}")
        print("-" * 60)
        for func, domain, range_ in domains_ranges:
            print(f"{func:<10}{domain:<25}{range_:<25}")
            
        print("\nKey Values:")
        key_values = [
            ("x", "arcsin x", "arccos x", "arctan x"),
            ("-1", "-π/2", "π", "-π/4"),
            ("-√3/2", "-π/3", "5π/6", "-"),
            ("-√2/2", "-π/4", "3π/4", "-"),
            ("-1/2", "-π/6", "2π/3", "-"),
            ("0", "0", "π/2", "0"),
            ("1/2", "π/6", "π/3", "-"),
            ("√2/2", "π/4", "π/4", "π/4"),
            ("√3/2", "π/3", "π/6", "-"),
            ("1", "π/2", "0", "π/4")
        ]
        
        print(f"\n{'x':<10}{'arcsin x':<15}{'arccos x':<15}{'arctan x':<15}")
        print("-" * 55)
        for row in key_values[1:]:
            print(f"{row[0]:<10}{row[1]:<15}{row[2]:<15}{row[3]:<15}")
            
        print("\nImportant Identities:")
        print("- arcsin(-x) = -arcsin x")
        print("- arccos(-x) = π - arccos x")
        print("- arctan(-x) = -arctan x")
        print("- arcsin x + arc
