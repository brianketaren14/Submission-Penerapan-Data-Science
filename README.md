# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

### Permasalahan Bisnis
Jumlah dropout yang tinggi ini menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
Adapaun cakupan proyek ini meliputi Persiapan Data, Data Understanding, Modelling, dan Pembuatan Dashboard.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```
numpy, pandas, scipy, matplotlib, seaborn, tensorflow, keras, streamlit
```

## Business Dashboard
Dashboard ini berfungsi memahami data dan memonitor berbagai faktor yang mempengaruhi tingginya dropout rate.

link : https://lookerstudio.google.com/reporting/232a6cd4-6254-47a6-9cb7-a579b6363e3e

![image](https://github.com/user-attachments/assets/f998d368-d751-4184-8514-a5e05ad14c30)

## Menjalankan Sistem Machine Learning
Untuk melakukan prediksi : Input nilai untuk setiap feature lalu klik tombol predict.

link : https://submission-penerapan-data-science-aejqjgfevn9rrsvgquvrdc.streamlit.app/

![image](https://github.com/user-attachments/assets/efbb1a1a-ceb4-4e6d-ac78-f0c1865ca763)

## Conclusion

### EDA

- Siswa dropout kebanyakan memiliki application order 1.
- Siswa dropout kebanyakan memiliki previous qualification grade sebesar 120-140.
- Siswa droput kebanyakan memiliki admission grade sebesar 120-140.
- Siswa dropout kebanyakan memiliki age at enrollment sebsear 15-20 tahun.
- Siswa dropout kebanyakan memiliki curricular units 1st sem (credited) sebesar 0.
- Siswa dropout kebanyakan memiliki curricular units 1st sem (enrolled) sebesar 5-6.
- Siswa dropout kebanyakan memiliki curricular units 1st sem (evaluations) sebesar 0.
-Siswa dropout kebanyakan memiliki curricular units 1st sem (approved) sebesar 0.
- Siswa dropout kebanyakan memiliki martial status single.
- Siswa dropout kebanyakan datang saat daytime.
- Siswa dropout kebanyakan bukan displaced person.
- Siswa dropout kebanyakan tidak membudtuhkan kebutuhan khusus,
- Siswa dropout kebanyakan bukan seorang debtor.
- Siswa dropout kebanyakan mempunyai biaya sekolah yang sesuai.
- Siswa dropout kebanyakan memiliki gender perempuan dan laki-laki (seimbang).
- Siswa dropout kebanyakan tidak memiliki beasiswa.
- Siswa dropout kebanyakan bukan siswa international.
- Siswa dropout kebanyakan memiliki application mode lewat 23 tahun.
- Siswa dropout kebanyakan berasal dari course management.
- Siswa dropout kebanyakan berasal dari secondary education.
- Siswa dropout kebanyakan berasal dari negaral Portugal.
- Siswa dropout kebanyakan memiliki mother's qualification Basic education 1st cycle (4th/5th year) or equiv.
- Siswa dropout kebanyakan memiliki father's qualification Basic education 1st cycle (4th/5th year) or equiv.
- Siswa dropout kebanyakan memiliki mother's occupation unskilled workers.
- Siswa dropout kebanyakan memiliki father's occupation unskilled workers.


### Model
- model good fit dengan accuracy 73%-75%.

### Action Items
1. Intervensi Akademik

- Tingkatkan Dukungan Akademik di Semester Pertama: Karena banyak siswa dropout memiliki nilai yang rendah dalam unit kurikuler semester pertama (0 kredit, 0 evaluasi, 0 disetujui), penting untuk memberikan dukungan akademik yang lebih intensif sejak awal. Program bimbingan, kelas tambahan, dan pengawasan lebih ketat bisa membantu siswa mengatasi kesulitan awal.

- Program Pembelajaran dan Kelas Remedial: Untuk siswa dengan nilai penerimaan dan kualifikasi sebelumnya di kisaran 120-140, mungkin ada kebutuhan untuk menilai kembali kurikulum dan memastikan bahwa materi yang diajarkan sesuai dengan tingkat pengetahuan mereka. Menyediakan kelas remedial atau tutorial tambahan bisa mengurangi kesulitan akademik.

2. Dukungan Psikososial
- Konseling dan Dukungan Kesejahteraan: Mengingat banyak siswa dropout yang berada pada rentang usia 15-20 tahun, usia yang sering kali menantang secara emosional, penting untuk menyediakan layanan konseling dan dukungan psikososial. Program konseling bisa membantu siswa mengatasi stres, tekanan, dan tantangan pribadi.

- Program Orientasi dan Pembimbingan: Siswa yang datang pada waktu siang dan dari latar belakang pendidikan menengah mungkin merasa terisolasi. Program orientasi dan pembimbingan dapat membantu mereka beradaptasi dengan lingkungan akademik baru dan membangun jaringan sosial di kampus.

3. Strategi Keterlibatan dan Motivasi
- Keterlibatan Orang Tua: Dengan banyak siswa memiliki orang tua dengan kualifikasi dan pekerjaan yang tidak terampil, melibatkan orang tua dalam proses pendidikan dan memberikan mereka informasi tentang cara mendukung anak-anak mereka di rumah bisa berkontribusi pada keberhasilan siswa.

- Motivasi dan Penghargaan: Program motivasi yang mencakup penghargaan untuk pencapaian akademik atau kemajuan dalam kurikulum bisa menjadi insentif untuk siswa agar tetap terlibat dan berkomitmen pada studi mereka.

4. Pendekatan Administratif
- Evaluasi dan Penyesuaian Aplikasi: Mengingat banyak siswa yang dropout mengajukan aplikasi lewat 23 tahun, mungkin perlu untuk menilai proses penerimaan dan memastikan bahwa siswa yang lebih muda atau baru lulus dari pendidikan menengah diprioritaskan dan diberikan dukungan tambahan.

- Pemantauan dan Analisis Berkelanjutan: Mengembangkan sistem pemantauan yang dapat mengidentifikasi siswa yang berisiko tinggi untuk dropout lebih awal. Data ini harus digunakan untuk memberikan intervensi dini yang sesuai.

5. Penanganan Spesifik Berdasarkan Latar Belakang
- Pendekatan untuk Kursus Management dan Pendidikan Sekunder: Karena banyak siswa yang dropout berasal dari kursus manajemen dan pendidikan menengah, menilai dan memperbaiki program studi di bidang ini serta menyesuaikan pendekatan pengajaran bisa membantu mengurangi angka dropout.

- Menangani Biaya Sekolah: Memastikan bahwa biaya sekolah tidak menjadi kendala untuk siswa dan menyediakan bantuan keuangan atau beasiswa tambahan bagi mereka yang membutuhkan dapat membantu dalam mengurangi dropout.

6. Diversifikasi dan Inklusi
- Meningkatkan Program Inklusi: Walaupun sebagian besar dropout bukan siswa internasional, penting untuk memastikan bahwa semua siswa, termasuk siswa internasional, merasa diterima dan mendapatkan dukungan yang diperlukan untuk berhasil di akademik.
- Dengan mengikuti langkah-langkah ini, diharapkan dapat mengurangi angka dropout dan meningkatkan tingkat keberhasilan siswa secara keseluruhan.
