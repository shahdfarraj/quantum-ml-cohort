# Personal practice: classical logic gates
# These are simple Python implementations based on the Chapter 1 topics
# introduced in the Quantum ML Cohort.

def AND(a, b):
    return a and b


def OR(a, b):
    return a or b


def NOT(a):
    return not a


def XOR(a, b):
    return a != b


if __name__ == "__main__":
    values = [False, True]

    print("AND")
    for a in values:
        for b in values:
            print(a, b, "->", AND(a, b))

    print("\nOR")
    for a in values:
        for b in values:
            print(a, b, "->", OR(a, b))

    print("\nNOT")
    for a in values:
        print(a, "->", NOT(a))

    print("\nXOR")
    for a in values:
        for b in values:
            print(a, b, "->", XOR(a, b))
