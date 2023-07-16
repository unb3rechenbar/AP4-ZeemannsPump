#   APbrain lite für Emergencies
import numpy as np
from scipy.optimize import curve_fit
import scipy.special


class WerttupelL:
    def __init__(self, Wert, Unsicherheit):
        self.Wert = Wert
        self.Unsicherheit = Unsicherheit

    def __add__(self, other):
        NeuerWert = self.Wert + other.Wert
        NeueUnsicherheit =  np.sqrt(self.Unsicherheit**2 + other.Unsicherheit**2)
        return WerttupelL(NeuerWert, NeueUnsicherheit)

    def __sub__(self, other):
        if type(other) is WerttupelL:
            NeuerWert = self.Wert - other.Wert
            NeueUnsicherheit = np.sqrt(self.Unsicherheit ** 2 + other.Unsicherheit ** 2)

        else:
            NeuerWert = self.Wert - other
            NeueUnsicherheit = self.Unsicherheit

        return WerttupelL(NeuerWert, NeueUnsicherheit)

    def __rsub__(self, other):
        if type(other) is WerttupelL:
            NeuerWert = other.Wert - self.Wert
            NeueUnsicherheit = np.sqrt(self.Unsicherheit ** 2 + other.Unsicherheit ** 2)

        else:
            NeuerWert = other - self.Wert
            NeueUnsicherheit = self.Unsicherheit

        return WerttupelL(NeuerWert, NeueUnsicherheit)

    def __neg__(self):
        return WerttupelL(-self.Wert, self.Unsicherheit)

    def __abs__(self):
        NeuerWert = abs(self.Wert)
        NeueUnsicherheit = self.Unsicherheit

        return WerttupelL(NeuerWert, NeueUnsicherheit)

    def __truediv__(self, other):
        if type(other) is WerttupelL:
            NeuerWert = self.Wert / other.Wert
            NeueUnsicherheit = np.sqrt((self.Unsicherheit / other.Wert)**2 + (other.Unsicherheit * self.Wert / other.Wert**2)**2)

        else:
            NeuerWert = self.Wert / other
            NeueUnsicherheit = self.Unsicherheit / other

        return WerttupelL(NeuerWert, NeueUnsicherheit)

    def __rtruediv__(self, other):
        if type(other) is WerttupelL:
            NeuerWert = other.Wert / self.Wert
            NeueUnsicherheit = np.sqrt((other.Unsicherheit / self.Wert) ** 2 + (self.Unsicherheit * other.Wert / self.Wert ** 2) ** 2)

        else:
            NeuerWert = other / self.Wert
            NeueUnsicherheit = abs(other / self.Wert**2) * self.Unsicherheit

        return WerttupelL(NeuerWert, NeueUnsicherheit)

    def __pow__(self, power, modulo=None):
        NeuerWert = self.Wert ** power
        NeuUnsicherheit = abs(power * self.Wert**(power - 1)) * self.Unsicherheit

        return WerttupelL(NeuerWert, NeuUnsicherheit)

    def __mul__(self, other):
        if type(other) is WerttupelL:
            NeuerWert = self.Wert * other.Wert
            NeueUnsicherheit = np.sqrt((self.Unsicherheit * other.Wert)**2 + (other.Unsicherheit * self.Wert)**2)

        else:
            NeuerWert = self.Wert * other
            NeueUnsicherheit = self.Unsicherheit * other

        return WerttupelL(NeuerWert, NeueUnsicherheit)

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        Wert, Unsicherheit = self.Wert, self.Unsicherheit

        if Unsicherheit >= 1:
            UnsicherheitStellen = int(round(Unsicherheit + 0.5))

            if len(str(UnsicherheitStellen)) == 1:
                WertGerundet = round(Wert, 1)
                UnsicherheitStellen = int(round(10 * Unsicherheit + 0.5))
            else:
                UnsicherheitStellen = int(round(Unsicherheit + 0.5))
                WertGerundet = int(round(Wert))
            return "%s(%s)" % (WertGerundet, UnsicherheitStellen)

        elif Unsicherheit == 0:
            return str(Wert)

        else:
            # bestimme erste Zifferstelle, die nicht Null ist
            Unsicherheit = "%e" % Unsicherheit
            if "-" in Unsicherheit:
                UnsicherheitStelle = int(Unsicherheit.split("-")[1])
            else:
                UnsicherheitStelle = int(Unsicherheit.split("+")[1])
            UnsicherheitStellen = round(int(Unsicherheit.split("-")[0].replace(".","")[0:2])+5,-1)

            # Werteausgabe
            WertGerundet = str(round(Wert, UnsicherheitStelle + 1))
            if len(WertGerundet) == UnsicherheitStelle + 2:  # tritt auf, wenn WertGerundet eigentlich eine Null als letzte Ziffer haben sollte
                WertGerundet += "0"
            return "%s(%s)" % (WertGerundet, UnsicherheitStellen)

    def __repr__(self):
        return str(self)

    def __float__(self):
        return self.Wert

    def __gt__(self, other):
        if self.Wert > other.Wert:
            return True
        else:
            return False


