# 📝 Web Scraper & Flask Dashboard

Proyek ini adalah aplikasi web sederhana yang dibangun menggunakan **Python** dan framework **Flask**. Aplikasi ini melakukan *web scraping* secara real-time pada situs berita Kompas.com untuk mengambil judul berita utama dan menampilkannya dalam dashboard interaktif atau format JSON API.

## 🚀 Fitur Utama
* **Real-time Scraping**: Mengambil berita terbaru langsung dari Kompas.com setiap kali halaman dimuat.
* **Dashboard Interaktif**: Tampilan antarmuka yang bersih untuk membaca daftar berita.
* **JSON API Endpoint**: Menyediakan data hasil scraping dalam format JSON yang dapat digunakan oleh aplikasi lain.
* **Navigasi Mudah**: Perpindahan antara halaman utama, daftar berita, dan API dengan satu klik.

## 🛠️ Teknologi yang Digunakan
* **Backend**: [Python](https://www.python.org/)
* **Web Framework**: [Flask](https://flask.palletsprojects.com/)
* **Scraping Library**: [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) & [Requests](https://requests.readthedocs.io/)
* **Frontend**: HTML5 & CSS3 (Embedded dalam Python)

---

## 🏁 Cara Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek di komputer lokal Anda.

### 1. Prasyarat
Pastikan Anda sudah menginstal **Python 3.x** di sistem Anda. Cek dengan perintah:
```bash
python --version
```

### 2. Persiapkan Lingkungan (Virtual Environment)
Disarankan untuk menggunakan virtual environment agar library tidak bentrok dengan proyek lain.

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Instal Dependensi
Instal semua library Python yang dibutuhkan melalui pip:
```bash
pip install flask requests beautifulsoup4
```
### 4. Jalankan Aplikasi
Jalankan file utama aplikasi (pastikan nama file sesuai):
```bash
python web_socket.py
```
### 5. Akses di Browser
Buka browser favorit Anda dan akses alamat berikut:
Halaman Utama:
```bash
http://127.0.0.1:5000/
```
Daftar Berita:
```bash
http://127.0.0.1:5000/news
```
API JSON:
```bash
http://127.0.0.1:5000/api/news
```
