# Link to katalog : https://tugas2pbp.herokuapp.com/katalog/

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita memakai virtual environment supaya dapat mengelola *packages* Python untuk proyek-proyek lain agar kita tidak meng-*install* *packages* Python secara global yang dimana dapat merusak alat sistem atau proyek lainnya. Kita tetap dapat menmbuat aplikasi web berbasis Django tanpa menggunakan *virtual environemnt* tetapi seperti poin sebelumnya bisa saja dengan meng-*install* secara global dapat merusak alat sistem atau proyek lainnya.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas

    1. Pertama saya membuat fungsi show_katalog agar dapat merender models dengan mengembalikannya dalam HTML
    2. Kedua saya melakukan routing antara views.py dengan katalog.html dengan memberikan nama file HTML yang saya ingin pakai yaitu katalog.html
    3. Ketiga saya membuat FILLME! menjadi {{nama}} agar dapat menampilkan nama saya yang sudah saya definisikan pada context pada views.py dan FILLME! kedua saya ganti menjadi {{npm}} supaya dapat menampilkan NPM saya yang sudah saya definisikan pada context pada views.py dan yang terakhir saya membuat *for loop* di katalog.html untuk menapilkan barang-barang pada katalog beserta atribut-atributnya yang sudah saya kodekan pada katalog.html
    4. Terakhir saya membuat repository secret dengan *key* HEROKU_API_KEY dan HEROKU_APP_NAME dan saya isikan *key*-nya dengan *value* yang bersesuaian
