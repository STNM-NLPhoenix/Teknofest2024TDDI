# İçerik

1. **Proje ve Ekip Tanıtımı**
   - Ekip Tanıtımı
   - Projenin Kapsamı ve Hedefleri
   - Kullanılan Teknikler ve Yöntemler

3. **Veri Kümesi**
   - Veri Kaynağı ve Toplama Süreci
   - Veri Setinin Genel Yapısı
   - Veri Setinin İçeriği

4. **Keşifsel Veri Analizi (EDA)**
   - Verinin Genel Özellikleri ve İlk İncelemeler
   - Veri Görselleştirme ve Öne Çıkan Bulgular
   - Firma İsimleri ve İlişkili Duygusal Analizler

5. **Firma İsimlerinin Tespiti**
   - Varlık Adı Tanıma (NER) Modeli ile Firma İsimlerinin Belirlenmesi
   - Modelin Eğitimi ve Değerlendirilmesi
   - Elde Edilen Sonuçların Doğruluğu ve Hassasiyeti

6. **Duygu Analizi**
   - Duygu Analizi Yöntemleri ve Kullanılan Model
   - Metin İçerisinde Firma İsimlerine Atfedilen Duyguların Tespiti
   - Duygu Dağılımının ve Sonuçların Görselleştirilmesi

7. **Veri Ön İşleme Aşamaları**
   - Metin Temizleme ve Normalizasyon
   - Stop Word'lerin Çıkarılması ve Lemmatizasyon

8. **Model Geliştirme**
   - Kullanılan NER ve ABSA Modellerinin Detayları
   - Model Eğitim Süreci ve Hiperparametre Ayarları
   - Modelin Performansının Değerlendirilmesi

10. **Sonuç ve Gelecek Çalışmalar**
    - Ek Veri Kaynaklarının Kullanımı
    - Model Geliştirmeleri ve Denemeler
    - İyileştirme Sonuçlarının Karşılaştırılması

9. **Sonuçlar ve Analiz**
   - NER Modeli Performans Metrikleri
   - ABSA Modeli Performans Metrikleri
   - En Başarılı Modellerin Confusion Matrix ve ROC Eğrisi

10. **Sonuç ve Gelecek Çalışmalar**
    - Projenin Sonuçları ve Genel Değerlendirme
    - Gelecekteki İyileştirme Alanları ve Öneriler
    - TDDi'ye katkısı

11. **Referanslar**
    - Kullanılan Kaynaklar ve Akademik Çalışmalar
    - Kullanılan Kütüphaneler ve Araçlar


13. **Bağımlılıklar (Dependencies)**
    - Projenin Çalışması İçin Gerekli Olan Python Paketleri
    - Ortam Kurulumu ve Kullanım Talimatları

<div align="center">
    <h1>Dökümantasyon</h1>
</div>

