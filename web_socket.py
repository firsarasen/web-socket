from flask import Flask, render_template_string, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# --- FUNGSI SCRAPING (Logika dari main.py) ---
def get_kompas_headlines():
    url = "https://www.kompas.com"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Mencari semua judul berita (tag h1 dengan class hlTitle)
        headlines = soup.find_all("h1", class_="hlTitle")
        
        data = []
        for i, item in enumerate(headlines, start=1):
            data.append({
                "no": i,
                "judul": item.text.strip()
            })
        return data
    except Exception as e:
        return [{"no": 0, "judul": f"Gagal mengambil data: {str(e)}"}]

# --- ROUTING ---

@app.route('/')
def home():
    """Halaman Utama dengan navigasi"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Scrapping & Web Socket</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; line-height: 1.6; }
            .container { max-width: 800px; margin: auto; }
            .btn { display: inline-block; background: #3498db; color: white; padding: 10px 20px; 
                   text-decoration: none; border-radius: 5px; margin-top: 20px; }
            .btn:hover { background: #2980b9; }
            .card { border: 1px solid #ddd; padding: 20px; border-radius: 8px; background: #f9f9f9; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Web Scraper Dashboard</h1>
            <div class="card">
                <p>Project ini menggabungkan <strong>Web Scrapping Python</strong> dan <strong>Web Socket Flask Framework</strong>.</p>
                <p>Data diambil secara langsung dari Kompas.com saat Anda menekan tombol di bawah.</p>
                <a href="/news" class="btn">Lihat Berita Terbaru</a>
                <a href="/api/news" class="btn" style="background:#2ecc71">Cek JSON API</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/news')
def show_news():
    """Menampilkan hasil scraping dalam bentuk tabel HTML"""
    news_data = get_kompas_headlines()
    
    # Membuat baris tabel secara dinamis
    table_rows = ""
    for item in news_data:
        table_rows += f"<tr><td>{item['no']}</td><td>{item['judul']}</td></tr>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Latest News</title>
        <style>
            body {{ font-family: sans-serif; margin: 40px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #3498db; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            .back {{ margin-bottom: 20px; display: block; }}
        </style>
    </head>
    <body>
        <a href="/" class="back">← Kembali ke Home</a>
        <h1>📰 Berita Utama Kompas.com</h1>
        <table>
            <tr>
                <th style="width: 50px;">No</th>
                <th>Judul Berita</th>
            </tr>
            {table_rows}
        </table>
        <p><small>Data di-scrape pada: Real-time</small></p>
    </body>
    </html>
    """

@app.route('/api/news')
def api_news():
    """Endpoint API yang mengembalikan JSON (seperti fungsi simpan data di main.py)"""
    news_data = get_kompas_headlines()
    return jsonify({
        "source": "kompas.com",
        "total_results": len(news_data),
        "articles": news_data
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)