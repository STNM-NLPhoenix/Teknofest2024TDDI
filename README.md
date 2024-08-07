![NLPhoenix Logo](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/NLPhoenix.png)

## 📜 İçerik

1. [**Proje ve Ekip Tanıtımı**](#proje-ve-ekip-tanıtımı) 📋
   - [Ekip Tanıtımı](#ekip-tanıtımı)
   - [Projenin Kapsamı ve Hedefleri](#projenin-kapsamı-ve-hedefleri)
   - [Kullanılan Teknikler ve Yöntemler](#kullanılan-teknikler-ve-yöntemler)

2. [**Veri Kümesi**](#veri-kümesi) 📊
   - [Veri Kaynağı ve Toplama Süreci](#veri-kaynağı-ve-toplama-süreci)
   - [Veri Setinin Genel Yapısı](#veri-setinin-genel-yapısı)
   - [Veri Setinin İçeriği](#veri-setinin-içeriği)

3. [**Keşifsel Veri Analizi (EDA)**](#keşifsel-veri-analizi-eda) 🔍
   - [Verinin Genel Özellikleri ve İlk İncelemeler](#verinin-genel-özellikleri-ve-ilk-incelemeler)
   - [Veri Görselleştirme ve Öne Çıkan Bulgular](#veri-görselleştirme-ve-öne-çıkan-bulgular)
   - [Firma İsimleri ve İlişkili Duygusal Analizler](#firma-isimleri-ve-ilişkili-duygusal-analizler)

4. [**Firma İsimlerinin Tespiti**](#firma-isimlerinin-tespiti) 🏢
   - [Varlık Adı Tanıma (NER) Modeli ile Firma İsimlerinin Belirlenmesi](#varlık-adı-tanıma-ner-modeli-ile-firma-isimlerinin-belirlenmesi)
   - [Modelin Eğitimi ve Değerlendirilmesi](#modelin-eğitimi-ve-değerlendirilmesi)
   - [Elde Edilen Sonuçların Doğruluğu ve Hassasiyeti](#elde-edilen-sonuçların-doğruluğu-ve-hassasiyeti)

5. [**Duygu Analizi**](#duygu-analizi) 😊😡
   - [Duygu Analizi Yöntemleri ve Kullanılan Model](#duygu-analizi-yöntemleri-ve-kullanılan-model)
   - [Metin İçerisinde Firma İsimlerine Atfedilen Duyguların Tespiti](#metin-içerisinde-firma-isimlerine-atfedilen-duyguların-tespiti)
   - [Duygu Dağılımının ve Sonuçların Görselleştirilmesi](#duygu-dağılımının-ve-sonuçların-görselleştirilmesi)

6. [**Veri Ön İşleme Süreci ve Kararlarımız**](#veri-ön-işleme-süreci-ve-kararlarımız) 🧹

7. [**Model Geliştirme**](#model-geliştirme) 🤖
   - [Kullanılan NER ve ABSA Modellerinin Detayları](#kullanılan-ner-ve-absa-modellerinin-detayları)
   - [Model Eğitim Süreci ve Hiperparametre Ayarları](#model-eğitim-süreci-ve-hiperparametre-ayarları)
   - [Modelin Performansının Değerlendirilmesi](#modelin-performansının-değerlendirilmesi)

8. [**Sonuçlar ve Analiz**](#sonuçlar-ve-analiz) 📈
   - [NER Modeli Performans Metrikleri](#ner-modeli-performans-metrikleri)
   - [ABSA Modeli Performans Metrikleri](#absa-modeli-performans-metrikleri)
   - [En Başarılı Modellerin Confusion Matrix ve ROC Eğrisi](#en-başarılı-modellerin-confusion-matrix-ve-roc-eğrisi)

9. [**Sonuç ve Gelecek Çalışmalar**](#sonuç-ve-gelecek-çalışmalar) 🚀
   - [Projenin Sonuçları ve Genel Değerlendirme](#projenin-sonuçları-ve-genel-değerlendirme)
   - [Gelecekteki İyileştirme Alanları ve Öneriler](#gelecekteki-iyileştirme-alanları-ve-öneriler)
   - [TDDi'ye Katkısı](#tddi-ye-katkısı)

10. [**Referanslar**](#referanslar) 📚

11. [**Bağımlılıklar (Dependencies)**](#bağımlılıklar-dependencies) 🛠️
    - [Projenin Çalışması İçin Gerekli Olan Python Paketleri](#projenin-çalışması-için-gerekli-olan-python-paketleri)
    - [Ortam Kurulumu ve Kullanım Talimatları](#ortam-kurulumu-ve-kullanım-talimatları)

<div align="center">
    <a href="your-call-to-action-link" style="background-color:#4CAF50; color:white; padding:10px 20px; text-align:center; text-decoration:none; display:inline-block; border-radius:5px;">Başlamak İçin Tıklayın</a>
</div>

<div align="center">
    <h1>Dökümantasyon</h1>
</div>

## Proje ve Ekip Tanıtımı

### Ekip Tanıtımı
Proje ekibi, Fırat Üniversitesi Yazılım Mühendisliği ve Bilgisayar Mühendisliği öğrencilerinden oluşmaktadır. Ekibimizi daha yakından tanımak için ekip tanıtım dosyamıza şuradan ulaşabilirsiniz. Ekip üyelerimiz:

- Murat Aydoğan (Danışman)
- Muhammed Talha Bıçak (Kaptan)
- Mustafa Utku Akbay
- Uğur Şahin
- Büşra Erdem

### Projenin Kapsamı ve Hedefleri
Bu proje, Teknofest Türkçe Doğal Dil İşleme yarışması için geliştirilmiştir ve Türkçe dilinde metin analizi yapmak amacıyla tasarlanmıştır. Proje, Türkçe dilinin yapısal ve anlamsal özelliklerine uygun olarak firma isimlerini tespit etmek ve bu firmalara atfedilen duygu tonlarını belirlemek için tasarlanmıştır.

**Kapsam:** Projenin kapsamı, Türkçe dilinde yazılmış çeşitli metin türlerinden oluşan geniş bir veri setinin analizini içerir. Bu metinler arasında sosyal medya paylaşımları, haber makaleleri, müşteri yorumları, blog yazıları ve proje ekibimizin ürettiği kaynaklar bulunmaktadır. Proje, Türkçe dilinde doğal dil işleme uygulamaları için önemli bir katkı sağlama ve Türkçe metinlerde firma adlarının ve duygu ifadelerinin doğru bir şekilde tanımlanmasını amaçlar.

**Hedefler:**
- **Varlık Tanıma:** Türkçe metinlerde geçen firma isimlerini yüksek doğrulukla tespit etmek ve kategorize etmek.
- **Duygu Analizi:** Her bir firma ismine atfedilen pozitif, negatif veya nötr duygu tonlarını belirlemek.
- **Türkçe NLP Alanına Katkı:** Türkçe dilinde doğal dil işleme tekniklerinin geliştirilmesi ve bu alanda yapılan çalışmalara katkıda bulunmak.
- **Eğitim ve Yaygınlaştırma:** Proje çıktılarının eğitim amaçlı kullanılabilirliğini sağlamak.
- **Gelecekteki Uygulamalar:** Elde edilen bulguların, Türkçe dilinde hizmet veren firmaların pazar algısını, müşteri geri bildirimlerini ve sosyal medya stratejilerini analiz etmelerinde kullanılabilmesi.

### Kullanılan Teknikler ve Yöntemler
Bu projede, doğal dil işleme alanındaki ileri düzey teknikler ve yöntemler kullanılarak, Türkçe dilinde yazılmış metinlerin analizi gerçekleştirilmiştir. Proje, derin öğrenme ve makine öğrenimi tekniklerinin yanı sıra, dilin yapısal özelliklerini dikkate alan özel NLP yöntemlerini de içermektedir.

- **Varlık Adı Tanıma (NER) Modeli:** Projede, metinlerde geçen firma isimlerini tanımlamak için gelişmiş Varlık Adı Tanıma (NER) modelleri kullanılmıştır. Bu modeller, BERT gibi önceden eğitilmiş dil modelleri temel alınarak özelleştirilmiş ve Türkçe diline uyarlanmıştır. NER modeli, metin içerisindeki belirli varlıkların (örneğin, şirket isimleri) doğru ve etkili bir şekilde tespit edilmesini sağlar.

- **Aspect-Based Sentiment Analysis (ABSA):** Firma isimlerine atfedilen duygu tonlarının belirlenmesi için, ABSA yöntemleri kullanılmıştır. Bu model, belirli bir firma veya konu hakkındaki pozitif, negatif veya nötr duyguları ayırt eder. ABSA modeli, metin içindeki belirli varlıklara (örneğin, şirket isimleri) ilişkin duygu ifadelerini tespit ederek, bu varlıkların algılanma biçimlerini analiz eder.

- **Keşifsel Veri Analizi (EDA):** Veri setinin genel özelliklerini anlamak ve öne çıkan bulguları belirlemek için keşifsel veri analizi yöntemleri kullanılmıştır. EDA, veri görselleştirme ve özet istatistikler gibi tekniklerle verinin yapısını, dağılımını ve öne çıkan desenleri incelemek için kullanılmıştır.

- **Doğal Dil İşleme Teknikleri:** Proje, doğal dil işleme alanındaki temel ve ileri düzey teknikleri kullanarak, Türkçe metinlerin doğru bir şekilde işlenmesini ve analiz edilmesini sağlar. Bu teknikler arasında kelime gömme (word embedding), metin ön işleme, dil modelleri ve duygu analizi gibi yöntemler bulunmaktadır.
