from sys import argv

key, input_file, output_file = argv[1], argv[2], argv[3]

file1 = open(input_file)
file2 = open(output_file, "wb")
i = 0
n = len(key)

for line in file1:
    for x in line:
        file2.write((ord(key[i % n]) ^ ord(x)).to_bytes(1, byteorder='big'))
        i += 1

file1.close()
file2.close()
