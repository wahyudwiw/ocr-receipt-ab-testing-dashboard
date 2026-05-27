# app.py

import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np
import yaml
import re

# ======================================
# TESSERACT PATH
# ======================================

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ======================================
# LOAD YAML
# ======================================

with open("dataset/data.yaml", "r") as f:
    data = yaml.safe_load(f)

classes = data["names"]

# ======================================
# STREAMLIT TITLE
# ======================================

st.set_page_config(
    page_title="OCR Receipt A/B Testing Dashboard",
    layout="wide"
)

st.title("OCR Receipt A/B Testing Dashboard")

st.write("Perbandingan OCR Original vs Preprocessing")

# ======================================
# UPLOAD IMAGE
# ======================================

uploaded_file = st.file_uploader(
    "Upload Gambar Struk",
    type=["jpg", "png", "jpeg"]
)

# ======================================
# JIKA FILE DIUPLOAD
# ======================================

if uploaded_file is not None:

    # ======================================
    # LOAD IMAGE
    # ======================================

    image = Image.open(uploaded_file)

    img = np.array(image)

    st.subheader("Gambar Struk")

    st.image(image, use_container_width=True)

    # ======================================
    # A = ORIGINAL OCR
    # ======================================

    text_original = pytesseract.image_to_string(img)

    # ======================================
    # B = PREPROCESSING OCR
    # ======================================

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    thresh = cv2.threshold(
        gray,
        150,
        255,
        cv2.THRESH_BINARY
    )[1]

    text_thresh = pytesseract.image_to_string(thresh)

    # ======================================
    # A/B TESTING DISPLAY
    # ======================================

    col1, col2 = st.columns(2)

    # ORIGINAL
    with col1:

        st.subheader("A - Original")

        st.image(img, use_container_width=True)

        st.subheader("OCR Original")

        if text_original.strip() == "":
            st.warning("Teks tidak terbaca")
        else:
            st.text(text_original)

    # PREPROCESSING
    with col2:

        st.subheader("B - Grayscale + Threshold")

        st.image(thresh, use_container_width=True)

        st.subheader("OCR Preprocessing")

        if text_thresh.strip() == "":
            st.warning("Teks tidak terbaca")
        else:
            st.text(text_thresh)

    # ======================================
    # ANALISIS A/B TESTING
    # ======================================

    st.subheader("Hasil A/B Testing")

    original_len = len(text_original)
    thresh_len = len(text_thresh)

    st.write(f"Jumlah karakter OCR Original : {original_len}")
    st.write(f"Jumlah karakter OCR Preprocessing : {thresh_len}")

    if thresh_len > original_len:
        st.success("Preprocessing menghasilkan OCR lebih baik")

    elif thresh_len < original_len:
        st.warning("OCR Original lebih baik")

    else:
        st.info("Hasil OCR keduanya sama")

    # ======================================
    # LABEL EXTRACTION
    # ======================================

    st.subheader("Label Extraction")

    # STORE
    store = "-"

    lines = text_thresh.split('\n')

    for line in lines:

        line = line.strip()

        if len(line) > 3 and any(c.isalpha() for c in line):
            store = line
            break

    # DATE
    date_pattern = r'\d{2}[/-]\d{2}[/-]\d{2,4}'

    date_match = re.search(date_pattern, text_thresh)

    date = date_match.group() if date_match else "-"

    # TOTAL
    total = "-"

    for line in lines:

        if "total" in line.lower():

            angka = re.findall(r'[\d.,]+', line)

            if angka:
                total = angka[-1]
                break

    # ======================================
    # SHOW LABEL
    # ======================================

    st.success(f"Store : {store}")
    st.success(f"Date : {date}")
    st.success(f"Total : {total}")

else:

    st.info("Silakan upload gambar struk terlebih dahulu")