# komplexe Funktionen für Werttupel
def GradZuBogenmass(Grad):
    return Grad / 360 * 2 * np.pi


# Fitfunktion
def BestimmeFitParameter(xDaten, yDaten, Fitfunktion, WerteGeraten=[]):
    xDatenWerte = [x.Wert for x in xDaten]
    yDatenWerte = [y.Wert for y in yDaten]

    if len(WerteGeraten) > 0:
        Parameter, Kovarianzen = curve_fit(Fitfunktion, xDatenWerte, yDatenWerte, p0=WerteGeraten)
    else:
        Parameter, Kovarianzen = curve_fit(Fitfunktion, xDatenWerte, yDatenWerte)
    Abweichung = np.sqrt(np.diag(Kovarianzen))

    ParameterWerttupel = [WerttupelL(P, A) for P, A in zip(Parameter, Abweichung)]
    return ParameterWerttupel


# Komplexe mathematischen Funktionen
def sin(W):
    AlterWert = GradZuBogenmass(W.Wert)
    AlteUnsicherheit = GradZuBogenmass(W.Unsicherheit)

    NeuerWert = np.sin(AlterWert)
    NeueUnsicherheit = abs(np.cos(AlterWert)) * AlteUnsicherheit

    return WerttupelL(NeuerWert, NeueUnsicherheit)


def wurzel(W):
    NeuerWert = np.sqrt(W.Wert)
    NeueUnsicherheit = 1 / (2 * np.sqrt(W.Wert)) * W.Unsicherheit

    return WerttupelL(NeuerWert, NeueUnsicherheit)


def Fehlerfunktion(W):
    NeuerWert = scipy.special.erf(W.Wert)
    NeueUnsicherheit = 2 / np.sqrt(np.pi) * np.exp(-W.Wert**2) * W.Unsicherheit

    return WerttupelL(NeuerWert, NeueUnsicherheit)


# Newton-Verfahren
# liefert momentan leider noch zu große Unsicherheiten :(
def Newton(Startwert, Funktion, Ableitung, *Funktionsparameter, Iterationen=10):
    Wert = Startwert

    for _ in range(Iterationen):
        Wert = Wert - Funktion(Wert, *Funktionsparameter) / Ableitung(Wert, *Funktionsparameter)

    return Wert

# statistische Funktionen


def Mittelwert(Messwerte):
    Summe = WerttupelL(0, 0)
    for Messwert in Messwerte:
        Summe += Messwert
    return Summe / len(Messwerte)


def Signifikanztest(W1, W2):
    Differenz = abs(W1.Wert - W2.Wert)
    KombinierteUnsicherheit = (W1 + W2).Unsicherheit

    return round((1 - scipy.special.erf(Differenz / KombinierteUnsicherheit)) * 100, 2)


# Tabellenerstellung
def ErstelleTabelle(Ueberschriften, Datenreihen, Unterschrift="eine Tabelle", Label="tab:mylabel"):
    Tabelle = "\\begin{table}[H]\n\t\\centering"
    Tabelle += "\n\t\\begin{tabular}{%s}\n\t\t" % "|".join("l" for _ in Ueberschriften)

    for Titel in Ueberschriften:
        Tabelle += "\\textbf{%s} & " % Titel
    Tabelle = Tabelle[:-3]

    for Reihe in Datenreihen:
        Tabelle += "\\\\\n\t\t\\hline\n\t\t"
        for Eintrag in Reihe:
            Tabelle += str(Eintrag) + " & "
        Tabelle = Tabelle[:-3]

    Tabelle += "\n\t\\end{tabular}\n\t\\caption{%s}\n\t" % Unterschrift
    Tabelle += "\\label{%s}\n" % Label
    Tabelle += "\\end{table}"
    return Tabelle


# pgfplots das Biest

