# ----------------------------------------------------------------------
# C1. Python — rīks, kas atlasa un saglabā
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram līmeni padod kā argumentu komandrindā. Skripts izvada, cik tāda līmeņa rindu žurnālā ir, un saglabā visas šīs rindas failā, kura nosaukums sākas ar līmeņa nosaukumu.
# Ja arguments nav padots, skripts izvada pamācību un neavarē.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                            Mainīgo, kurā glabā līmeni, nosauc ar vārdu meklejamais.

import csv
import sys

if len(sys.argv) < 2:
    sys.exit("python F1_uzraksti.py <līmenis>")

meklejamais = str(sys.argv[1])
rindas_limenis = []

for rinda in open("sistema.log", encoding="utf-8"):
    if meklejamais in rinda:
        rindas_limenis.append(rinda)

print("Skaits:", len(rindas_limenis))
for rinda in rindas_limenis:
    
    with open("WARNING.csv", "w", newline="",
        encoding="utf-8-sig") as f:
        r = csv.writer(f, delimiter=";")
        for meklejamais in rindas_limenis:
            r.writerow([meklejamais])