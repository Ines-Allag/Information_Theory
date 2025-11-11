import heapq


class Huffman:
    def __init__(self):
        self.codes = {}

    def compress(self, probabilites):
        # Créer les nœuds avec les probabilités
        nodes = []
        for char, prob in probabilites.items():
            nodes.append([prob, [char, ""]])

        nodes.sort(key=lambda x: x[0])

        print("Étapes de construction des codes Huffman:")
        step = 1

        # Fusionner les nœuds
        while len(nodes) > 1:
            lo = nodes.pop(0)
            hi = nodes.pop(0)

            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]

            new_prob = lo[0] + hi[0]
            new_node = [new_prob] + lo[1:] + hi[1:]

            print(f"Étape {step}: {lo[1][0]}({lo[0]}) + {hi[1][0]}({hi[0]}) = {new_prob}")
            step += 1

            nodes.append(new_node)
            nodes.sort(key=lambda x: x[0])

        # Extraire les codes
        self.codes = {char: code for char, code in nodes[0][1:]}

        print("\nCodes Huffman générés:")
        for char, code in sorted(self.codes.items()):
            print(f"  {char}: {code}")

        return self.codes


# Programme principal
if __name__ == "__main__":
    huffman = Huffman()

    # Demander les éléments et leurs probabilités
    probabilites = {}
    n = int(input("Nombre d'éléments dans la source: "))

    print("Entrez les éléments et leurs probabilités:")
    for i in range(n):
        element = input(f"Élément {i + 1}: ")
        proba = float(input(f"Probabilité pour {element}: "))
        probabilites[element] = proba

    print()
    codes = huffman.compress(probabilites)