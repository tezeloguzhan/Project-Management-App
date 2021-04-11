# Project-Management-App
## Technologies Stack 
**Flask** <br/>
**Flask Rest Api** <br/>
**Flask Marshmallow** <br/>
**MongoEngine** <br/>
**Docker** <br/>

Öncelikle uygulamanın çalışabilmesi için MongoDB Atlas üzerinden Cluster açıp database oluşturmanız gerekmektedir.
app.py dosyası üzerinden  MongoDB Atlas 'ın vermiş olduğu linki yapıştırmanız gerekli.



Bu kısımda ise formatladığımız bölgeleri güvenlik gereğince constants.py dosyası açıp database_password ve database_name bilgilerini entegre ediyoruz.
```python
DB_URL="mongodb+srv://oguzhan:{}@cluster0.xemc7.mongodb.net/{}?retryWrites=true&w=majority".format(database_password,database_name)

app.config['MONGODB_HOST'] = DB_URL
}
```

Ardından uygulamayı docker ile ayağa kaldırmak istiyorsanız ImageFıle oluşturuyoruz :

```python
docker build -f Dockerfile -t <image_name>:latest . 
```

ImageFile oluştuktan sonra çalıştırmak için son adımımız :

```python
docker run -p 5000:5000 --rm <image_name>
```

**Önemli Not: App.py dosyası üzerinde docker ile ayağa kaldırmak için ayarımızı değiştirmeyi unutmuyoruz.

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0") 
```



