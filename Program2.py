import math


def two_sources_analysis():
    print("=== PROGRAMME 2: DEUX SOURCES ===")

    # Source X
    nX = int(input("Nombre de symboles source X: "))
    symbolsX = []
    for i in range(nX):
        symbolsX.append(input(f"Symbole X{i + 1}: "))

    # Source Y
    nY = int(input("Nombre de symboles source Y: "))
    symbolsY = []
    for i in range(nY):
        symbolsY.append(input(f"Symbole Y{i + 1}: "))

    # Joint probabilities
    print("\nProbabilités conjointes p(x,y):")
    joint_prob = []
    for i in range(nX):
        row = []
        for j in range(nY):
            p = float(input(f"p({symbolsX[i]},{symbolsY[j]}): "))
            row.append(p)
        joint_prob.append(row)

    # Normalize
    total = sum(sum(row) for row in joint_prob)
    if abs(total - 1.0) > 0.001:
        print(f"Normalisation: somme = {total}")
        joint_prob = [[p / total for p in row] for row in joint_prob]

    # Calculate marginals
    marginal_X = [sum(row) for row in joint_prob]
    marginal_Y = [sum(joint_prob[i][j] for i in range(nX)) for j in range(nY)]

    # JOINT ENTROPY
    H_XY = 0
    for i in range(nX):
        for j in range(nY):
            if joint_prob[i][j] > 0:
                H_XY += joint_prob[i][j] * math.log2(1 / joint_prob[i][j])

    # AVERAGE CONDITIONAL ENTROPY
    H_XgivenY = 0
    for j in range(nY):
        if marginal_Y[j] > 0:
            for i in range(nX):
                if joint_prob[i][j] > 0:
                    p_x_given_y = joint_prob[i][j] / marginal_Y[j]
                    H_XgivenY += joint_prob[i][j] * math.log2(1 / p_x_given_y)

    # MUTUAL INFORMATION
    H_X = sum(-p * math.log2(p) for p in marginal_X if p > 0)
    H_Y = sum(-p * math.log2(p) for p in marginal_Y if p > 0)
    I_XY = H_X + H_Y - H_XY

    # Display results
    print("\n=== RÉSULTATS ===")
    print(f"1. Entropie conjointe H(X,Y) = {H_XY:.4f} bits")
    print(f"2. Entropie conditionnelle moyenne H(X|Y) = {H_XgivenY:.4f} bits")
    print(f"3. Quantité d'information mutuelle I(X;Y) = {I_XY:.4f} bits")

two_sources_analysis()