import numpy as np
from header.APbrainLite import *
from header.Messwerte import *

print(ZeemanMagnetfeldTransversal, ZeemanMagnetfeldLongitudinal)

# Schritt 1: berechne Wellenlängendifferenz zwischen aufgespaltenen Spektrallinien über 6.4.2
def BerechneWellenlaengeDifferenz(WinkelAufspaltung):
    return Wellenlaenge ** 2 / (2 * a * n) * WinkelAufspaltung

WellenlaengeDifferenzTransversal = BerechneWellenlaengeDifferenz(WinkelAufspaltungTransversal)
WellenlaengeDifferenzLongitudinal = BerechneWellenlaengeDifferenz(WinkelAufspaltungLongitudinal)


# Schritt 2: berechne Frequenzdifferenzen über f = c0 / lambda und eine Taylor-Entwicklung bis zum ersten Term
def BerechneFrequenzDifferenz(WellenlaengeDifferenz):
    return c0 / Wellenlaenge**2 * WellenlaengeDifferenz

FrequenzdifferenzTransversal = BerechneFrequenzDifferenz(WellenlaengeDifferenzTransversal)
FrequenzdifferenzLongitudinal = BerechneFrequenzDifferenz(WellenlaengeDifferenzLongitudinal)


# Schritt 3: berechne Elementarladung über 6.4.1
def BerechneSpezElementarladung(Frequenzdifferenz, Magnetfeld):
    return 4 * np.pi * Frequenzdifferenz / Magnetfeld

SpezElementarladungTransversal = BerechneSpezElementarladung(FrequenzdifferenzTransversal, ZeemanMagnetfeldTransversal)
SpezElementarladungLongitudinal = BerechneSpezElementarladung(FrequenzdifferenzLongitudinal, ZeemanMagnetfeldLongitudinal)


# Schritt 4: Signifikanztests mit Literaturwert und Werten aus AP-2-Versuch "Fadenstrahlrohr
SpezElementarladungLiteratur = WerttupelL(1.75882001076 * 10**11, 0)
SpezElementarladungFadenstrahl = WerttupelL(2.06043 * 10**11, 3819027359)

VereinbarkeitTransversalLiteratur = Signifikanztest(SpezElementarladungTransversal, SpezElementarladungLiteratur)
VereinbarkeitLongitudinalLiteratur = Signifikanztest(SpezElementarladungLongitudinal, SpezElementarladungLiteratur)

VereinbarkeitTransversalFadenstrahl = Signifikanztest(SpezElementarladungTransversal, SpezElementarladungFadenstrahl)
VereinbarkeitLongitudinalFadenstrahl = Signifikanztest(SpezElementarladungLongitudinal, SpezElementarladungFadenstrahl)

# gut is sowieso kein Wert mit einen anderen vereinbar
print(ErstelleTabelle(["", "spezifische Ladung", r"Vereinbarkaeit mit $e/m_{Lit}$", r"Vereinbarkaeit mit $e/m_{Fad}$"],
                      [["transversal", SpezElementarladungTransversal, VereinbarkeitTransversalLiteratur, VereinbarkeitTransversalFadenstrahl],
                       ["longitudinal", SpezElementarladungLongitudinal, VereinbarkeitLongitudinalLiteratur, VereinbarkeitLongitudinalFadenstrahl]]))