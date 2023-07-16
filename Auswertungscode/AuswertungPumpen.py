import numpy as np
from header.APbrainLite import *
from header.Messwerte import *


# Schritt 1: Spannungen in Magnetfeld umrechnen
def BerechneHelmholtzMagnetfeld(Spannung):
    Strom = Spannung / Widerstand

    return 8 / np.sqrt(125) * MagnetischeFeldkonstante * HelmholtzWindungen * Strom / HelmholtzRadius


PumpenNullfeld = BerechneHelmholtzMagnetfeld(PumpenNullspannung)
PumpenBFeldMinima1 = np.array([BerechneHelmholtzMagnetfeld(U) for U in PumpenSpannungMinima1])
PumpenBFeldMinima2 = np.array([BerechneHelmholtzMagnetfeld(U) for U in PumpenSpannungMinima2])

print("Null B-Feld: ", PumpenNullfeld)
print(ErstelleTabelle(["Stromminimum 1", "", "Stromminimum 2", ""],
                      [[i1, b1*10**6, i2, b2*10**6] for i1, b1, i2, b2 in zip(PumpenSpannungMinima1, PumpenBFeldMinima1, PumpenSpannungMinima2, PumpenBFeldMinima2)],
                      Unterschrift="Spannungswerte und Magnetfelder bei Strominima", Label="PumpenMessdaten"))


# Schritt 2: Null B-Feld abziehen von Messdaten
PumpenBFeldMinima1 -= PumpenNullfeld
PumpenBFeldMinima2 -= PumpenNullfeld


# Schritt 3: Linearer Fit mit PumpenFrequenzen als x-Werte und PumpenBFeldMinima1/2 als y-Werte
def lineareFunktion(x, m, n):
    return m * x + n


Steigung1, Achsenabschnitt1 = BestimmeFitParameter(PumpenFrequenzen, PumpenBFeldMinima1, lineareFunktion)
Steigung2, Achsenabschnitt2 = BestimmeFitParameter(PumpenFrequenzen, PumpenBFeldMinima2, lineareFunktion)

StandardPGFPlot([PumpenFrequenzen, PumpenFrequenzen], [PumpenBFeldMinima1, PumpenBFeldMinima2], LinRegSetting=[1,1],
                AxisLabels=["Frequenz der Wechselspannung", "Magnetfeld bei Stromminima"],
                Caption="Magnetfeldkurven zur Bestimmung der Landé-Faktoren von $^85$Rb und $^87$Rb",
                FigLabel="PumpenMagnetkurven", AxisUnits=["Hz", "T"])

print("Fit-Ergebnisse: je (m,n): ", Steigung1, Achsenabschnitt1, " und ", Steigung2, Achsenabschnitt2)

# Schritt 4: berechne Landé-Faktoren aus Steigungen
LandeFaktorF1 = h / (MagnetonBohr * Steigung1)
LandeFaktorF2 = h / (MagnetonBohr * Steigung2)

print("LandeFaktoren: ", LandeFaktorF1, LandeFaktorF2)


# Schritt 5: berechne Kernspinquantenzahl I

Kernspin1 = 1 / LandeFaktorF1 - 1/2
Kernspin2 = 1 / LandeFaktorF2 - 1/2

print("Kerspinzahlen: ", Kernspin1, Kernspin2)