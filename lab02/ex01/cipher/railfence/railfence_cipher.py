class RailFenceCipher:
    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1: return plain_text
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1

        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        return "".join(["".join(rail) for rail in rails])

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1: return cipher_text
        
        # Bước 1: Tính độ dài từng rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Bước 2: Chia cipher_text vào các rail
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Bước 3: Đọc zigzag để lấy lại plain_text
        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0) # Lấy ký tự đầu tiên ra
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text