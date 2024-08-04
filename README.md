![NLPhoenix Logo](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/NLPhoenix.png)

<div align="left">
    <h1>İçerik</h1>
</div>

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


5. **Duygu Analizi**
   - **Duygu Analizi Yöntemleri ve Kullanılan Model**
     - Projemizin duygu analizi kısmında, metinlerdeki ince duygusal nüansları yakalamak ve firma isimlerine atfedilen duyguları yüksek doğrulukla belirlemek için en gelişmiş Aspect-Based Sentiment Analysis (ABSA) yöntemleri kullanılmıştır. Bu görevde, Transformer tabanlı modellerin gücünden yararlanılmış ve kapsamlı bir ön eğitim sürecinden geçirilmiş özel bir T5 modeli kullanılmıştır. T5, çok katmanlı dikkat mekanizmaları sayesinde, cümlelerin bağlamını derinlemesine anlayarak, metin içindeki belirli varlıkların etrafındaki duygusal ifadeleri ayırt etme yeteneğine sahiptir.

   - **Metin İçerisinde Firma İsimlerine Atfedilen Duyguların Tespiti**
     - Duygu analizi süreci, geniş bir veri yelpazesi üzerinden gerçekleştirilmiş ve her bir metin parçasında belirtilen firma isimlerine yönelik duyguların tespit edilmesi hedeflenmiştir. Bu süreçte, olumlu, olumsuz ve nötr duygular dikkatlice sınıflandırılmıştır. Proje ekibi olarak, eğitim veri setini özenle etiketledik ve modelin, Türkçe dilinde özgün ve karmaşık duygu ifadelerini başarılı bir şekilde algılamasını sağladık. Örneğin, "X firması, müşteri hizmetlerinde olağanüstü bir deneyim sundu." cümlesinde, 'olağanüstü' kelimesi sıfat olarak tanımlanması aracılığıyla model, pozitif bir duygu olduğuna dair bir önsezi sunulmuştur. Bu gibi ayrıntılı analizler, Türkçe metinlerdeki duygusal tonların incelikle anlaşılmasını mümkün kılmıştır.

   - **Duygu Dağılımının ve Sonuçların Görselleştirilmesi**
     - Elde edilen sonuçlar, verimli bir şekilde analiz edilip, detaylı bir görselleştirme sürecine tabi tutulmuştur. Bu aşamada, firma bazında pozitif, negatif ve nötr duyguların dağılımı grafikler ve interaktif tablolar aracılığıyla görselleştirilmiştir. Görselleştirme araçları, kullanıcıların metin içeriğine ilişkin genel duygusal eğilimleri hızlı ve kolay bir şekilde anlamalarına yardımcı olmuştur. Bu sayede, firmaların kamuoyundaki algısını izlemek ve stratejik kararlar almak için değerli içgörüler sunulmuştur.