1. **Proje ve Ekip Tanıtımı**
   - **Ekip Tanıtımı**
     - Proje ekibi, Fırat Üniversitesi Yazılım Mühendisliği ve Bilgisayar Mühendisliği öğrencilerinden oluşmaktadır. Ekibimizi daha yakından tanımak için ekip tanıtım dosyamıza şuradan ulaşabilirsiniz.

   - **Projenin Kapsamı ve Hedefleri**
      - Bu proje, Teknofest Türkçe Doğal Dil İşleme yarışması için geliştirilmiştir ve Türkçe dilinde metin analizi yapmak amacıyla tasarlanmıştır. Proje, Türkçe dilinin yapısal ve anlamsal özelliklerine uygun olarak firma isimlerini tespit etmek ve bu firmalara atfedilen duygu tonlarını belirlemek için NER ve ABSA modellerini kullanmaktadır.
     
     - **Kapsam:** Projenin kapsamı, Türkçe dilinde yazılmış çeşitli metin türlerinden oluşan geniş bir veri setinin analizini içerir. Bu metinler arasında sosyal medya paylaşımları, haber makaleleri, müşteri yorumları ve blog yazıları gibi kaynaklar bulunmaktadır. Proje, Türkçe dilinde doğal dil işleme uygulamaları için önemli bir katkı sağlama ve Türkçe metinlerde firma adlarının ve duygu ifadelerinin doğru bir şekilde tanımlanmasını amaçlar.

     - **Hedefler:**
       - **Varlık Tanıma:** Türkçe metinlerde geçen firma isimlerini yüksek doğrulukla tespit etmek ve kategorize etmek.
       - **Duygu Analizi:** Her bir firma ismine atfedilen olumlu, olumsuz veya nötr duygu tonlarını belirlemek.
       - **Türkçe NLP Alanına Katkı:** Türkçe dilinde doğal dil işleme tekniklerinin geliştirilmesi ve bu alanda yapılan çalışmalara katkıda bulunmak.
       - **Eğitim ve Yaygınlaştırma:** Proje çıktılarının eğitim amaçlı kullanılabilirliğini sağlamak.
       - **Gelecekteki Uygulamalar:** Elde edilen bulguların, Türkçe dilinde hizmet veren firmaların pazar algısını, müşteri geri bildirimlerini ve sosyal medya stratejilerini analiz etmelerinde kullanılabilmesi.

   - **Kullanılan Teknikler ve Yöntemler**
      - Bu projede, doğal dil işleme alanındaki ileri teknikler ve yöntemler kullanılarak, Türkçe dilinde yazılmış metinlerin analizi gerçekleştirilmiştir. Proje, derin öğrenme ve makine öğrenimi tekniklerinin yanı sıra, dilin yapısal özelliklerini dikkate alan özel NLP yöntemlerini de içermektedir.

      - **Varlık Adı Tanıma (NER) Modeli:** Projede, metinlerde geçen firma isimlerini tanımlamak için gelişmiş Varlık Adı Tanıma (NER) modelleri kullanılmıştır. Bu modeller, BERT gibi önceden eğitilmiş dil modelleri temel alınarak özelleştirilmiş ve Türkçe diline uyarlanmıştır. NER modeli, metin içerisindeki belirli varlıkların (örneğin, şirket isimleri) doğru ve etkili bir şekilde tespit edilmesini sağlar.

     - **Aspect-Based Sentiment Analysis (ABSA):** Firma isimlerine atfedilen duygu tonlarının belirlenmesi için, ABSA yöntemleri kullanılmıştır. Bu model, belirli bir firma veya konu hakkındaki olumlu, olumsuz veya nötr duyguları ayırt eder. ABSA, cümle düzeyinde duygu tespiti yaparken, çeşitli dil özelliklerini ve metnin bağlamını göz önünde bulundurur. Transformer tabanlı modeller, Türkçe dilinin nüanslarını yakalamak ve yüksek doğrulukta sonuçlar elde etmek için kullanılmıştır.

     - **Veri Ön İşleme ve Temizleme:** Proje kapsamında, ham verilerin analiz için uygun hale getirilmesi amacıyla kapsamlı bir veri ön işleme süreci uygulanmıştır. Bu süreç, metin verilerinin temizlenmesi, normalizasyonu ve tokenizasyon gibi adımları içerir. Ayrıca, Türkçe diline özgü stop word'lerin çıkarılması ve özel karakterlerin işlenmesi gibi işlemler için de analizler yapılmıştır ilerleyen satırlarda bu konu hakkında daha ayrıntılı bilgilendirme yapacağız.

     - **Model Eğitimi ve Değerlendirme:** Modellerin eğitimi sırasında, büyük ölçekli veri setlerinden yararlanılmış ve hiperparametre optimizasyonu yapılmıştır. Model performansı, çeşitli metrikler (örneğin, doğruluk, precision, recall, F1 skoru) kullanılarak değerlendirilmiş ve iyileştirilmiştir. Ayrıca, çapraz doğrulama yöntemleri ile modelin genelleştirme yeteneği test edilmiştir.

     - **API Entegrasyonu ve Arayüz:** Elde edilen sonuçların kullanıcı dostu bir şekilde sunulabilmesi için API entegrasyonu gerçekleştirilmiş ve kullanıcı dostu bir arayüz geliştirilmiştir. Bu arayüz, kullanıcıların metin verilerini kolayca analiz edebilmesini ve sonuçları görselleştirebilmesini sağlar. Geliştirilen API, metin analizi süreçlerini otomatikleştirir ve kullanıcıların ihtiyaçlarına göre özelleştirilebilir.




4. **Firma İsimlerinin Tespiti**
   - **Varlık Adı Tanıma (NER) Modeli ile Firma İsimlerinin Belirlenmesi**
     - Bu projede, Türkçe metinlerde geçen firma isimlerinin doğru ve etkili bir şekilde tespit edilmesi amacıyla, modern Varlık Adı Tanıma (NER) modelleri kullanılmıştır. Deneysel aşamada, RoBERTa, BERTürk, DistilBERT ve T5 gibi önde gelen dil modelleri değerlendirilmiştir. Model seçimi sürecinde, farklı modellerin performansları karşılaştırılmış ve en iyi sonuçların T5 modeli ile elde edildiği gözlemlenmiştir. T5'in güçlü dil anlayışı ve esnek yapısı, Türkçe metinlerde firma isimlerinin tespiti için üstün bir performans sergilemiştir.

   - **Modelin Eğitimi ve Değerlendirilmesi**
     - T5 modeli, geniş ve çeşitli bir veri kümesi kullanılarak eğitilmiştir. Eğitim süreci, yaklaşık 120 bin etiketlenmiş veri örneği üzerinde gerçekleştirilmiştir. Bu veri seti, farklı sektörlerden ve kaynaklardan toplanan metinleri içermekte olup, modelin geniş bir yelpazede firma isimlerini tanıyabilmesini sağlamıştır. Eğitim sürecinde, veri ön işleme adımları dikkatle uygulanmış, veri temizliği ve normalizasyon gibi işlemler titizlikle gerçekleştirilmiştir. Modelin eğitimi sırasında, hiperparametre optimizasyonu yapılarak modelin doğruluğu ve genelleme yeteneği artırılmıştır.

   - **Elde Edilen Sonuçların Doğruluğu ve Hassasiyeti**
     - Eğitim süreci sonrasında, T5 modelinin performansı kapsamlı bir şekilde değerlendirilmiştir. Doğruluk (accuracy), hassasiyet (precision), geri çağırma (recall) ve F1 skoru gibi performans metrikleri kullanılarak modelin başarımı ölçülmüştür. Sonuçlar, modelin firma isimlerini yüksek doğrulukla tanıyabildiğini ve düşük hata oranlarıyla etkili bir şekilde sınıflandırma yapabildiğini göstermiştir. Özellikle, modelin Türkçe dilinin yapısal özelliklerini ve nüanslarını anlamadaki başarısı, projenin hedeflerine ulaşmasında kritik bir rol oynamıştır.
