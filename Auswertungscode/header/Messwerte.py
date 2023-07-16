from header.APbrainLite import *


# ---ALLGEMEINE DATEN---
c0 = 299792458
h = 6.62607015 * 10**-34
MagnetonBohr = 9.2740100783 * 10**-24
MagnetischeFeldkonstante = 1.25663706212 * 10**-6


# ---ZEEMAN---
# Daten: fürs Setup
a = WerttupelL(4*10**-3,0)  # IN m
n = WerttupelL(1.4567, 0)
Wellenlaenge = WerttupelL(643.8*10**-9,0)   # IN m
WinkelAufspaltungTransversal = 1 / 3    # ???
WinkelAufspaltungLongitudinal = 1 / 4   # ???


# Daten: transversales Magnetfeld (IN T)
ZeemanMagnetfelderTransversal = [WerttupelL(0.6, 0.01),
                                 WerttupelL(0.56, 0.01),
                                 WerttupelL(0.57, 0.01),
                                 WerttupelL(0.57, 0.01),
                                 WerttupelL(0.58, 0.01)
                                ]
ZeemanMagnetfeldTransversal = Mittelwert(ZeemanMagnetfelderTransversal)

# Daten: longitudinales Magnetfeld (IN T)
ZeemanMagnetfelderLongitudinal = [WerttupelL(0.457, 0.01),
                                 WerttupelL(0.480, 0.01),
                                 WerttupelL(0.497, 0.01),
                                 WerttupelL(0.468, 0.01),
                                 WerttupelL(0.460, 0.01)
                                ]
ZeemanMagnetfeldLongitudinal = Mittelwert(ZeemanMagnetfelderLongitudinal)


# ---OPTISCHES PUMPEN---
# Daten: fürs Setup
HelmholtzRadius = WerttupelL(0.1639, 0) # (IN m)
HelmholtzWindungen = 11
Widerstand = WerttupelL(1, 0)    # (IN Ohm)


# Daten: Spannung für das Nullmagnetfeld der Erde (IN V)
PumpenNullspannungMessungen = [WerttupelL(0.0843, 0.005),
                           WerttupelL(0.0664, 0.005),
                           WerttupelL(0.0711, 0.005),
                           WerttupelL(0.0669, 0.005),
                           WerttupelL(0.0700, 0.005),
                           WerttupelL(0.0703, 0.005),
                           WerttupelL(0.0679, 0.005),
                           WerttupelL(0.0688, 0.005),
                           WerttupelL(0.0679, 0.005),
                           WerttupelL(0.0677, 0.005),
                           WerttupelL(0.0677, 0.005)]
PumpenNullspannung = Mittelwert(PumpenNullspannungMessungen)

# Daten: Frequenzen, bei denen alle Magnetfelder je gemessen wurden (IN Hz)
PumpenFrequenzen = [WerttupelL((100 + i) * 10**3,0) for i in range(0, 110, 10)]

# Daten: Spannung zum 1. Stromminimum (IN V)
PumpenSpannungMinima1 = np.array([WerttupelL(0.2983, 0.005),
                      WerttupelL(0.3197, 0.005),
                      WerttupelL(0.3465, 0.005),
                      WerttupelL(0.3704, 0.005),
                      WerttupelL(0.3931, 0.005),
                      WerttupelL(0.4169, 0.005),
                      WerttupelL(0.4396, 0.005),
                      WerttupelL(0.4610, 0.005),
                      WerttupelL(0.4859, 0.005),
                      WerttupelL(0.5088, 0.005),
                      WerttupelL(0.5330, 0.005)])

# Daten: Spannung zum 2. Stromminimum (IN V)
PumpenSpannungMinima2 = np.array([WerttupelL(0.5339, 0.005),
                      WerttupelL(0.5759, 0.005),
                      WerttupelL(0.6252, 0.005),
                      WerttupelL(0.6721, 0.005),
                      WerttupelL(0.7173, 0.005),
                      WerttupelL(0.7643, 0.005),
                      WerttupelL(0.8107, 0.005),
                      WerttupelL(0.8569, 0.005),
                      WerttupelL(0.9016, 0.005),
                      WerttupelL(0.9503, 0.005),
                      WerttupelL(0.9963, 0.005)])
