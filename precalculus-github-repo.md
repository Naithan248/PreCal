# Precalculus Complete Guide

Welcome to the Precalculus Complete Guide repository! This resource is designed to provide a comprehensive understanding of precalculus concepts, with special emphasis on trigonometry.

## Repository Structure

```
precalculus-guide/
├── 01-fundamentals/
│   ├── 01-real-numbers.md
│   ├── 02-cartesian-coordinates.md
│   ├── 03-functions-introduction.md
│   ├── 04-function-operations.md
│   ├── 05-function-transformations.md
│   └── examples/
├── 02-polynomial-rational-functions/
│   ├── 01-polynomials.md
│   ├── 02-rational-functions.md
│   ├── 03-partial-fractions.md
│   ├── 04-asymptotes.md
│   └── examples/
├── 03-exponential-logarithmic-functions/
│   ├── 01-exponential-functions.md
│   ├── 02-logarithmic-functions.md
│   ├── 03-solving-exponential-logarithmic-equations.md
│   ├── 04-applications.md
│   └── examples/
├── 04-trigonometry/
│   ├── 01-angle-measure.md
│   ├── 02-unit-circle.md
│   ├── 03-trigonometric-functions.md
│   ├── 04-graphs-of-trig-functions.md
│   ├── 05-inverse-trig-functions.md
│   ├── 06-trigonometric-identities.md
│   ├── 07-solving-trig-equations.md
│   ├── 08-law-of-sines-cosines.md
│   └── examples/
├── 05-analytic-geometry/
│   ├── 01-conics-introduction.md
│   ├── 02-circles.md
│   ├── 03-ellipses.md
│   ├── 04-hyperbolas.md
│   ├── 05-parabolas.md
│   └── examples/
├── 06-vectors-matrices/
│   ├── 01-vectors.md
│   ├── 02-dot-cross-products.md
│   ├── 03-matrices.md
│   ├── 04-matrix-operations.md
│   ├── 05-determinants.md
│   ├── 06-systems-of-equations.md
│   └── examples/
├── 07-sequences-series/
│   ├── 01-sequences.md
│   ├── 02-series.md
│   ├── 03-arithmetic-sequences.md
│   ├── 04-geometric-sequences.md
│   ├── 05-binomial-theorem.md
│   └── examples/
├── 08-introduction-to-calculus/
│   ├── 01-limits.md
│   ├── 02-continuity.md
│   ├── 03-derivative-preview.md
│   ├── 04-applications.md
│   └── examples/
├── resources/
│   ├── cheatsheets/
│   ├── formulas/
│   └── calculators/
├── practice-problems/
│   ├── by-topic/
│   └── comprehensive/
└── README.md
```

## Detailed Content: Trigonometry Section

Let's dive deeper into the trigonometry section, which is a major component of precalculus:

### 04-trigonometry/01-angle-measure.md

```markdown
# Angle Measure

## Degrees vs. Radians
- Degrees: A full circle is 360°
- Radians: A full circle is 2π radians
- Conversion: π radians = 180°
- Formula: radians = (degrees × π) / 180

## Important Angle Measurements
| Degrees | Radians | Radians (simplified) |
|---------|---------|----------------------|
| 0°      | 0       | 0                    |
| 30°     | π/6     | π/6                  |
| 45°     | π/4     | π/4                  |
| 60°     | π/3     | π/3                  |
| 90°     | π/2     | π/2                  |
| 180°    | π       | π                    |
| 270°    | 3π/2    | 3π/2                 |
| 360°    | 2π      | 2π                   |

## Arc Length
The length of an arc is given by:
- s = rθ
  - s = arc length
  - r = radius of circle
  - θ = angle in radians

## Sector Area
The area of a sector is given by:
- A = (1/2)r²θ
  - A = sector area
  - r = radius of circle
  - θ = angle in radians
```

### 04-trigonometry/02-unit-circle.md

