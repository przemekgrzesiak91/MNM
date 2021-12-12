def count_unique(input):
    unique = {}
    result = 0
    for char in input:
        if char.lower() not in unique:
            unique[char.lower()] = 1
        else:
            unique[char.lower()] += 1

    for keys,values in unique.items():
        if values > 1:
            result += 1
    return(result)

print(count_unique('RabarbArka'))