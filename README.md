# Project-Management-App
## Kullanılan Teknolojiler 
**Flask** <br/>
**Flask Rest Api** <br/>
**Flask Marshmallow** <br/>
**MongoEngine** <br/>
**Docker** <br/>

Öncelikle uygulamanın çalışabilmesi için MongoDB Atlas üzerinden Cluster açıp database oluşturmanız gerekmektedir.
app.py dosyası üzerinden  MongoDB Atlas 'ın vermiş olduğu linki yapıştırmanız gerekli.



Bu kısımda ise formatladığımız bölgeleri güvenlik gereğince constants.py dosyası açıp database_password ve database_name bilgilerimizi entegre ediyoruz.
```python
DB_URL="mongodb+srv://oguzhan:{}@cluster0.xemc7.mongodb.net/{}?retryWrites=true&w=majority".format(database_password,database_name)

app.config['MONGODB_HOST'] = DB_URL
}
```

Ardından uygulamayı docker ile ayağa kaldırmak istiyorsanız ImageFıle oluşturuyoruz(İsim Size Kalmış) :

```python
docker build -f Dockerfile -t <image_name>:latest . 
```

ImageFile oluştuktan sonra çalıştırmak için son adımımız :

```python
docker run -p 5000:5000 --rm <image_name>
```

**Önemli Not: App.py dosyası üzerinde docker ile ayağa kaldırmak için ayarımızı değiştirmeyi unutmuyoruz.**

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0") 
```

Eğer uygulamayı lokalinizde çalıştırmak istiyorsanız çok küçük bir değişiklik yapmanız yeterli.

```python
if __name__ == "__main__":
    app.run(debug=True) 
```

# API ENDPOINTS

POSTMAN Dökümantasyonuna ulaşmak için : <br/>
[Postman Dökümantasyon](https://documenter.getpostman.com/view/14844311/TzCV3QDL) 
**Kullanıcı İşlemleri**
<br/>

| METOD | İŞLEM | ENDPOINT |
| —— | —— | —— |
| GET | Kullanıcı Kayıtlarını Getirme | /users |
| POST | Kullanıcı Kayıt Oluşturma | /signup |
| POST | Kullanıcı Giriş Yapma | /login |

**İş Kayıt İşlemleri**

| METOD | İŞLEM | ENDPOINT |
| —— | —— | —— |
| GET |  Tüm İş Kayıtlarını Getirme | /tasks |
| GET |  İstenilen İş Kaydını Getirme | /tasks/<task_id> |
| POST | İş Kayıt Oluşturma | /addtask |
| POST | İş Kaydına Yorum Yapma | /comment/<task_id> |
| DELETE | İş Kaydını Silme | /delete/tasks/<task_id> |
| PUT | İş Kaydını Güncelleme | /update/tasks/<task_id> |


**Proje İşlemleri**

| METOD | İŞLEM | ENDPOINT |
| —— | —— | —— |
| GET | Tüm Projeleri Getirme | /projects |
| POST | Proje Oluşturma | /addprojects |
| DELETE | Proje Silme | /delete/project/<project_id>|
| PUT | Proje Güncelleme | /update/project/<project_id>|
