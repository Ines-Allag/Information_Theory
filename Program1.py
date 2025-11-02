import math


def single_source_analysis():
    print("=== PROGRAMME 1: SOURCE UNIQUE ===")

   #Symbols + their probas
    n = int(input("Nombre de symboles: "))
    symbols = []
    probas = []

    for i in range(n):
        s = input(f"Symbole {i + 1}: ")
        p = float(input(f"Probabilité p({s}): "))
        symbols.append(s)
        probas.append(p)

    # Normalize if needed
    total = sum(probas)
    if abs(total - 1.0) > 0.001:
        print(f"Normalisation: somme = {total}")
        probas = [p / total for p in probas]

    # information quantity for each element
    information = []
    for i in range(n):
        if probas[i] > 0:
            I = math.log2(1 / probas[i])
            information.append(I)
        else:
            information.append(0)

    # entropy
    entropy = 0
    for i in range(n):
        if probas[i] > 0:
            entropy += probas[i] * information[i]

    # results
    print("\n=== RÉSULTATS ===")
    print(f"{'Symbole':<10} {'Probabilité':<12} {'I(x) bits':<12}")
    print("-" * 40)

    for i in range(n):
        print(f"{symbols[i]:<10} {probas[i]:<12.4f} {information[i]:<12.4f}")

    print(f"\nEntropie H(X) = {entropy:.4f} bits/symbole")

single_source_analysis()