# OCR Receipt A/B Testing Dashboard

Dashboard OCR berbasis Streamlit untuk melakukan:
- OCR gambar struk
- Preprocessing gambar
- A/B Testing OCR
- Information Extraction:
  - Store
  - Date
  - Total

---

# Features

✅ Upload gambar struk  
✅ OCR menggunakan Tesseract OCR  
✅ A/B Testing preprocessing  
✅ Information extraction:
- Store
- Date
- Total

✅ Dashboard interaktif menggunakan Streamlit

---

# Technologies Used

- Python
- Streamlit
- OpenCV
- Pytesseract
- NumPy
- Tesseract OCR

---

# Project Structure

```bash
├── app.py
├── requirements.txt
├── packages.txt
├── runtime.txt
├── README.md
├── .gitignore
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/username/ocr-receipt-ab-testing-dashboard.git
```

---

## 2. Masuk ke Folder Project

```bash
cd ocr-receipt-ab-testing-dashboard
```

---

# Install Python

Download Python:

https://www.python.org/downloads/

Saat install:
✅ Centang "Add Python to PATH"

Cek Python:

```bash
python --version
```

atau:

```bash
py --version
```

---

# Install Tesseract OCR (WAJIB)

Project ini menggunakan OCR Engine:
Tesseract OCR

## Download Tesseract OCR

Windows:

https://github.com/UB-Mannheim/tesseract/wiki

---

# Install Tesseract OCR

Saat instalasi:
- gunakan default installation
- pastikan lokasi install:

```bash
C:\Program Files\Tesseract-OCR\
```

---

# Cek Tesseract OCR

Buka CMD / PowerShell:

```bash
tesseract --version
```

Jika berhasil akan muncul versi Tesseract OCR.

---

# Install Python Library

```bash
pip install -r requirements.txt
```

atau:

```bash
py -m pip install -r requirements.txt
```

---

# Run Streamlit

```bash
streamlit run app.py
```

atau:

```bash
py -m streamlit run app.py
```

---

# A/B Testing Method

Metode preprocessing yang dibandingkan:
- A = Original Image
- B = Grayscale + Threshold

Evaluasi dilakukan berdasarkan hasil OCR.

---

# Information Extraction

Sistem menampilkan:
- Store
- Date
- Total

berdasarkan hasil OCR dari gambar struk.

---

# Deployment

Dashboard dapat di-deploy menggunakan Streamlit Cloud:

https://ocr-receipt-ab-testing-dashboard.streamlit.app/

---

# Author


