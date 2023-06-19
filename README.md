# Flask Todo List

Bu repo, Flask web çatısı kullanılarak geliştirilmiş bir yapılacaklar listesi (todo list) uygulamasını içermektedir. Bu uygulama, kullanıcılara yapılacak işleri ekleyebilme, düzenleyebilme ve tamamlandıkça işaretleyebilme özellikleri sunar.

## Özellikler

- Kullanıcılar, yapılacak işleri ekleyebilir, düzenleyebilir ve silebilir.
- Her iş, başlık, açıklama ve tamamlanma durumu bilgilerini içerir.
- Kullanıcılar, tamamlanan işleri işaretleyebilir ve yeniden geri alabilir.
- Tüm yapılacak işler listesi ve tamamlanan işler listesi görüntülenebilir.
- Kullanıcılar, giriş yapabilir ve hesaplarını yönetebilir.
- Oturum açmayan kullanıcılar, sadece yapılacak işleri görüntüleyebilir, ancak düzenleme yapamazlar.

## Nasıl Çalışır?

Flask Todo List, Flask ve Python programlama dilleri kullanılarak geliştirilmiştir. Uygulama, SQLite veritabanı kullanır ve temel CRUD (Create, Read, Update, Delete) işlemlerini gerçekleştirir.

Uygulamayı çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Python'u bilgisayarınıza yükleyin (https://www.python.org/downloads/).

2. Repo bağlantısını kullanarak projeyi bilgisayarınıza indirin:
```
git clone https://github.com/KaygusuzBK/Flask-Todo-List.git
```

3. İndirilen dizine gidin:
```
cd Flask-Todo-List
```

4. Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:
```
pip install -r requirements.txt
```

5. Uygulamayı başlatmak için aşağıdaki komutu çalıştırın:
```
python app.py
```

6. Web tarayıcınızda `http://localhost:5000` adresini açın ve uygulamayı görüntüleyin.

## Kullanım

Uygulamanın kullanımı için aşağıdaki adımları izleyebilirsiniz:

1. Ana sayfada, yeni bir kullanıcı hesabı oluşturun veya mevcut bir hesapla giriş yapın.

2. Giriş yaptıktan sonra, yapılacak işlerin listesini göreceksiniz. Yeni bir iş eklemek için "Add Task" düğmesine tıklayın.

3. İş ekleme formunda, işin başlığını, açıklamasını ve tamamlanma durumunu belirtin. Ardından "Add" düğmesine tıklayın.

4. Eklenen işler, ana sayfada görüntülenecektir. İ

şleri düzenlemek veya silmek için ilgili düğmelere tıklayabilirsiniz.

5. Tamamlanan işleri işaretlemek veya geri almak için ilgili işaretleyiciyi tıklayabilirsiniz.

6. Tüm yapılacak işler listesini ve tamamlanan işler listesini görüntülemek için "All Tasks" veya "Completed Tasks" düğmelerine tıklayabilirsiniz.

## Katkı

Her türlü katkıya açığız! Eğer bu projeye katkıda bulunmak isterseniz, lütfen bir Pull Request oluşturun veya bize bildirin.

---
