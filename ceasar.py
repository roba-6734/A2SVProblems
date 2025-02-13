def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char
    return decrypted_text

encrypted_text = """Ghdu Vwxghqwv
Sohdvh surylgh ph zlwk wkh iroorzlqj 

 Brxu Ixoo Qdph 

Brxu LG 

Brxu Ode Vhfwlrq Qxpehu"""

  # Example Caesar cipher

  
# print("Brute Force Decryption Attempts:")
# for shift in range(1, 26):
#     print(f"Shift {shift}: {caesar_decrypt(encrypted_text, shift)}")

print(caesar_decrypt(encrypted_text,3))
