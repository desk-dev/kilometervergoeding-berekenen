while True:
    try:
        zakelijke_kilometers = float(input("Aantal zakelijke kilometers in het afgelopen jaar: "))
        if zakelijke_kilometers < 0:
            raise ValueError("Aantal kilometers kan niet negatief zijn.")
        break
    except ValueError as e:
        print(f"Ongeldige invoer: {e}. Probeer opnieuw.")
kilometervergoeding = 0.23 # vergoeding in 2025

def kilometervergoeding_berekenen(zakelijke_kilometers,kilometervergoeding):
    """ Het berekenen van je gereden zakelijke kilometers met je prive auto van het afgelopen boekjaar"""
    vergoeding = zakelijke_kilometers * kilometervergoeding
    print(f"Je totale zakelijke kilometers: €{zakelijke_kilometers:.2f} ")
    print(f"Je vergoeding die mag meenemen in de kosten van je boekhouding: €{vergoeding:.2f}")

kilometervergoeding_berekenen(zakelijke_kilometers,kilometervergoeding)
    
