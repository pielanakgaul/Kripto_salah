s = []
for x in range(256):
    s.append(x)

input_key = 'saputra1'
k = bytearray(input_key, "utf8")

j = 0
for i in range(len(k)):
    j = (j + s[i] + k[i % len(input_key)]) % 256
    c = s[i]
    s[j] = c
    s[i] = j

print(s)
