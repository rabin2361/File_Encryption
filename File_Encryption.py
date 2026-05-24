# Open file and read content
file = open("message.txt", "r")
data = file.read()
file.close()

# Encrypt the data
encrypted_text = ""

for letter in data:
    encrypted_text += chr(ord(letter) + 3)

# Save encrypted data
file = open("encrypted.txt", "w")
file.write(encrypted_text)
file.close()

print("File encrypted successfully!")

# Decrypt the data
decrypted_text = ""

for letter in encrypted_text:
    decrypted_text += chr(ord(letter) - 3)

# Save decrypted data
file = open("decrypted.txt", "w")
file.write(decrypted_text)
file.close()

print("File decrypted successfully!")