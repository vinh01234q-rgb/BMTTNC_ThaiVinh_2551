from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher 
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

# Khởi tạo đối tượng
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

# --- CAESAR ---
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    return jsonify({'encrypted_message': caesar_cipher.encrypt_text(data.get('plain_text', ''), int(data.get('key', 0)))})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    return jsonify({'decrypted_message': caesar_cipher.decrypt_text(data.get('cipher_text', ''), int(data.get('key', 0)))})

# --- VIGENERE ---
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    return jsonify({'encrypted_text': vigenere_cipher.vigenere_encrypt(data.get('plain_text', ''), data.get('key', ''))})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    return jsonify({'decrypted_text': vigenere_cipher.vigenere_decrypt(data.get('cipher_text', ''), data.get('key', ''))})

# --- RAIL FENCE ---
@app.route('/api/railfence/encrypt', methods=['POST'])
def rf_encrypt():
    data = request.json
    key = int(data.get('key') or data.get('num_rails') or 2)
    return jsonify({'encrypted_text': railfence_cipher.rail_fence_encrypt(data.get('plain_text', ''), key)})

@app.route('/api/railfence/decrypt', methods=['POST'])
def rf_decrypt():
    data = request.json
    key = int(data.get('key') or data.get('num_rails') or 2)
    return jsonify({'decrypted_text': railfence_cipher.rail_fence_decrypt(data.get('cipher_text', ''), key)})

# --- PLAYFAIR ---
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_matrix():
    data = request.json
    matrix = playfair_cipher.create_playfair_matrix(data.get('key', ''))
    return jsonify({"playfair_matrix": matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def pf_encrypt():
    data = request.json
    matrix = playfair_cipher.create_playfair_matrix(data.get('key', ''))
    return jsonify({'encrypted_text': playfair_cipher.playfair_encrypt(data.get('plain_text', ''), matrix)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def pf_decrypt():
    data = request.json
    matrix = playfair_cipher.create_playfair_matrix(data.get('key', ''))
    return jsonify({'decrypted_text': playfair_cipher.playfair_decrypt(data.get('cipher_text', ''), matrix)})

# --- TRANSPOSITION ---
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.json
    return jsonify({'encrypted_text': transposition_cipher.encrypt(data.get('plain_text', ''), int(data.get('key', 1)))})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.json
    return jsonify({'decrypted_text': transposition_cipher.decrypt(data.get('cipher_text', ''), int(data.get('key', 1)))})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)