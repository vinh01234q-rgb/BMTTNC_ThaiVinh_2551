from .alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                # Công thức: (vị trí cũ + khóa) chia lấy dư cho 26
                output_index = (letter_index + key) % alphabet_len
                encrypted_text.append(self.alphabet[output_index])
            else:
                # Nếu là khoảng trắng hoặc số thì giữ nguyên
                encrypted_text.append(letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        # Giải mã thực chất là mã hóa với khóa âm
        return self.encrypt_text(text, -key)    