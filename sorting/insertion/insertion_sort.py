
def insert(sorted, value):
    position = 0

    while position < len(sorted) and value > sorted[position]:
        position += 1

    while position < len(sorted):
        temp = sorted[position]
        sorted[position] = value
        value = temp
        position += 1
    sorted.append(value)


def insertion_sort(array_input):
    sorted = [array_input[0]]

    for i in range(1, len(array_input)):
        insert(sorted, array_input[i])

    return sorted


if __name__ == "__main__":
    array_input = [2,3,5,7,13,11]
    print(insertion_sort(array_input))