```markdown
# The Unit Circle

The unit circle is a circle centered at the origin with a radius of 1 unit. It's a fundamental tool for understanding trigonometric functions.

## Basic Concept
- A unit circle has radius 1 and is centered at the origin (0, 0)
- Any point (x, y) on the unit circle satisfies x² + y² = 1
- For an angle θ in standard position:
  - x-coordinate = cos θ
  - y-coordinate = sin θ

## Unit Circle Coordinates
| Angle (degrees) | Angle (radians) | Coordinates (cos θ, sin θ) |
|-----------------|-----------------|----------------------------|
| 0°              | 0               | (1, 0)                     |
| 30°             | π/6             | (√3/2, 1/2)                |
| 45°             | π/4             | (√2/2, √2/2)               |
| 60°             | π/3             | (1/2, √3/2)                |
| 90°             | π/2             | (0, 1)                     |
| 120°            | 2π/3            | (-1/2, √3/2)               |
| 135°            | 3π/4            | (-√2/2, √2/2)              |
| 150°            | 5π/6            | (-√3/2, 1/2)               |
| 180°            | π               | (-1, 0)                    |
| 210°            | 7π/6            | (-√3/2, -1/2)              |
| 225°            | 5π/4            | (-√2/2, -√2/2)             |
| 240°            | 4π/3            | (-1/2, -√3/2)              |
| 270°            | 3π/2            | (0, -1)                    |
| 300°            | 5π/3            | (1/2, -√3/2)               |
| 315°            | 7π/4            | (√2/2, -√2/2)              |
| 330°            | 11π/6           | (√3/2, -1/2)               |
| 360°            | 2π              | (1, 0)                     |

## Symmetry Properties
- First Quadrant (0° to 90°): All values are positive
- Second Quadrant (90° to 180°): Only sin θ is positive
- Third Quadrant (180° to 270°): Only tan θ is positive
- Fourth Quadrant (270° to 360°): Only cos θ is positive

## Reference Angles
The reference angle is the acute angle (θ') formed by:
- The terminal side of angle θ
- The x-axis (positive or negative)

For any angle θ:
- First quadrant: θ' = θ
- Second quadrant: θ' = π - θ
- Third quadrant: θ' = θ - π
- Fourth quadrant: θ' = 2π - θ
```

### 04-trigonometry/03-trigonometric-functions.md

```markdown
# Trigonometric Functions

## The Six Trigonometric Functions
For an angle θ in standard position with point (x, y) on the terminal ray at distance r from the origin:

| Function | Definition | Unit Circle (r=1) |
|----------|------------|-------------------|
| Sine     | sin θ = y/r | sin θ = y        |
| Cosine   | cos θ = x/r | cos θ = x        |
| Tangent  | tan θ = y/x | tan θ = y/x      |
| Cosecant | csc θ = r/y | csc θ = 1/y      |
| Secant   | sec θ = r/x | sec θ = 1/x      |
| Cotangent| cot θ = x/y | cot θ = x/y      |

## Right Triangle Definitions
For a right triangle with angle θ:

| Function | Definition                      |
|----------|----------------------------------|
| sin θ    | Opposite side / Hypotenuse      |
| cos θ    | Adjacent side / Hypotenuse      |
| tan θ    | Opposite side / Adjacent side   |
| csc θ    | Hypotenuse / Opposite side      |
| sec θ    | Hypotenuse / Adjacent side      |
| cot θ    | Adjacent side / Opposite side   |

## Domains and Ranges

| Function | Domain                          | Range            |
|----------|----------------------------------|------------------|
| sin θ    | All real numbers                | [-1, 1]          |
| cos θ    | All real numbers                | [-1, 1]          |
| tan θ    | All real numbers except θ = π/2 + nπ | All real numbers |
| csc θ    | All real numbers except θ = nπ  | (-∞, -1] ∪ [1, ∞) |
| sec θ    | All real numbers except θ = π/2 + nπ | (-∞, -1] ∪ [1, ∞) |
| cot θ    | All real numbers except θ = nπ  | All real numbers |

## Reciprocal Identities
- csc θ = 1/sin θ
- sec θ = 1/cos θ
- cot θ = 1/tan θ

## Quotient Identities
- tan θ = sin θ/cos θ
- cot θ = cos θ/sin θ

## Pythagorean Identities
- sin²θ + cos²θ = 1
- 1 + tan²θ = sec²θ
- 1 + cot²θ = csc²θ

## Even/Odd Properties
- sin(-θ) = -sin θ (odd function)
- cos(-θ) = cos θ (even function)
- tan(-θ) = -tan θ (odd function)
```

### 04-trigonometry/04-graphs-of-trig-functions.md