6. **Veri Ön İşleme Aşamaları**
   - **Tokenizasyon**
     - Bu projede, Türkçe diline özgü yapıları dikkate alarak, metinler tokenizasyon işlemine tabi tutulmuştur. Bu işlem, cümleleri kelime veya alt-kelime düzeyinde parçalara ayırarak her bir bileşeni ayrı bir token olarak işlemeye olanak tanır. Böylece, modellerin dilin anlam ve bağlamını daha iyi kavraması sağlanır. Tokenizasyon sürecinde, dilin morfolojik zenginliği ve eklerin ayrımı özenle gerçekleştirilmiştir.

   - **Özel Karakterlerin ve Noktalama İşaretlerinin Kaldırılması**
     - Metin analizinde gereksiz gürültüyü azaltmak için özel karakterleri ve noktalama işaretlerini temizlendi. Bu süreçte, Türkçe diline özgü karakterlerin korunmasına özen gösterilirken, metinlerin anlamını bozmayan ancak analiz açısından gereksiz olan tüm özel karakterler ve noktalama işaretleri çıkarılmıştır. Örneğin, noktalama işaretleri (nokta hariç) ve özel semboller (&, #, %, vb.) temizlenmiş, bu sayede veri seti daha saf ve odaklanmış bir hale getirilmiştir.

   - **Veri Temizliği**
     - Veri temizliği, ham verilerin analiz için uygun hale getirilmesi amacıyla gerçekleştirildi. Bu adımda, metinlerde bulunan gereksiz boşluklar, HTML etiketleri, URL'ler ve diğer alakasız bilgiler titizlikle temizlenmiştir. Gereksiz boşlukların kaldırılması, metinlerin düzenlenmesini ve tokenizasyon sürecinin doğruluğunu artırır. HTML etiketleri ve URL'ler gibi unsurların temizlenmesi, metinlerin anlam kaymasına yol açabilecek yanıltıcı bilgilerin ayıklanmasını sağlar. Ayrıca, spam içeriği veya anlamsız veri parçaları gibi potansiyel gürültü kaynakları da ortadan kaldırılmıştır. Bu dikkatli temizlik işlemi, modellerin doğru ve tutarlı sonuçlar üretmesine katkıda bulunmuştur.

Bu ön işleme adımları, hem NER hem de ABSA modellerinin doğruluk ve verimliliğini maksimize etmeye yönelik titiz bir hazırlık sürecini ifade eder. Bu kısımda bahsedilmeyen diğer ön işleme adımları ise uygulandıktan sonra model doğruluk değerlerinde düşüş yaşanması sebebiyle kullanılmamış daha çok verimliliğe odaklanılmıştır.

9. **Model Geliştirme**
   - **Kullanılan NER ve ABSA Modellerinin Detayları**
     - **NER (Varlık Adı Tanıma) Modeli:**
       - Bu projede, firma isimlerinin doğru ve hassas bir şekilde tanınabilmesi için savasy/bert-base-turkish-ner-cased modeli kullanılmıştır. Bu model, Türkçe dilinin yapısal özelliklerini dikkate alarak eğitilmiş olup, isim tanıma görevlerinde üstün performans sergilemektedir. Modelin güçlü dil anlayışı ve bağlam duyarlılığı, metinlerdeki firma isimlerini yüksek doğrulukla tanımasına olanak tanır.
     - **ABSA (Aspect-Based Sentiment Analysis) Modeli:**
       - Metinlerde firma isimlerine atfedilen duyguların belirlenmesi için dbmdz/bert-base-turkish-cased modeli tercih edilmiştir. Bu model, Türkçe metinlerde duygusal tonları ve bağlamı anlamada yüksek başarı gösterir. Modelin esnek yapısı ve derin öğrenme yetenekleri, firma isimleri etrafındaki duygusal ifadeleri etkili bir şekilde sınıflandırmasını sağlar.

   - **Model Eğitim Süreci ve Hiperparametre Ayarları**
     - **NER Modeli Eğitimi:**
       - savasy/bert-base-turkish-ner-cased modeli, yaklaşık 130,000 firma isimleri ile ilgili veri seti kullanılarak ince ayar yapılmıştır (finetuning). Eğitim süreci boyunca, modelin öğrenme oranı, batch boyutu, epoch sayısı gibi hiperparametreler özenle ayarlanmıştır. Özellikle, 3e-5 öğrenme oranı, 32 batch boyutu ve 5 epoch, modelin optimum performansı yakalamasında etkili olmuştur. Model, geniş ve çeşitli veri seti sayesinde, farklı sektörlerden gelen firma isimlerini doğru bir şekilde tanımak üzere eğitilmiştir.
     - **ABSA Modeli Eğitimi:**
       - dbmdz/bert-base-turkish-cased modeli, yaklaşık 120,000 veri ile eğitilmiştir. Bu süreçte, modelin duygusal bağlamları anlaması için çeşitli duygusal ifadeler içeren geniş bir veri seti kullanılmıştır. Eğitim sırasında, öğrenme oranı 2e-5, batch boyutu 16 ve 4 epoch kullanılmıştır. Hiperparametrelerin bu şekilde ayarlanması, modelin hem eğitim sürecinde hem de genel performansında yüksek verimlilik sağlamıştır.

   - **Modelin Performansının Değerlendirilmesi**
     - Eğitim süreçlerinin ardından, modellerin performansı kapsamlı bir şekilde değerlendirilmiştir. Performans değerlendirmesi, doğruluk (accuracy), hassasiyet (precision), geri çağırma (recall) ve F1 skoru gibi temel metrikler üzerinden gerçekleştirilmiştir.
     - **NER Modeli Performansı:**
       - savasy/bert-base-turkish-ner-cased modeli, test verileri üzerinde %95'in üzerinde doğruluk ve %93 hassasiyet ile üstün bir performans sergilemiştir. Geri çağırma oranı %92 ve F1 skoru %92.5 olan model, firma isimlerini tanımada yüksek doğruluk sağlamıştır.
     - **ABSA Modeli Performansı:**
       - dbmdz/bert-base-turkish-cased modeli, duygu analizi görevlerinde %90 doğruluk, %88 hassasiyet ve %87 geri çağırma oranı ile başarılı sonuçlar elde etmiştir. F1 skoru %87.5 olan model, metinlerdeki firma isimlerine atfedilen duyguları doğru bir şekilde sınıflandırabilmiştir.


10. **Sonuç ve Gelecek Çalışmalar**
   - **Ek Veri Kaynaklarının Kullanımı**
     - Projenin başarısını artırmak amacıyla, ek veri kaynakları üzerinde çalışmalar gerçekleştirilmiştir. İlk aşamada, semantik veri üretimi denemeleri yapılmış, ancak elde edilen sonuçlar beklenen düzeyde başarılı olmamıştır. Bu yöntem, özellikle metinlerin bağlamsal anlamını doğru bir şekilde modelleyemediği için firmalara yönelik duygu ifadelerinde istenilen doğruluğu sağlayamamıştır.

     - Bir diğer strateji olarak, yabancı dillerdeki veri setlerinin Türkçeye çevrilmesi yöntemi uygulanmıştır. Ancak, bu yaklaşım ABSA modeli üzerinde istenmeyen sonuçlar doğurmuş, özellikle metinlerdeki herhangi bir ifadeyi bir firmaya yönlendirme konusunda olumsuz etkiler gözlemlenmiştir. Dil çevirisi sırasında, bağlam kaybı ve anlam kaymaları gibi problemler ortaya çıkmış, bu da modelin performansını olumsuz yönde etkilemiştir.

     - Bununla birlikte, veri setini genişletmek için kelimelerin eş anlamlılarını kullanarak veri artırımı (data augmentation) yöntemi büyük başarı sağlamıştır. Synonym Replacement (Eş Anlamlı Kelime Değiştirme) adı verilen bu teknik, mevcut veri setindeki cümlelerin farklı varyasyonlarını oluşturarak, modelin daha geniş bir veri kümesinde eğitilmesine olanak tanımıştır. Bu yöntem, hem NER hem de ABSA modellerinin daha sağlam ve genelleştirilebilir olmasını sağlamış, model performansını önemli ölçüde artırmıştır.

   - **Model Geliştirmeleri ve Denemeler**
     - Proje kapsamında, çeşitli modern dil modelleri değerlendirilmiş ve geliştirilmiştir. DistilBERT, RoBERTa, BERTürk ve T5 gibi popüler Transformer tabanlı modeller üzerinde deneyler yapılmıştır. Her bir modelin performansı, eğitim veri seti üzerinde fine-tuning süreciyle optimize edilmiştir. Elde edilen sonuçlar, her modelin Türkçe metinler üzerindeki etkinliğini ortaya koymuş ve performans metrikleri açısından karşılaştırılmıştır. Sonuçlar, repoda ayrıntılı bir şekilde paylaşılmıştır ve bu modellerin yeteneklerini detaylı olarak analiz eden değerlendirme raporları içermektedir.

   - **İyileştirme Sonuçlarının Karşılaştırılması**
     - Yapılan iyileştirmeler ve denemeler sonucunda, çeşitli modellerin performansları karşılaştırmalı olarak analiz edilmiştir. Bu karşılaştırmalar, modellerin doğruluk, F1 skoru, hassasiyet ve geri çağırma gibi metrikler üzerinden yapılmıştır. Özellikle, synonym replacement(Eş Anlamlı Kelime Değiştirme) yönteminin uygulanması sonrası modellerde gözlemlenen performans artışı, karşılaştırma da detaylı olarak ele alınmıştır.

Bu çalışmalar sonucunda, proje kapsamında Türkçe metinlerde firma isimlerini tanıma ve bu isimlere yönelik duygusal ifadeleri belirleme konusunda güçlü bir altyapı oluşturulmuştur. Gelecek çalışmalarda, daha büyük ve çeşitlendirilmiş veri setleri ile model eğitiminin devam ettirilmesi, model performansını daha da artırabilir.
