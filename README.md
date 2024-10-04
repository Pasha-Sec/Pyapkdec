# Pyapkdec
![bfust](https://github.com/user-attachments/assets/40be6a68-8b8f-475b-957f-caddc8d47032)
APK dosyalarını parçalamak (decompile) ve yeniden derlemek (recompile) için bir Python tabanlı araçtır. Kullanıcı dostu bir arayüz sağlayan bu yazılım, APK dosyalarının iç yapısını analiz etmek ve Android uygulamaları üzerinde çalışmalar yapmak isteyen geliştiriciler için uygundur. Ayrıca ana aktivitenin belirlenmesi gibi özellikleriyle hızlı bir analiz imkanı sunar.

## Özellikler
APK Dosyası Seçimi: Kullanıcı, dosya seçici aracılığıyla APK dosyasını kolayca seçebilir.
Decompile İşlemi: APK dosyasını decompile eder ve AndroidManifest.xml gibi önemli dosyalara erişim sağlar.
Ana Aktiviteyi Gösterme: Decompile edilen APK'nin ana aktivitesini gösterir.
Recompile İşlemi: Decompile edilen APK'yi yeniden derleyerek onarılmış bir APK oluşturur.
Kullanıcı Dostu Arayüz: Basit, etkili ve terminal görünümüne sahip grafik arayüz ile kolay kullanım sağlar.
Arkaplan Görseli ve Logo: Arayüze estetik katmak için görseller kullanılmıştır.

## Gereksinimler
1. Python 3.x
2. apktool yüklü olmalıdır. APK dosyalarını decompile etmek ve yeniden derlemek için kullanılır.
3. Pillow: Python Imaging Library (PIL), arayüzdeki görselleri işlemek için kullanılır.
4. pyaxmlparser: AndroidManifest.xml dosyasını analiz etmek için kullanılır.

## Kurulum
Gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu kullanabilirsiniz:
```pip install pillow pyaxmlparser```
Daha sonra,
```git clone https://github.com/Pasha-Sec/Pyapkdec.git```

## Kullanım
1. Programı çalıştırdığınızda arayüzde bir Dosya Seç butonu göreceksiniz. Bu butona tıklayarak bir APK dosyası seçin.
2. APK dosyasını seçtikten sonra Parçala! butonuna basarak dosyayı decompile edin. Program, seçilen APK'nin ana aktivitesini bulacak ve decompile edilen dosya yolunu gösterecektir.
3. Eğer decompile edilen dosyaları yeniden derlemek istiyorsanız, Onar butonuna basarak APK'yi yeniden derleyebilirsiniz.

![bfguiscreen](https://github.com/user-attachments/assets/e704c754-f2a6-449b-a986-567e941ae0f9)


