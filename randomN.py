import random

def sortear_mega_sena():
    numeros_sorteados = random.sample(range(1, 61), 6)
    numeros_sorteados.sort()
    return numeros_sorteados


if __name__ == "__main__":
    numeros_sorteados = sortear_mega_sena()
    print("Números sorteados para a mega sena:\n" + str(numeros_sorteados))
  