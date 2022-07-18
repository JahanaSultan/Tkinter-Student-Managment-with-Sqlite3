Bu proyekt tələbələrin qiymətləndirilməsi üçündür. Database olaraq Sqlite3 istifadə olunmuşdur.

3 giriş mövcuddur. Tələbə, Müəllim və Admin. 

Tələbə girişinə örnək: 

username: cahana@gmail.com
password: 123456

Müəllim girişinə örnək:

username: abc
password:123456

Admin girişi:

username: admin
password: admin

Run etmədən öncə pillow yüklü olmasına diqqət edin. Pillow yoxdursa:

pip install pillow 

Tələbə yalnız məlumatlarını görə bilir.
Müəllim sadəcə öz qruplarını görür, qiymət yazır və yazdığı qiyməti dəyişə bilir.
Admin yeni tələbə, müəllim, dərs və grup qeydiyyatdan keçirir.