def transform(x):
    result = ['','']
    even = 0

    for char in x:
        if even:
            result[0] += char.upper()
            result[1] += char.lower()
            even = 0
        else:
            result[0] += char.lower()
            result[1] += char.upper()
            even = 1
    print(result)

transform('abcdef')