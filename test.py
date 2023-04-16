
X = "84014298546"  # replace with the desired string of digits

weights = [3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]  # replicate the pattern [3, 1] six times
index = 0
sum = 0
for char in X:
    sum += (int(char) * weights[index])
    index += 1
checksum = (10 - sum % 10) % 10  # calculate the checksum
result = X + str(checksum)
print(checksum)
print(result)