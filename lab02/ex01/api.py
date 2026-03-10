from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher # Mới

app = Flask(__name__)

# Khởi tạo 3 đối tượng
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence_cipher = RailFenceCipher()

# --- CAESAR ROUTES ---
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    return jsonify({'encrypted_message': caesar_cipher.encrypt_text(data.get('plain_text', ''), int(data.get('key', 0)))})

# --- VIGENERE ROUTES ---
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    return jsonify({'encrypted_text': vigenere_cipher.vigenere_encrypt(data.get('plain_text', ''), data.get('key', ''))})

# --- RAIL FENCE ROUTES (EX03) ---
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    num_rails = int(data.get('num_rails', 2))
    encrypted_text = rail_fence_cipher.rail_fence_encrypt(plain_text, num_rails)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    num_rails = int(data.get('num_rails', 2))
    decrypted_text = rail_fence_cipher.rail_fence_decrypt(cipher_text, num_rails)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)