```markdown
# Graphs of Trigonometric Functions

## Sine Function
- f(x) = sin x
- Domain: All real numbers
- Range: [-1, 1]
- Period: 2π
- Key points over one period [0, 2π]:
  - (0, 0), (π/2, 1), (π, 0), (3π/2, -1), (2π, 0)

## Cosine Function
- f(x) = cos x
- Domain: All real numbers
- Range: [-1, 1]
- Period: 2π
- Key points over one period [0, 2π]:
  - (0, 1), (π/2, 0), (π, -1), (3π/2, 0), (2π, 1)

## Tangent Function
- f(x) = tan x
- Domain: All real numbers except x = π/2 + nπ
- Range: All real numbers
- Period: π
- Vertical asymptotes at x = π/2 + nπ
- Key points over one period [0, π]:
  - (0, 0), (π/4, 1), (π/2-, ∞), (π/2+, -∞), (3π/4, -1), (π, 0)

## Cosecant Function
- f(x) = csc x
- Domain: All real numbers except x = nπ
- Range: (-∞, -1] ∪ [1, ∞)
- Period: 2π
- Vertical asymptotes at x = nπ

## Secant Function
- f(x) = sec x
- Domain: All real numbers except x = π/2 + nπ
- Range: (-∞, -1] ∪ [1, ∞)
- Period: 2π
- Vertical asymptotes at x = π/2 + nπ

## Cotangent Function
- f(x) = cot x
- Domain: All real numbers except x = nπ
- Range: All real numbers
- Period: π
- Vertical asymptotes at x = nπ

## Transformations of Trigonometric Functions
For a function of the form f(x) = A sin(Bx - C) + D:
- |A| is the amplitude (for sine and cosine only)
- 2π/|B| is the period
- C/B is the phase shift (right if positive, left if negative)
- D is the vertical shift

For a function of the form f(x) = A cos(Bx - C) + D, similar rules apply.

For tangent, cotangent, secant, and cosecant, there is no amplitude, but the other transformations work the same way.
```

### 04-trigonometry/05-inverse-trig-functions.md

```markdown
# Inverse Trigonometric Functions

## Definitions and Notation
- arcsin x = sin⁻¹ x: The angle whose sine is x
- arccos x = cos⁻¹ x: The angle whose cosine is x
- arctan x = tan⁻¹ x: The angle whose tangent is x
- arccsc x = csc⁻¹ x: The angle whose cosecant is x
- arcsec x = sec⁻¹ x: The angle whose secant is x
- arccot x = cot⁻¹ x: The angle whose cotangent is x

## Domains and Ranges
The domains and ranges are restricted to ensure that the inverse functions are well-defined:

| Function  | Domain           | Range               |
|-----------|------------------|--------------------|
| arcsin x  | [-1, 1]          | [-π/2, π/2]        |
| arccos x  | [-1, 1]          | [0, π]             |
| arctan x  | All real numbers | (-π/2, π/2)        |
| arccsc x  | (-∞, -1] ∪ [1, ∞) | [-π/2, 0) ∪ (0, π/2] |
| arcsec x  | (-∞, -1] ∪ [1, ∞) | [0, π/2) ∪ (π/2, π] |
| arccot x  | All real numbers | (0, π)             |

## Key Values
| x     | arcsin x | arccos x | arctan x |
|-------|----------|----------|----------|
| -1    | -π/2     | π        | -π/4     |
| -√3/2 | -π/3     | 5π/6     | -       |
| -√2/2 | -π/4     | 3π/4     | -       |
| -1/2  | -π/6     | 2π/3     | -       |
| 0     | 0        | π/2      | 0        |
| 1/2   | π/6      | π/3      | -       |
| √2/2  | π/4      | π/4      | π/4      |
| √3/2  | π/3      | π/6      | -       |
| 1     | π/2      | 0        | π/4      |

## Inverse Function Relationships
- sin(arcsin x) = x for all x in [-1, 1]
- arcsin(sin θ) = θ for all θ in [-π/2, π/2]
- cos(arccos x) = x for all x in [-1, 1]
- arccos(cos θ) = θ for all θ in [0, π]
- Similar relationships exist for the other trigonometric functions

## Important Identities
- arcsin(-x) = -arcsin x
- arccos(-x) = π - arccos x
- arctan(-x) = -arctan x
- arcsin x + arccos x = π/2
- arctan x + arccot x = π/2
```

### 04-trigonometry/06-trigonometric-identities.md

