import streamlit as st

# Judul aplikasi
st.title("Deteksi Tingkat Stres")

# Deskripsi aplikasi
st.write("""
Aplikasi ini membantu Anda menilai tingkat stres yang Anda alami saat ini. 
Silakan jawab pertanyaan-pertanyaan berikut sesuai dengan kondisi Anda.
""")

# Pertanyaan dan opsi jawaban
questions = {
    "Seberapa sering Anda merasa cemas atau khawatir?": ["Tidak pernah", "Jarang", "Kadang-kadang", "Sering", "Selalu"],
    "Seberapa sering Anda merasa sulit untuk tidur atau mengalami gangguan tidur?": ["Tidak pernah", "Jarang", "Kadang-kadang", "Sering", "Selalu"],
    "Seberapa sering Anda merasa lelah atau kehabisan energi?": ["Tidak pernah", "Jarang", "Kadang-kadang", "Sering", "Selalu"],
    "Seberapa sering Anda merasa sulit berkonsentrasi?": ["Tidak pernah", "Jarang", "Kadang-kadang", "Sering", "Selalu"],
    "Seberapa sering Anda merasa kehilangan minat dalam aktivitas sehari-hari?": ["Tidak pernah", "Jarang", "Kadang-kadang", "Sering", "Selalu"],
}

# Skor untuk setiap jawaban (dari 0 hingga 4)
scores = {
    "Tidak pernah": 0,
    "Jarang": 1,
    "Kadang-kadang": 2,
    "Sering": 3,
    "Selalu": 4
}

# Pengumpulan jawaban
total_score = 0
for question, options in questions.items():
    answer = st.radio(question, options)
    total_score += scores[answer]

# Menampilkan hasil berdasarkan skor total
if st.button("Tampilkan Hasil"):
    st.write("**Skor Anda:**", total_score)

    if total_score <= 10:
        st.success("Anda baik-baik saja. Tidak ada indikasi stres.")
    elif total_score <= 20:
        st.warning("Anda mengalami stres ringan. Cobalah untuk rileks dan atasi sumber stres Anda.")
    elif total_score <= 30:
        st.warning("Anda mengalami stres sedang. Disarankan untuk mencari dukungan atau konsultasi.")
    else:
        st.error("Anda mengalami stres berat. Penting untuk segera mencari bantuan profesional.")

# Informasi tambahan
st.info("Aplikasi ini tidak menggantikan konsultasi dengan profesional kesehatan mental. Jika Anda merasa perlu, segera hubungi ahli kesehatan mental.")
