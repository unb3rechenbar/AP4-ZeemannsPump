set xlabel 'Nummer des Peaks'
set ylabel 'Spannung U'

set yrange [0.28:1.0]

set datafile separator ","

# Funktion zum Filtern der Datenzeilen
is_valid(line) = (strcol(1) != '#')

p "OptischesPumpen.txt" u 4:2