```markdown
# Trigonometric Identities

## Fundamental Identities
- **Reciprocal Identities:**
  - sin θ = 1/csc θ
  - cos θ = 1/sec θ
  - tan θ = 1/cot θ

- **Quotient Identities:**
  - tan θ = sin θ/cos θ
  - cot θ = cos θ/sin θ

- **Pythagorean Identities:**
  - sin²θ + cos²θ = 1
  - 1 + tan²θ = sec²θ
  - 1 + cot²θ = csc²θ

- **Negative Angle (Even/Odd) Identities:**
  - sin(-θ) = -sin θ
  - cos(-θ) = cos θ
  - tan(-θ) = -tan θ

## Sum and Difference Identities
- **Sine:**
  - sin(α + β) = sin α cos β + cos α sin β
  - sin(α - β) = sin α cos β - cos α sin β

- **Cosine:**
  - cos(α + β) = cos α cos β - sin α sin β
  - cos(α - β) = cos α cos β + sin α sin β

- **Tangent:**
  - tan(α + β) = (tan α + tan β)/(1 - tan α tan β)
  - tan(α - β) = (tan α - tan β)/(1 + tan α tan β)

## Double Angle Identities
- sin(2θ) = 2sin θ cos θ
- cos(2θ) = cos²θ - sin²θ = 2cos²θ - 1 = 1 - 2sin²θ
- tan(2θ) = 2tan θ/(1 - tan²θ)

## Half Angle Identities
- sin²(θ/2) = (1 - cos θ)/2
- cos²(θ/2) = (1 + cos θ)/2
- sin(θ/2) = ±√[(1 - cos θ)/2]
- cos(θ/2) = ±√[(1 + cos θ)/2]
- tan(θ/2) = (1 - cos θ)/sin θ = sin θ/(1 + cos θ) = √[(1 - cos θ)/(1 + cos θ)]

## Product-to-Sum Identities
- sin α sin β = [cos(α - β) - cos(α + β)]/2
- cos α cos β = [cos(α - β) + cos(α + β)]/2
- sin α cos β = [sin(α + β) + sin(α - β)]/2

## Sum-to-Product Identities
- sin α + sin β = 2sin[(α + β)/2]cos[(α - β)/2]
- sin α - sin β = 2cos[(α + β)/2]sin[(α - β)/2]
- cos α + cos β = 2cos[(α + β)/2]cos[(α - β)/2]
- cos α - cos β = -2sin[(α + β)/2]sin[(α - β)/2]

## Power-Reduction Formulas
- sin²θ = (1 - cos 2θ)/2
- cos²θ = (1 + cos 2θ)/2
- tan²θ = (1 - cos 2θ)/(1 + cos 2θ)

## Cofunction Identities
- sin(π/2 - θ) = cos θ
- cos(π/2 - θ) = sin θ
- tan(π/2 - θ) = cot θ
```

### 04-trigonometry/07-solving-trig-equations.md

```markdown
# Solving Trigonometric Equations

## Basic Strategies
1. **Isolate the trigonometric function**
2. **Use trigonometric identities** to simplify the equation
3. **Find the basic solutions** within the principal period
4. **Find the general solution** by adding the appropriate period multiplier

## General Solutions
- sin θ = k has solutions θ = arcsin k + 2nπ and θ = π - arcsin k + 2nπ
- cos θ = k has solutions θ = ±arccos k + 2nπ
- tan θ = k has solutions θ = arctan k + nπ

Where n is an integer.

## Example 1: Solving sin θ = 1/2
1. Basic solution: θ = π/6 or θ = 5π/6
2. General solution: θ = π/6 + 2nπ or θ = 5π/6 + 2nπ

## Example 2: Solving 2sin²θ - sin θ - 1 = 0
1. Use substitution: Let u = sin θ
2. Solve 2u² - u - 1 = 0
3. Apply quadratic formula: u = (1 ± √9)/4 = (1 ± 3)/4
4. Solutions: u = 1 or u = -1/2
5. Therefore: sin θ = 1 or sin θ = -1/2
6. θ = π/2 + 2nπ or θ = 7π/6 + 2nπ or θ = 11π/6 + 2nπ

## Example 3: Solving sin 2θ = cos θ
1. Convert using identity: sin 2θ = 2sin θ cos θ
2. Substitute: 2sin θ cos θ = cos θ
3. Factor: cos θ(2sin θ - 1) = 0
4. Either cos θ = 0 or sin θ = 1/2
5. θ = π/2 + nπ or θ = π/6 + 2nπ or θ = 5π/6 + 2nπ

## Restricted Domains
When solving on a restricted domain [a, b]:
1. Find the general solution
2. Determine which solutions fall within [a, b]

## Using Technology
Graphical methods can be useful:
1. Graph both sides of the equation
2. Find intersection points
3. Use a calculator to find numerical solutions
```

