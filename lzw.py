class LZW:
    def __init__(self):
        self.base_dict = {chr(i): i for i in range(256)}

    def compress(self, text):
        dictionary = self.base_dict.copy()
        dict_size = 256
        w = ""
        result = []

        print("\nCompression LZW:")
        print("Étape | Séquence | Caractère | Code")
        print("-" * 40)

        step = 1
        for c in text:
            wc = w + c
            if wc in dictionary:
                w = wc
                print(f"{step:5d} | {w:8} | {c:9} | -")
            else:
                dictionary[wc] = dict_size
                dict_size += 1
                result.append(dictionary[w])
                print(f"{step:5d} | {w:8} | {c:9} | {dictionary[w]:4}")
                w = c
            step += 1

        if w:
            result.append(dictionary[w])
            print(f"{step:5d} | {w:8} | FIN     | {dictionary[w]:4}")

        return result

    def decompress(self, compressed):
        dictionary = {i: chr(i) for i in range(256)}
        dict_size = 256
        w = chr(compressed[0])
        result = w

        print("\nDécompression LZW:")
        print("Étape | Code | Séquence")
        print("-" * 25)
        print(f"{1:5d} | {compressed[0]:4} | {w:8}")

        step = 2
        for k in compressed[1:]:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[0]
            else:
                raise ValueError("Code invalide")

            result += entry
            dictionary[dict_size] = w + entry[0]
            dict_size += 1
            print(f"{step:5d} | {k:4} | {entry:8}")
            w = entry
            step += 1

        return result


# Programme principal
if __name__ == "__main__":
    lzw = LZW()

    texte = input("Entrez la chaîne à compresser: ")

    compressed = lzw.compress(texte)
    print(f"\nCodes compressés: {compressed}")

    decompressed = lzw.decompress(compressed)
    print(f"\nTexte décompressé: '{decompressed}'")
    print(f"Vérification: {'✓ OK' if texte == decompressed else '✗ ERREUR'}")