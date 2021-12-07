from sys import argv

output_file, key,  input_recuperat = argv[1], argv[2], argv[3]

file1 = open(output_file, "rb")
file2 = open(input_recuperat, "w")

i = 0
n = len(key)

while True:
    b = file1.read(1)
    if not b:
        break
    file2.write(chr((int.from_bytes(b, byteorder='big')) ^ (ord(key[i % n]))))
    i += 1


file1.close()
file2.close()
