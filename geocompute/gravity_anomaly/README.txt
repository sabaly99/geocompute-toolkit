

## 🌍 Gravity Anomaly

A **gravity anomaly** is the difference between the **observed gravity** at a point on the Earth’s surface and the **theoretical (normal) gravity** expected at that location.

It helps reveal variations in subsurface mass distribution such as buried structures, density contrasts, ore bodies, or tectonic features.

[
\textbf{Gravity Anomaly} = g_{\text{observed}} - g_{\text{theoretical}}
]

Where:

* ( g_{\text{observed}} ) = measured gravity at a station
* ( g_{\text{theoretical}} ) = normal gravity computed from a reference ellipsoid

The normal gravity is commonly computed using the **International Gravity Formula (IGF)** based on the World Geodetic System 1984:

[
g(\phi) = 9.780327 \left(1 + 0.0053024 \sin^2\phi - 0.0000058 \sin^2 2\phi \right) \ \text{m/s}^2
]

Where:

* ( \phi ) = latitude

---

## 🔎 Types of Gravity Anomalies

### 1️⃣ Free-Air Anomaly

Corrects for elevation above sea level but does not account for mass between the station and sea level.

[
\Delta g_{FA} = g_{\text{obs}} - g_{\text{theoretical}} + 0.3086h
]

Where:

* ( h ) = height above sea level (in meters)
* 0.3086 mGal/m = Free-air correction factor

---

### 2️⃣ Bouguer Anomaly

Corrects for both elevation and the mass of rock between the station and sea level.

[
\Delta g_{B} = g_{\text{obs}} - g_{\text{theoretical}} + 0.3086h - 0.0419\rho h
]

Where:

* ( \rho ) = density of rock (g/cm³)
* 0.0419ρh = Bouguer correction

---

## 📌 Importance of Gravity Anomalies

### 🛰️ 1. Geodesy

* Determines the **geoid**
* Improves orthometric height computation
* Supports GNSS height correction
* Helps refine Earth models

### ⛏️ 2. Geophysical Prospecting

* Detects mineral deposits
* Identifies oil & gas reservoirs
* Maps subsurface cavities
* Locates fault zones

###  3. Tectonic & Structural Studies

* Identifies crustal thickness variations
* Maps sedimentary basins
* Studies plate boundaries

---

## 📖 Summary

Gravity anomalies reveal hidden variations in Earth’s internal structure by comparing measured gravity with theoretical values. They are fundamental in geodesy, mineral exploration, and tectonic analysis.


