from typing import List

def countBits(n: int) -> List[int]:
    result = [0]
    bitRep = [0]

    for i in range(1, n + 1):
        ones = 0
        carry = 1

        for j, bit in enumerate(bitRep):
            # Figuring out what the current bit must become
            bitRep[j] = (bit + carry) % 2

            # Figuring out what carries over
            carry += bit
            carry = 1 if carry == 2 else 0

            ones += bitRep[j]

        if carry == 1:
            bitRep.append(1)
            ones += 1

        result.append(ones)

    return result


def countBitsOptimized(n: int) -> List[int]:
    result = [0]

    # Creating an array to store locations where there are powers of 2
    locations = []
    powerOfTwo = 1
    for i in range(n + 1):
        if i == powerOfTwo:
            locations.append(1)
            powerOfTwo *= 2
        else:
            locations.append(0)
        i += 1

    lookBack = 1
    for i in range(1, n + 1):
        if locations[i] == 1:
            lookBack *= 2
            result.append(1)
        else:
            result.append(result[i - lookBack] + 1)

    return result


if __name__ == "__main__":
    print(countBits(8))
    print(countBitsOptimized(8))


