from header.APbrainLite import *


# ---ALLGEMEINE DATEN---
c0 = 299792458


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
