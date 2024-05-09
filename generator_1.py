def all_variants(t):
    for start in range(len(t)):
        for end in range(start+1, len(t)+1):
            yield t[start:end]

a = all_variants('abc')
for i in a:
    print(i)