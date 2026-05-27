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

---

# Project Structure

```bash
dbs/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/username/repository-name.git
```

---

## 2. Masuk ke Folder Project

```bash
cd repository-name
```

---

## 3. Install Library

```bash
pip install -r requirements.txt
```

atau:

```bash
py -m pip install -r requirements.txt
```

---

# Install Tesseract OCR

## Windows

Download Tesseract OCR:

https://github.com/UB-Mannheim/tesseract/wiki

Pastikan lokasi instalasi:

```bash
C:\Program Files\Tesseract-OCR\tesseract.exe
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

Evaluasi dilakukan berdasarkan hasil ekstraksi teks OCR.

---

# Output Information Extraction

Sistem menampilkan:
- Store
- Date
- Total

berdasarkan hasil OCR dari gambar struk.

---

# Deployment

Dashboard dapat di-deploy menggunakan Streamlit Cloud:

https://streamlit.io/cloud

---

# Author