### 04-trigonometry/08-law-of-sines-cosines.md

```markdown
# Law of Sines and Law of Cosines

## Law of Sines
For any triangle with sides a, b, c and opposite angles A, B, C:

$\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}$

Alternatively:
$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$

### Applications of the Law of Sines
1. **Find a missing side** when you know:
   - Two angles and one side (AAS or ASA)
   
2. **Find a missing angle** when you know:
   - Two sides and an angle opposite one of them (SSA)
   
3. **The Ambiguous Case (SSA)**
   - May yield 0, 1, or 2 solutions
   - Occurs when given two sides and an angle opposite one of them

### Area of a Triangle Using Sine
$\text{Area} = \frac{1}{2}ab\sin C = \frac{1}{2}bc\sin A = \frac{1}{2}ac\sin B$

## Law of Cosines
For any triangle with sides a, b, c and opposite angles A, B, C:

$a^2 = b^2 + c^2 - 2bc\cos A$
$b^2 = a^2 + c^2 - 2ac\cos B$
$c^2 = a^2 + b^2 - 2ab\cos C$

Solving for the angles:
$\cos A = \frac{b^2 + c^2 - a^2}{2bc}$
$\cos B = \frac{a^2 + c^2 - b^2}{2ac}$
$\cos C = \frac{a^2 + b^2 - c^2}{2ab}$

### Applications of the Law of Cosines
1. **Find the third side** when you know:
   - Two sides and the included angle (SAS)
   
2. **Find an angle** when you know:
   - All three sides (SSS)

## When to Use Each Law
- **Law of Sines**: Use when you have AAS, ASA, or SSA configurations
- **Law of Cosines**: Use when you have SSS or SAS configurations

## Example: Solving a Triangle
Given:
- a = 8
- b = 12
- C = 60°

Find c and angles A and B.

Solution:
1. Use Law of Cosines to find c:
   $c^2 = a^2 + b^2 - 2ab\cos C$
   $c^2 = 8^2 + 12^2 - 2(8)(12)\cos 60°$
   $c^2 = 64 + 144 - 192(0.5)$
   $c^2 = 208 - 96 = 112$
   $c = \sqrt{112} \approx 10.58$

2. Use Law of Sines to find angle A:
   $\frac{\sin A}{a} = \frac{\sin C}{c}$
   $\sin A = \frac{a\sin C}{c} = \frac{8\sin 60°}{10.58} \approx 0.654$
   $A \approx 40.9°$

3. Find angle B:
   $B = 180° - A - C = 180° - 40.9° - 60° = 79.1°$
```

## Core Trigonometry Concepts

The trigonometry section of this repository covers:

1. **Angle Measurement**
   - Degrees and radians
   - Conversions between units
   - Arc length and sector area

2. **The Unit Circle**
   - Definition and properties
   - Coordinates for special angles
   - Reference angles

3. **Trigonometric Functions**
   - Definitions (sine, cosine, tangent, etc.)
   - Domains and ranges
   - Right triangle relationships

4. **Graphing Trigonometric Functions**
   - Key features of each function
   - Periods, amplitudes, and phase shifts
   - Transformations of trigonometric graphs

5. **Trigonometric Identities**
   - Fundamental identities
   - Sum and difference formulas
   - Double and half-angle formulas
   - Product-to-sum and sum-to-product formulas

6. **Inverse Trigonometric Functions**
   - Definitions and restrictions
   - Domains and ranges
   - Key values and applications

7. **Solving Trigonometric Equations**
   - Basic solution techniques
   - Finding general solutions
   - Solving in restricted domains

8. **Applications in Triangle Trigonometry**
   - Law of Sines
   - Law of Cosines
   - Area formulas using trigonometry

## Additional Resources

The repository includes:

- Interactive calculators for trigonometric functions
- Comprehensive cheat sheets for quick reference
- Practice problems organized by difficulty level
- Detailed solutions for all example problems
- Applied problems showing real-world applications

## Getting Started

To use this repository effectively:
1. Start with the fundamentals section if you need a refresher
2. Focus on the trigonometry section for a deep dive into those topics
3. Work through the practice problems to test your understanding
4. Use the calculators and cheat sheets for quick reference

Each markdown file includes detailed explanations, formulas, examples, and visualizations to help you master the concepts.
