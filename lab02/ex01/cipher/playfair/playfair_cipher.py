class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = []
        for char in key:
            if char not in key_set and char.isalpha():
                key_set.append(char)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in key_set:
                key_set.append(char)
        
        matrix = [key_set[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper().replace(" ", "")
        processed_text = ""
        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            if (i + 1) < len(plain_text):
                b = plain_text[i+1]
                if a == b:
                    processed_text += a + "X"
                    i += 1
                else:
                    processed_text += a + b
                    i += 2
            else:
                processed_text += a + "X"
                i += 1
        
        encrypted_text = ""
        for i in range(0, len(processed_text), 2):
            row1, col1 = self.find_letter_coords(matrix, processed_text[i])
            row2, col2 = self.find_letter_coords(matrix, processed_text[i+1])
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper().replace(" ", "")
        decrypted_text = ""
        
 
        for i in range(0, len(cipher_text), 2):
            if (i + 1) < len(cipher_text):
                coords1 = self.find_letter_coords(matrix, cipher_text[i])
                coords2 = self.find_letter_coords(matrix, cipher_text[i+1])
                
                if not coords1 or not coords2: 
                    continue 
                
                row1, col1 = coords1
                row2, col2 = coords2
                
                if row1 == row2:
                    decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
                elif col1 == col2:
                    decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
                else:
                    decrypted_text += matrix[row1][col2] + matrix[row2][col1]

     
        final_text = ""
        i = 0
        while i < len(decrypted_text):
            char = decrypted_text[i]
           
            if char == 'X' and i > 0 and i < len(decrypted_text) - 1:
                if decrypted_text[i-1] == decrypted_text[i+1]:
                    i += 1 
                    continue
            
            final_text += char
            i += 1

        
        if final_text.endswith('X'):
            final_text = final_text[:-1]
            
        return final_text