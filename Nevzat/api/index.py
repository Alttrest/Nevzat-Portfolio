from flask import Flask, render_template, jsonify

# Vercel klasör yapısına göre template ve static yollarını bir üst dizin olarak ayarlıyoruz
app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def home():
    # templates klasöründeki index.html dosyasını ekrana basar
    return render_template('index.html')

# İleride projeleri veritabanından çekmek istersen diye örnek bir API endpoint'i
@app.route('/api/projeler')
def get_projeler():
    return jsonify({
        "status": "success",
        "mesaj": "Backend aktif ve çalışıyor!"
    })

# Vercel'in uygulamayı bulabilmesi için 'app' değişkeni hazır olmalı
if __name__ == '__main__':
    app.run(debug=True)