# X, Y, Xerror, Yerror: Listen von Datenreihen, d.h. X=[X-Werte Datenreihe 1, X-Werte Datenreihe 2,...]
# LingRegSettings: Liste von Booleans: wenn i-ter Eintrag True ist, wird lineare Regression mit i-ten Datensatz gemachtn
# RegSettings: für nichtlineare Regression, Liste mit Optionen-Dictionaries oder 'None': z.B [Reg1, Reg2, None, Reg4,...]
# Struktur von Regj: {"Funktion": String der Funktion mit eingesetzten Parametern, "Domain": [x0,x1] mit [x0,x1]
# geplottetes Intervall}, "Label": Name der Regressionskurve
# AxisUnits: Einheiten der x- und y-Achse
def StandardPGFPlot(X, Y, LinRegSetting=[], RegSettings=[],
                    DatenLabels=[], AxisLabels=["x-Achse", "y-Achse"], Caption="ein wunderbarer Plot",
                    FigLabel="fig:wunderbarerplot", FigTyp=0, PlotWidth="10cm", AxisUnits=[None, None]):
    colors = ["red", "blue", "green", "yellow", "orange", "brown", "pink"]

    Xerror, Yerror = [[x.Unsicherheit for x in Xe] for Xe in X], [[y.Unsicherheit for y in Ye] for Ye in Y]
    X, Y = [[x.Wert for x in Xe] for Xe in X], [[y.Wert for y in Ye] for Ye in Y]

    # erstellt Tabelle mit Daten
    def Tabellenblock(x, y, xerror, yerror):
        print("\t\t\tX\tY\txerror\tyerror\t\\\\")
        for i in range(0, len(x)):
            print("\t\t\t", x[i], "\t", y[i], "\t", xerror[i], "\t", yerror[i], "\t\\\\")

    if FigTyp == 0:
        print("\\begin{figure}[H]\n")
    elif FigTyp == 1:
        print("\\begin{subfigure}[b]{0.4\\textwidth}\n")
    else:
        print("Fehlerhafte Konfigurationsanweisung!")
        exit()
    print(
        "\t\\centering\n\t\\begin{tikzpicture}\n\t\t\\pgfplotsset{width=" + PlotWidth + ",compat=1.3,legend style={font=\\footnotesize}}\n\t\t\\begin{axis}[xlabel={" +
        AxisLabels[0] + "},ylabel={" + AxisLabels[1] + "},legend cell align=left,legend pos=north west]\n\t\t")

    # plottet alle Datenreihen
    for i in range(len(X)):
        print("\t\t\\addplot+[only marks,color=" + colors[i % len(
            colors)] + ",mark=square,error bars/.cd,x dir=both,x explicit,y dir=both,y explicit,error bar style={color=black}] table[x=X,y=Y,x error=xerror,y error=yerror,row sep=\\\\]{")
        Tabellenblock(X[i], Y[i], Xerror[i], Yerror[i])
        print("\t\t};")

        # Datensatz benennen
        try:
            print("\t\t\\addlegendentry{%s}\n" % DatenLabels[i])
        except IndexError:
            print("\t\t\\addlegendentry{Messpunkte Datensatz " + str(i) + "}\n")

        # führt ggf. lineare Regression mit Datensatz i durch
        if len(LinRegSetting) >= i+1:
            if LinRegSetting[i] == 1:
                print("\t\t\\addplot[] table[row sep=\\\\,y={create col/linear regression={y=Y}}]{")
                Tabellenblock(X[i], Y[i], Xerror[i], Yerror[i])
                print("\t\t};")

                # Einheiten von Steigung und y-Achsenabschnitt bestimmen
                AchsenabschnittUnit, SteigungUnit = "", ""
                if AxisUnits[0] is None and AxisUnits[1] is not None:
                    AchsenabschnittUnit = "\\si{" + AxisUnits[1] + "}"
                    SteigungUnit = "\\si{" + AxisUnits[1] + "}"
                elif AxisUnits[0] is not None and AxisUnits[1] is None:
                    SteigungUnit = "\\si{\\per " + AxisUnits[0] + "}"
                elif AxisUnits[0] is not None and AxisUnits[1] is not None:
                    AchsenabschnittUnit = "\\si{" + AxisUnits[1] + "}"
                    SteigungUnit = "\\si{" + AxisUnits[1] + "\\per " + AxisUnits[0] + "}"

                print(
                    "\t\t\\addlegendentry{%\n\t\t\t$\pgfmathprintnumber{\pgfplotstableregressiona}\\," + SteigungUnit +
                    "\cdot x\pgfmathprintnumber[print sign]{\pgfplotstableregressionb}\\," + AchsenabschnittUnit + "$ lin. Regression} %")

        # führt ansonsten ggf. nichtlineare Regression durch
        elif len(RegSettings) >= i+1:
            if RegSettings[i] is not None:
                Regression = RegSettings[i]
                x0, x1 = Regression["Domain"]
                print("\t\t\\addplot[domain=" + str(x0) + ":" + str(x1) + "] " + "{%s};" % Regression["Funktion"])
                print("\t\t\\addlegendentry{%s}\n" % Regression["Label"])

    print("\t\t\\end{axis}\n\t\t\\end{tikzpicture}")
    print("\t\\caption{" + Caption + "}\n\t\\label{fig:" + FigLabel + "}")

    if FigTyp == 0:
        print("\\end{figure}")
    elif FigTyp == 1:
        print("\\end{subfigure}")
    else:
        print("Fehlerhafte Konfigurationsanweisung!")
        exit()


# Daten einlesen
def DatenEinlesen(Pfad, ZeilenCutoff=1, Spaltensep=" ", Spaltenzahl=2):
    Spalten = [[] for _ in range(Spaltenzahl)]

    with open(Pfad) as f:
        Zeilen = f.readlines()[ZeilenCutoff:]

        for Zeile in Zeilen:
            SpaltenEintraege = Zeile.split(Spaltensep)
            for i, Spalte in enumerate(Spalten):
                Spalte.append(float(SpaltenEintraege[i]))

    return Spalten