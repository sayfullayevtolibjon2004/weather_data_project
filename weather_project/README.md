Loyiha haqida:
1 weather ob havo malumotlari saytidan url dan shaxsiy api token orqali o'zbekiston respublikasining barcha viloyotlari ob-havo malumotlari tortildi
2.python pandas orqali tartiblandi (jadvalningn maydon nomlari o'zgartirildi,malumbir kerak maydonlar olindi )
3 pyodbc kutubxonasi orqali sssmsga (sql serverga yuklandi ) malumotlar yuklandi
4 loyiha jarayonida to'laqonli linux operatsion sistemasidan foydalanildi

Avtomatik ishlashi:

1 avtomatik ishlashi uchun bash (linux) terminali orqali cron yozildi.
2 Hamma kompyuterda ishlashi uchun Dockerfile va docker-compose.yml fayllardan foydalanib konteyner tuzildi.
3.u yerda avtomatik loglar yoziladi




kerakli kutubxonalar requirements.txt fileda kerakli kutubxonalar mavjud 

database:
1. loyiha sql server bilan bog'landi
2. vaqtinchalik jadval yaratilib malumotlar tekshirilgandan keyen asosiy jadvalga qo'shuvchi procedura qo'shildi.

ishlatilgan texnalogiyalar:
ssms sql server
python (library pandas pyodbd requests...)
linux operation system
docker
git hub
git 

loyiha qiladigan ish :
o'zbekton viloyatlari ob havosini har kuni soat 11:00 da bazaga qo'shish .

