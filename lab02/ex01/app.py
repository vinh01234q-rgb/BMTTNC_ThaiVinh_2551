from flask import Flask, render_template, request
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

@app.route("/")
def index():
    return render_template('index.html')

# Route điều hướng trang cho cả 5 bài
@app.route("/<algo>")
def algo_page(algo):
    return render_template(f'{algo}.html')

# ROUTE XỬ LÝ CHUNG (Để không bao giờ bị lỗi 404)
@app.route("/process/<algo>/<mode>", methods=['POST'])
def process(algo, mode):
    # Lấy dữ liệu (hỗ trợ cả 2 tên biến thường gặp trong form)
    text = request.form.get('inputPlainText') or request.form.get('inputCipherText')
    key_raw = request.form.get('inputKey')
    res = ""

    try:
        if algo == 'caesar':
            res = caesar_cipher.encrypt_text(text, int(key_raw)) if mode == 'enc' else caesar_cipher.decrypt_text(text, int(key_raw))
        
        elif algo == 'vigenere':
            res = vigenere_cipher.vigenere_encrypt(text, key_raw) if mode == 'enc' else vigenere_cipher.vigenere_decrypt(text, key_raw)
        
        elif algo == 'railfence':
            res = railfence_cipher.rail_fence_encrypt(text, int(key_raw)) if mode == 'enc' else railfence_cipher.rail_fence_decrypt(text, int(key_raw))
        
        elif algo == 'playfair':
            matrix = playfair_cipher.create_playfair_matrix(key_raw)
            res = playfair_cipher.playfair_encrypt(text, matrix) if mode == 'enc' else playfair_cipher.playfair_decrypt(text, matrix)
        
        elif algo == 'transposition':
            res = transposition_cipher.encrypt(text, int(key_raw)) if mode == 'enc' else transposition_cipher.decrypt(text, int(key_raw))
    except Exception as e:
        res = f"Lỗi: {str(e)}"

    return render_template(f'{algo}.html', result=res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)