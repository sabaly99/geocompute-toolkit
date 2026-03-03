## 🌍 Gravity Anomaly

In simple terms, a **gravity anomaly** is the difference between the gravity measured at a specific location and the gravity value we expect at that location based on a mathematical Earth model.

Since the Earth is not perfectly uniform in composition or shape, gravity varies slightly from place to place. These small differences give us useful information about subsurface density variations, buried structures, mineral deposits, sedimentary basins, and tectonic features.

### General Expression

Gravity Anomaly = g_observed − g_theoretical

Where:

* g_observed = gravity measured in the field
* g_theoretical = normal gravity computed from a reference ellipsoid

The theoretical gravity is commonly calculated using the International Gravity Formula (IGF) based on the World Geodetic System 1984 (WGS84):

g(φ) = 9.780327 (1 + 0.0053024 sin²φ − 0.0000058 sin²2φ)  m/s²

Where:

* φ = latitude

Gravity changes with latitude because of Earth’s rotation and its slightly flattened (ellipsoidal) shape.

---

## 🔎 Types of Gravity Anomalies

In practice, corrections are applied to observed gravity values before interpretation. The two most common anomalies are:

---

### 1️⃣ Free-Air Anomaly

The Free-Air anomaly corrects for the height of the observation point above sea level but does not account for the mass of rock between the station and sea level.

Δg_FA = g_obs − g_theoretical + 0.3086h

Where:

* h = height above sea level (in meters)
* 0.3086 mGal/m = Free-Air correction factor

This anomaly is useful for studying large-scale features such as mountains and ocean basins because it highlights mass variations without removing terrain mass effects.

---

### 2️⃣ Bouguer Anomaly

The Bouguer anomaly corrects for both elevation and the gravitational effect of the rock mass between the station and sea level.

Δg_B = g_obs − g_theoretical + 0.3086h − 0.0419ρh

Where:

* ρ = average rock density (g/cm³)
* 0.0419ρh = Bouguer slab correction

The Bouguer anomaly is widely used in mineral exploration and crustal structure studies because it isolates deeper density variations more effectively.

---

## 📌 Why Gravity Anomalies Are Important

### 🛰️ Geodesy

* Used in determining the geoid
* Improves orthometric height computation
* Supports GNSS height corrections
* Helps refine Earth reference models

### ⛏️ Geophysical Prospecting

* Detects high-density mineral deposits
* Identifies oil and gas reservoirs
* Maps subsurface cavities
* Locates fault zones

### 🌋 Tectonic & Structural Studies

* Reveals crustal thickness variations
* Maps sedimentary basins
* Studies plate boundaries and large geological structures

---

## 📖 Summary

Gravity anomalies represent the difference between measured and theoretical gravity values. By analyzing these differences, we can detect hidden variations in Earth’s internal structure. They play a key role in geodesy, resource exploration, and tectonic research.
