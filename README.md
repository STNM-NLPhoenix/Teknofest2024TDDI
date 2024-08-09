![NLPhoenix Logo](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/img/NLPhoenix.png)

## 📜 İçerik

1. [**Proje ve Ekip Tanıtımı**](#1-proje-ve-ekip-tanıtımı) 📋
   - [Ekip Tanıtımı](#ekip-tanıtımı)
   - [Projenin Kapsamı ve Hedefleri](#projenin-kapsamı-ve-hedefleri)
   - [Kullanılan Teknikler ve Yöntemler](#kullanılan-teknikler-ve-yöntemler)

2. [**Veri Kümesi**](#2-veri-kümesi) 📊
   - [Veri Kaynağı ve Toplama Süreci](#veri-kaynağı-ve-toplama-süreci)
   - [Veri Setinin Genel Yapısı](#veri-setinin-genel-yapısı)

3. [**Keşifsel Veri Analizi (EDA)**](#3-keşifsel-veri-analizi-eda) 🔍
   - [Verinin Genel Özellikleri ve İlk İncelemeler](#verinin-genel-özellikleri-ve-ilk-incelemeler)
   - [Veri Görselleştirme ve Öne Çıkan Bulgular](#veri-görselleştirme-ve-öne-çıkan-bulgular)
   - [Firma İsimleri ve İlişkili Duygusal Analizler](#firma-isimleri-ve-ilişkili-duygusal-analizler)

4. [**Firma İsimlerinin Tespiti**](#4-firma-isimlerinin-tespiti) 🏢
   - [Varlık Adı Tanıma (NER) Modeli ile Firma İsimlerinin Belirlenmesi](#varlık-adı-tanıma-ner-modeli-ile-firma-isimlerinin-belirlenmesi)
   - [Modelin Eğitimi ve Değerlendirilmesi](#modelin-eğitimi-ve-değerlendirilmesi)
   - [Elde Edilen Sonuçların Doğruluğu ve Hassasiyeti](#elde-edilen-sonuçların-doğruluğu-ve-hassasiyeti)

5. [**Duygu Analizi**](#5-duygu-analizi) 😊😡
   - [Duygu Analizi Yöntemleri ve Kullanılan Model](#duygu-analizi-yöntemleri-ve-kullanılan-model)
   - [Metin İçerisinde Firma İsimlerine Atfedilen Duyguların Tespiti](#metin-içerisinde-firma-isimlerine-atfedilen-duyguların-tespiti)
   - [Duygu Dağılımının ve Sonuçların Görselleştirilmesi](#duygu-dağılımının-ve-sonuçların-görselleştirilmesi)

6. [**Veri Ön İşleme Süreci ve Kararlarımız**](#6-veri-ön-işleme-süreci-ve-kararlarımız) 🧹

7. [**Sonuçlar ve Analiz**](#7-sonuçlar-ve-analiz) 📈
   - [NER Modeli Performans Metrikleri](#ner-modeli-performans-metrikleri)
   - [ABSA Modeli Performans Metrikleri](#absa-modeli-performans-metrikleri)
   - [Kullanılan NER ve ABSA Modellerinin Detayları](#kullanılan-ner-ve-absa-modellerinin-detayları)
   - [NER (Varlık Adı Tanıma) Modeli](#ner--varlık-adı-tanıma-modeli)
   - [ABSA (Aspect-Based Sentiment Analysis) Modeli](#absa-aspect-based-sentiment-analysis-modeli)
   - [Model Eğitim Süreci ve Hiperparametre Ayarları](#model-eğitim-süreci-ve-hiperparametre-ayarları)
   - [Modelin Performansının Değerlendirilmesi](#modelin-performansının-değerlendirilmesi)
   - [NER Modeli Performansı](#ner-modeli-performansı)
   - [Analiz ve Sonuçlar](#analiz-ve-sonuçlar)

   
8. [**Arayüz ve API Entegrasyonu**](#8-arayuz-ve-api-entegrasyonu)

9. [**Sonuç ve Gelecek Çalışmalar**](#9-sonuç-ve-gelecek-çalışmalar) 🚀
   - [Projenin Sonuçları ve Genel Değerlendirme](#projenin-sonuçları-ve-genel-değerlendirme)
   - [Gelecekteki İyileştirme Alanları ve Öneriler](#gelecekteki-iyileştirme-alanları-ve-öneriler)
   - [TDDi'ye Katkısı](#tddiye-katkısı)

10. [**Referanslar**](#10-referanslar) 📚

11. [**Bağımlılıklar**](#11-bağımlılıklar) 🛠️

<div align="center">
    <h1>Dökümantasyon</h1>
</div>
<br><br>

## 1. Proje ve Ekip Tanıtımı

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

- **Aspect-Based Sentiment Analysis (ABSA):** Firma isimlerine atfedilen duygu tonlarının belirlenmesi için, ABSA yöntemleri kullanılmıştır. Bu model, belirli bir firma veya konu hakkındaki duygusal tonları (pozitif, negatif, nötr) belirlemeye yönelik özelleştirilmiştir. ABSA, belirli bir metindeki duygu durumlarını daha detaylı ve ince bir şekilde analiz ederek, firma algısını ve müşteri geri bildirimlerini anlamada önemli bir rol oynar.

- **Veri Ön İşleme ve Temizleme:** Verilerin doğruluğunu ve kalitesini artırmak için kapsamlı veri ön işleme ve temizleme işlemleri uygulanmıştır. Bu işlemler, metinlerdeki gereksiz bilgilerin temizlenmesi, özel karakterlerin ve duraklamaların (stopwords) çıkarılması, yazım hatalarının düzeltilmesi ve metinlerin dil bilgisi kurallarına uygun hale getirilmesi gibi adımları içerir.

- **Makine Öğrenimi ve Derin Öğrenme Teknikleri:** Projede, makine öğrenimi ve derin öğrenme teknikleri kullanılarak, metinlerin analizi ve sınıflandırılması gerçekleştirilmiştir. Bu teknikler, metin verilerinin özelliklerinin çıkarılması, örüntülerin tespit edilmesi ve sınıflandırma işlemlerinde yüksek doğruluk ve performans sağlar.

- **Veri Görselleştirme ve Analiz:** Elde edilen sonuçların daha iyi anlaşılabilir ve yorumlanabilir hale getirilmesi için, veri görselleştirme teknikleri kullanılmıştır. Grafikler, tablolar ve diğer görsel araçlar, metin analizlerinin sonuçlarını daha etkili bir şekilde sunar ve önemli bulguların öne çıkmasını sağlar.

Bu teknikler ve yöntemler, projenin başarılı bir şekilde gerçekleştirilmesi ve hedeflerine ulaşması için önemli katkılar sağlamıştır. Projenin çıktıları, Türkçe dilinde doğal dil işleme alanındaki araştırmalara ve uygulamalara değerli bir katkı sunmaktadır.

## 2. Veri Kümesi

### Veri Kaynağı ve Toplama Süreci
Modelimizi geliştirirken iki farklı veri kümesi kullandık. İlk veri kümesi ABSA (Aspect-Based Sentiment Analysis) veri kümesi olup müşteri yorumlarındaki görüşlerin ve hedef varlıkların saptanması için tasarlanmıştır. İkinci veri kümesi ise NER (Named Entity Recognition) veri kümesidir. Bu veri kümesi, metindeki firmaların tanınması ve sınıflandırılması için kullanılıyor. Veri setlerini oluştururken öncelikle modelimiz için gerekli doğru formatı belirledik. Yapay zeka araçlarını kullanarak belirlediğimiz formatta veri setini oluşturarak modelin gerçek performansını öğrenmeyi amaçladık.

### Veri Setinin Genel Yapısı

### ABSA (Aspect-Based Sentiment Analysis) Veri Kümesi
Bu veri kümesi, müşteri yorumlarındaki görüşlerin (sentiment) ve hedef varlıkların (entities) belirlenmesi amacıyla kullanılır. Her bir örnek, bir metin parçası ve bu metindeki varlıklar ile bu varlıkların duygusal yönelimlerini (pozitif, negatif, nötr) içerir. 
Örneğin, "Vodafone'un verdiği tanıtım faaliyetleri hayli avantajlı, lakin Turkcell'in servisleri hayli standart." cümlesinde "Vodafone" varlığı pozitif, "Turkcell" varlığı ise nötr olarak etiketlenmiştir. Bu veri kümesi, müşteri görüşlerinin analizi ve işletmelerin hizmetlerinin daha iyi anlaşılması için değerlidir.

Örneğin, aşağıdaki cümlede iki şirket ve bu şirketlerin duygusal yönelimleri belirtilmiştir:

            {
                "text": "Vodafone'un verdiği tanıtım faaliyetleri hayli avantajlı, lakin Turkcell'in servisleri hayli standart.",
                "entities": [
                    {
                        "entity": "Vodafone",
                        "sentiment": "positive"
                    },
                    {
                        "entity": "Turkcell",
                        "sentiment": "neutral"
                    }
                ]
            }
            
Bu örnekte, "Vodafone" varlığı pozitif, "Turkcell" varlığı ise nötr olarak etiketlenmiştir. 

### ABSA Veri Seti Formatı:

```
   {
        "text":"Turkcell'in ağ sürati çoğunlukla hoşnutluk sağlayıcı değil, Vodafone'un alıcı servisleri eğer pek çoğu vakit tesirsiz ile Türk Telekom'un data projeleri eğer ortalama.",
        "entities":[
            {
                "entity":"Turkcell",
                "sentiment":"negative"
            },
            {
                "entity":"Vodafone",
                "sentiment":"neutral"
            },
            {
                "entity":"Türk Telekom",
                "sentiment":"negative"
            }
        ]
    }
```
```
text: Analiz edilen yorumun tam metni.
entities: Yorumdaki şirketler ve bu şirketlerle ilişkili duyguların belirtildiği bir liste.

entity: Şirket adı.
sentiment: Şirketle ilişkili duygu (olumlu, olumsuz, nötr).

```
### NER (Named Entity Recognition) Veri Kümesi
NER veri kümesi, metindeki önemli varlıkların (firmalar) tanınması ve sınıflandırılması için kullanılır. Veri kümesinde her satır, bir kelime ve bu kelimenin entity tipini (B-organization, I-organization, O) içerir. Örneğin, "vodafone", "turk telekom" ve "türknet" gibi kuruluş adları B-organization veya I-organization olarak etiketlenmiştir.

### NER Veri Seti Formatı:

Özelleşmiş isterlere göre dizayn edilmiş organizasyon bazlı conLL formatında NER veri seti, her satırda bir kelime ve o kelimenin etiketini içerecek şekilde düzenlenmiştir. Bir cümle veya metin parçasının sonu boş bir satırla ayrılmıştır. Etiketler, organizasyon isimlerinin başlangıcını ("B-organization") ve devamını ("I-organization") belirtir.
```
B-organization: Bir organizasyon isminin başlangıcını belirtir.

I-organization: Organizasyon isminin devamını belirtir.

O: Organizasyon adı olmayan diğer kelimeleri belirtir.
```
| words     | label            |
|-----------|------------------|
| turk      | B-organization   |
| telekom   | I-organization   |
| musterileri| O                |
| hizmetleri| O                |
| kotu      | O                |
| olsa      | O                |
| da        | O                |
| turknet   | B-organization   |
| musterileri| O                |
| hizmetleri| O                |
| oldukca   | O                |
| ortalama  | O                |


Bu veri kümesinde "turk telekom" bir organizasyon adı olarak başlangıç ve devam etiketleriyle (B-organization, I-organization) belirtilmiş, diğer kelimeler ise organizasyon adı olmayan (O) kelimeler olarak etiketlenmiştir.


## 3. Keşifsel Veri Analizi (EDA)

### Verinin Genel Özellikleri ve İlk İncelemeler

Veri setinin genel özellikleri incelenmiş ve metinlerde geçen firma isimleri ile bu isimlere atfedilen duygu durumları analiz edilmiştir. İlk incelemeler, veri setindeki firma isimlerinin ve duygu durumlarının dağılımını ortaya koymuştur.
<br><br><br><br>
![NER Modeli Sınıf Dağılım Grafiği](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/img/NER_SinifDagilimiEski.png)
<br><br><br>
Bu grafikten elde ettiğimiz bulgular sayesinde hazırladığımız veri setinde O etiketi, organizasyon etiketlerine oranla çok daha fazla olduğunu görebiliyoruz. Bu sebepten ötürü veri setindeki organizasyon etiketlerinin toplamını O etiketine yaklaştırmayı hedefleyerek bu yönde bir çalışma yapılmıştır. Bu çalışmaların sonucu aşağıdaki grafikte görülmektedir.
<br><br><br>
![NER Modeli Sınıf Dağılım Grafiği](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/img/NER_SinifDagilimiDuzenlendi.png)
<br><br><br>

### Veri Görselleştirme ve Öne Çıkan Bulgular
Veri seti, çeşitli görselleştirme teknikleri kullanılarak analiz edilmiştir. Bu analizler, firma isimlerinin ve duygu durumlarının dağılımını görselleştirerek, öne çıkan bulguları ortaya koymuştur.

Aşağıdaki grafik, bir NER (Adlandırılmış Varlık Tanıma) veri setindeki kelime uzunluklarının dağılımını göstermektedir. Grafik, veri setindeki ortalama kelime uzunluklarını daha iyi anlayabilmek için tasarlanmıştır. Yatay eksende ortalama kelime uzunlukları, dikey eksende ise bu uzunlukların frekansları yer almaktadır. Görselde, kelime uzunluklarının büyük bir kısmının 4 ile 8 arasında yoğunlaştığı, 15'ten uzun kelimelerin ise oldukça nadir olduğu görülmektedir. Bu tür bir analiz, NER modellerinin kelime uzunluklarına göre performansını değerlendirmek veya veri setinin genel dil yapısını anlamak için kullanılabilir. Ek olarak, grafik üzerinde KDE (Kernel Yoğunluk Tahmini) çizgisi de bulunmaktadır; bu çizgi, kelime uzunluklarının yoğunluk dağılımını pürüzsüz bir şekilde göstermektedir. Özellikle, 5-7 karakter uzunluğundaki kelimelerin en yüksek frekansa sahip olduğu dikkat çekmektedir. Bu tür görselleştirmeler, dil işleme görevlerinde veri setinin yapısına dair kritik bilgiler sunar.
<br><br><br>
![NER Modeli Kelime Uzunluğu Grafiği](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/img/Ner_KelimeUzunlugu.png)
<br><br><br>
Aşağıdaki grafikte, veri setinde en sık geçen kelimelerin frekansları gösterilmektedir. Grafikte görüldüğü gibi, "ve", "bir", "ise", "genellikle" gibi bağlaçlar ve zarf fiiller en yüksek frekanslarla yer almaktadır. Bu kelimelerin sıklığı, veri setindeki genel dil yapısını ve kelime kullanım eğilimlerini anlamamıza olanak sağlar.

Veri setinde en sık kullanılan bu kelimeleri belirledikten sonra, bu kelimeler için Türkçe eş anlamlı sözcükler tespit edilmiştir. Örneğin, "ve" kelimesi yerine "ile", "ama" kelimesi yerine "fakat" gibi eş anlamlılar kullanılmıştır. Bu işlem, veri setindeki kelimelerin varyasyonlarını artırarak, veri setinin kapsamını genişletmeyi ve zenginleştirmeyi amaçlamaktadır.

Grafikteki kelimeler, veri setinin dil yapısını daha iyi anlamamıza yardımcı olurken, eş anlamlı sözcüklerle yapılan genişletme işlemi, doğal dil işleme (NLP) modellerinin performansını artırmak için daha çeşitli ve zengin bir veri seti oluşturmayı hedeflemektedir. Özellikle sık kullanılan kelimelerin eş anlamlılarının eklenmesi, modelin dilsel çeşitliliği daha iyi kavramasına ve farklı cümle yapılarını öğrenmesine katkı sağlamaktadır.

Bu sayede, veri setimizi büyük oranda büyüterek, doğal dil işleme modellerinin daha geniş bir kelime dağarcığı ile çalışmasını sağlamayı amaçladık.
<br><br><br>
![En Sık Kullanılan Kelimeler](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/img/NER_EnCokGecenler.png)
<br><br><br>

### Firma İsimleri ve İlişkili Duygusal Analizler

Aşağıdaki grafikte, ABSA (Aspect-Based Sentiment Analysis) veri setindeki firma isimlerine atfedilen duygusal tonların dağılımı, bir pasta grafiği aracılığıyla görselleştirilmiştir. Grafikte, verisetindeki yorumların %43,3'ünün pozitif, %29,5'inin negatif, ve %27,1'inin nötr olduğu görülmektedir. Bu grafik, firma algısını ve müşteri geri bildirimlerini anlamak adına önemli bir araç olarak kullanılabilir.

Firma isimlerine atfedilen bu duygusal tonların analizi, müşteri yorumlarının firma algısı üzerindeki etkisini değerlendirmede kritik bilgiler sunmaktadır. Örneğin, pozitif yorumların yüksek oranı, firmaların genel olarak olumlu bir algıya sahip olduğunu, ancak negatif yorumların da göz ardı edilemeyecek bir oranda olduğunu göstermektedir. Nötr yorumların ise, müşterilerin belirli bir konuda olumlu ya da olumsuz bir yargıya varmadan, daha objektif bir bakış açısı sunduklarını işaret eder.

Pasta grafiği, veri setindeki duygu dağılımındaki eşitsizlikleri ortaya koyarak, veri setinin daha dengeli bir duygu dağılımına sahip olup olmadığını değerlendirme imkanı sağlar. Duygusal tonlar arasındaki bu dengesizlik, analizlerin sonuçlarını etkileyebilir ve bu nedenle dikkate alınması gereken önemli bir faktördür. Özellikle, pozitif yorumların ağırlıkta olduğu bir veri seti, analiz sonuçlarının firma lehine eğilim gösterebileceğini düşündürebilir.

Bu tür bir duygu dağılım analizi, firma isimleri ve müşteri geri bildirimleri arasındaki ilişkileri daha derinlemesine inceleyerek, müşteri memnuniyetinin ve marka algısının nasıl şekillendiğini anlamaya yardımcı olabilir.
<br><br><br>
![Pasta](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/img/ABSA_DuyguDagilimiPasta.png)
<br><br>
Aşağıdaki grafik, belirli şirketler için yapılan duygu analizi sonuçlarını göstermektedir. Grafikte, en sık kullanılan 10 şirketin (Adidas, Apple, Google, Microsoft, Nike, Samsung, Sony, Turkcell, Türk Telekom, Vodafone) adları yatay eksende yer alırken, dikey eksen bu şirketlere atfedilen yorumların frekansını göstermektedir. 

Grafikteki sütunlar, her şirket için pozitif, nötr ve negatif duyguya sahip yorumların dağılımını göstermektedir. Üç farklı renk, bu duygu kategorilerini temsil eder:
- Sarı: Pozitif duygu
- Yeşil: Nötr duygu
- Mor: Negatif duygu

Örneğin, Apple için pozitif duyguya sahip yorumların sayısı en yüksekken, negatif duyguya sahip yorumlar daha düşük bir frekansta gözlenmektedir. Microsoft ve Samsung gibi diğer büyük teknoloji şirketleri için de benzer bir dağılım görülmektedir, ancak şirketten şirkete pozitif ve negatif yorumların oranı değişiklik göstermektedir.

Bu grafik, belirli şirketlere yönelik genel kullanıcı duyarlılığını anlamak için kullanışlıdır ve şirketlerin marka imajını yönetmelerine yardımcı olabilir. ABSA (Aspect-Based Sentiment Analysis) veri setinde en sık rastlanan şirket isimlerini analiz etmek, verinin amaca uygunluğunu kontrol etmek için önemli bir adım olmuştur. Bu analiz sonucunda, verilerin şirketler arası duygu dağılımını anlamaya yönelik olduğu görülmektedir.
<br><br><br>
![En Sık 10 Şirket](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/img/EnCokGecenSirket.png)
<br>

## 4. Firma İsimlerinin Tespiti

### Varlık Adı Tanıma (NER) Modeli ile Firma İsimlerinin Belirlenmesi
Varlık Adı Tanıma (NER) modeli kullanılarak, metinlerde geçen firma isimleri yüksek doğrulukla tespit edilmiştir. Bu model, BERT gibi önceden eğitilmiş dil modelleri temel alınarak özelleştirilmiş ve Türkçe diline uyarlanmıştır.

### Modelin Eğitimi ve Değerlendirilmesi
Modelin eğitimi, geniş bir veri seti kullanılarak gerçekleştirilmiş ve modelin performansı çeşitli metrikler kullanılarak değerlendirilmiştir. Eğitim süreci ve modelin performansına dair detaylı bilgiler sunulmuştur.

### Elde Edilen Sonuçların Doğruluğu ve Hassasiyeti
Modelin tespit ettiği firma isimlerinin doğruluğu ve hassasiyeti değerlendirilmiş, elde edilen sonuçların doğruluğu ve güvenilirliği ortaya koyulmuştur.

## 5. Duygu Analizi

### Duygu Analizi Yöntemleri ve Kullanılan Model
Projemizin duygu analizi kısmında, metinlerdeki ince duygusal nüansları yakalamak ve firma isimlerine atfedilen duyguları yüksek doğrulukla belirlemek amacıyla gelişmiş Aspect-Based Sentiment Analysis (ABSA) yöntemleri kullanılmıştır. Bu görevde, Transformer tabanlı modellerin gücünden yararlanılmış ve kapsamlı bir ön eğitim sürecinden geçirilmiş özel bir BERTürk modeli kullanılmıştır. BERTürk, çok katmanlı dikkat mekanizmaları sayesinde, cümlelerin bağlamını derinlemesine anlayarak, metin içindeki belirli varlıkların etrafındaki duygusal ifadeleri ayırt etme yeteneğine sahiptir.

### Metin İçerisinde Firma İsimlerine Atfedilen Duyguların Tespiti
Metinler içerisinde firma isimlerine atfedilen duyguların tespiti, ABSA modelimiz aracılığıyla gerçekleştirilmiştir. Model, cümleler içinde belirtilen her bir firma ismi için ilgili duygu durumunu (pozitif, negatif, nötr) belirler. Bu sayede, firmalarla ilgili müşteri yorumları ve geri bildirimleri detaylı bir şekilde analiz edilebilir.

```
Örnek olarak:


{
    "text": "Vodafone'un verdiği tanıtım faaliyetleri hayli avantajlı, lakin Turkcell'in servisleri hayli standart.",
    "entities": [
        {
            "entity": "Vodafone",
            "sentiment": "positive"
        },
        {
            "entity": "Turkcell",
            "sentiment": "neutral"
        }
    ]
}
```
Yukarıdaki örnekte, ABSA modelimiz "Vodafone" için pozitif, "Turkcell" için nötr duygu durumu tespit etmiştir.

### Duygu Dağılımının ve Sonuçların Görselleştirilmesi
Yapılan analizler sonucunda elde edilen duygu dağılımlarının ve sonuçların görselleştirilmesi, firmaların genel duygu profillerini ve müşteri algısını daha iyi anlamamıza yardımcı olmaktadır. Aşağıda, farklı grafik türleri kullanarak elde edilen görselleştirmeler açıklanmıştır:


## 6. Veri Ön İşleme Süreci ve Kararlarımız

Geliştirme sürecimizde, çeşitli veri ön işleme adımlarının etkilerini analiz ederek en uygun microservice’i oluşturduk. Bu sürecin sonunda, metin işleme ve model performansını artıran en etkili yöntemleri belirledik.

1. Noktalama İşaretlerinin Kaldırılması
Gözlem: Noktalama işaretlerini kaldırdığımızda, modelin cümle yapısını anlamakta zorluk çektiğini ve bu nedenle Adlandırılmış Varlık Tanıma (NER) ve Duygu Analizi performansının düştüğünü fark ettik.
Karar: Noktalama işaretlerinin cümle yapısının korunması ve anlamın doğru bir şekilde modellenmesi için kritik öneme sahip olduğunu belirledik ve bu işlemden vazgeçtik.

2. Stop-Words’lerin Kaldırılması
Gözlem: Stop-words’leri kaldırmak, veri boyutunu azaltarak verimliliği artırdı; ancak, bu işlem modelin duygusal ipuçlarını tespit etme yeteneğini olumsuz etkiledi ve doğruluğu düşürdü.
Karar: Stop-words’lerin cümledeki duygusal tonu belirlemede önemli bir rol oynadığını göz önünde bulundurarak, bu kelimeleri veri setinde bırakmaya karar verdik.

3. Stemming ve Lemmatization
Gözlem: Stemming ve Lemmatization işlemleri, kelimelerin kök formlarını çıkarmaktadır. Ancak, özellikle firmaların adları için bu işlem anlam kaybına neden oldu. Örneğin, "Microsoft" ismi "micro" ve "soft" gibi farklı köklere indirgenerek yanlış yorumlamalara yol açtı. Karar: Firmaların isimlerinin doğru bir şekilde tanımlanabilmesi nu işlemlerden vazgeçtik. İsimlerin orijinal formlarını korumanın daha uygun olduğuna karar verdik.

4. Tekrarlayan Boşluklar ve Karakterlerin Temizlenmesi
Gözlem: Tekrarlayan boşluklar ve karakterler temizlendiğinde, modelin performansında belirgin bir iyileşme gözlemedik. Bu adım, metnin daha tutarlı ve okunabilir hale gelmesini sağladı.
Karar: Tekrarlayan boşlukları ve karakterleri temizleme adımını uygulamaya devam ettik. Bu işlem, veri kalitesini artırmakta ve model performansını iyileştirmektedir.

5. Büyük/Küçük Harfe Dönüştürme
Gözlem: Büyük/küçük harfe dönüştürme işlemi, bazı varlıkların tanımlanmasında sorun yarattı. Özellikle kısaltmaların tanımlanmasında zorluk yaşandı. Örneğin, "NASA" büyük harflerle kolayca algılanırken, küçük harflere dönüştürüldüğünde tanınmakta zorlandı.
Karar: Kısaltmalar ve özel isimler için bu dönüşümü uygulamaktan vazgeçtik ve bu işlemi dikkatli bir şekilde ele aldık.

Sonuç
Yukarıdaki ön işleme adımları ve gözlemler doğrultusunda, modelimiz için en uygun veri ön işleme stratejilerini belirledik ve bu adımları bir microservice olarak hayata geçirdik. Bu microservice, metinlerin doğru bir şekilde işlenmesini sağlayarak, hem NER hem de Duygu Analizi görevlerinde yüksek performans sergilemektedir.
<br>
## 7. Sonuçlar ve Analiz 📈

### NER Modeli Performans Metrikleri

| Metric       | Value  |
|--------------|--------|
| Doğruluk     | %96.2  |
| Hassasiyet   | %95.0  |
| Geri Çağırma | %95.8  |
| F1 Skoru     | %95.4  |

### ABSA Modeli Performans Metrikleri

| Metrik       | Değer  |
|--------------|--------|
| Doğruluk     | %94.8  |
| Hassasiyet   | %95.5  |
| Geri Çağırma | %95.1  |
| F1 Skoru     | %95.3  |

### Kullanılan NER ve ABSA Modellerinin Detayları

Bu projede, firma isimlerinin doğru ve hassas bir şekilde tanınabilmesi ve bu isimlere atfedilen duyguların belirlenmesi amacıyla, iki gelişmiş model kullanılmıştır: NER (Varlık Adı Tanıma) ve ABSA (Aspect-Based Sentiment Analysis) modelleri. Aşağıda, bu modellerin detayları, eğitim süreçleri ve performans değerlendirmeleri yer almaktadır.

### NER (Varlık Adı Tanıma) Modeli

Bu projede, savasy/bert-base-turkish-ner-cased modeli kullanılmıştır. Bu model, Türkçe dilinin yapısal özelliklerini dikkate alarak eğitilmiş olup, isim tanıma görevlerinde üstün performans sergilemektedir. Modelin güçlü dil anlayışı ve bağlam duyarlılığı, metinlerdeki firma isimlerini yüksek doğrulukla tanımasına olanak tanır.
<br>
#### Kullanımı
```
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
model = AutoModelForTokenClassification.from_pretrained("STNM-NLPhoenix/bert-base-ner-cased")
tokenizer = AutoTokenizer.from_pretrained("STNM-NLPhoenix/bert-base-ner-cased")
```

### ABSA (Aspect-Based Sentiment Analysis) Modeli

Metinlerde firma isimlerine atfedilen duyguların belirlenmesi için dbmdz/bert-base-turkish-cased modeli tercih edilmiştir. Bu model, Türkçe metinlerde duygusal tonları ve bağlamı anlamada yüksek başarı gösterir. Modelin esnek yapısı ve derin öğrenme yetenekleri, firma isimleri etrafındaki duygusal ifadeleri etkili bir şekilde sınıflandırmasını sağlar.
<br>
#### Kullanımı
```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("STNM-NLPhoenix/bert-base-absa")
model = AutoModelForSequenceClassification.from_pretrained("STNM-NLPhoenix/bert-base-absa")
```

### Model Eğitim Süreci ve Hiperparametre Ayarları

*NER Modeli Eğitimi*
<br><br>
| Model Adı                                   | learning_rate | batch_size | epochs | val_loss | f1_score |
|---------------------------------------------|---------------|------------|--------|----------|----------|
| STNM-NLPhoenix/bert-base-ner-cased            | 4e-5          | 32         | 2      | 0.2725   | 0.9543   |
| STNM-NLPhoenix/bert-base-ner-cased            | 3e-5          | 64         | 3      | 0.2694   | 0.9517   |
| STNM-NLPhoenix/bert-base-ner-cased            | 5e-5          | 16         | 4      | 0.2633   | 0.9392   |

savasy/bert-base-turkish-ner-cased modeli, yaklaşık 130,000 firma isimleri ile ilgili veri seti kullanılarak ince ayar yapılmıştır (finetuning). Eğitim süreci boyunca, modelin öğrenme oranı, batch boyutu, epoch sayısı gibi hiperparametreler özenle ayarlanmıştır. Özellikle, 3e-5 öğrenme oranı, 32 batch boyutu ve 5 epoch, modelin optimum performansı yakalamasında etkili olmuştur. Model, geniş ve çeşitli veri seti sayesinde, farklı sektörlerden gelen firma isimlerini doğru bir şekilde tanımak üzere eğitilmiştir.


*ABSA Modeli Eğitimi*
<br><br>
| Model Adı                                   | learning_rate | batch_size | epochs | val_loss | f1_score |
|---------------------------------------------|---------------|------------|--------|----------|----------|
| STNM-NLPhoenix/bert-base-absa           | 2e-5          | 64         | 2      | 0.2689   | 0.9535   |
| STNM-NLPhoenix/bert-base-absa           | 4e-5          | 128        | 3      | 0.2641   | 0.9521   |
| STNM-NLPhoenix/bert-base-absa           | 3e-5          | 16         | 4      | 0.2738   | 0.9358   |

dbmdz/bert-base-turkish-cased modeli, yaklaşık 120,000 veri ile eğitilmiştir. Bu süreçte, modelin duygusal bağlamları anlaması için çeşitli duygusal ifadeler içeren geniş bir veri seti kullanılmıştır. Eğitim sırasında, öğrenme oranı 2e-5, batch boyutu 16 ve 4 epoch kullanılmıştır. Hiperparametrelerin bu şekilde ayarlanması, modelin hem eğitim sürecinde hem de genel performansında yüksek verimlilik sağlamıştır.


### Modelin Performansının Değerlendirilmesi

Eğitim süreçlerinin ardından, modellerin performansı kapsamlı bir şekilde değerlendirilmiştir. Performans değerlendirmesi, doğruluk (accuracy), hassasiyet (precision), geri çağırma (recall) ve F1 skoru gibi temel metrikler üzerinden gerçekleştirilmiştir.

### NER Modeli Performansı

savasy/bert-base-turkish-ner-cased modeli, test verileri üzerinde %95'in üzerinde doğruluk ve %93 hassasiyet ile üstün bir performans sergilemiştir. Geri çağırma oranı %92 ve F1 skoru %92.5 olan model, firma isimlerini tanımada yüksek doğruluk sağlamıştır.

### Analiz ve Sonuçlar

Projemizin analiz ve sonuçları, kullanılan NER ve ABSA modellerinin üstün performansını ve metin analizindeki etkinliğini göstermektedir. Bu modeller sayesinde, Türkçe metinlerde firma isimlerinin doğru bir şekilde tanınması ve bu isimlere atfedilen duyguların yüksek doğrulukla belirlenmesi sağlanmıştır. Kullanılan NER ve ABSA modelleri, metin analizi süreçlerinde yüksek doğruluk ve etkinlik sunarak, proje hedeflerimize ulaşmamızı sağlamıştır.

## 8. Arayüz ve API Entegrasyonu
Projede, kullanıcı dostu ve etkili bir arayüz oluşturmak için FastAPI kullanıldı. FastAPI, projede API'lerin hızlı ve verimli bir şekilde sunulmasını sağladı. Modern Python web framework'leri arasında yer alan FastAPI, yüksek performansı ve kolay entegrasyon imkanı sayesinde öne çıktı. Kullanıcılar, bu API'ler aracılığıyla modellere erişip sonuçları hızlıca elde edebildi ve API'lerin sunduğu esneklik sayesinde farklı cihaz ve platformlardan kolayca veri çekebildi.

Ayrıca, Jinja şablon motoru projede önemli bir rol oynadı. Jinja, dinamik içerikler oluşturmak için güçlü bir araç sundu ve verilerin şablonlara kolayca entegre edilmesini sağladı. Bu sayede, kullanıcıya özelleştirilmiş ve dinamik içerikler sunularak, arayüzün kullanıcı ihtiyaçlarına göre şekillendirilmesi mümkün hale getirildi. Jinja, FastAPI ile mükemmel bir uyum içinde çalışarak projenin esnekliğini ve kullanıcı deneyimini daha da geliştirdi.
<br>
![API](https://github.com/STNM-NLPhoenix/Teknofest2024TDDI/blob/main/img/Arayuz.jpg)

## 9. Sonuç ve Gelecek Çalışmalar

### Projenin Sonuçları ve Genel Değerlendirme
Teknofest Türkçe Doğal Dil İşleme Yarışması'nda Entity Bazlı Duygu Analizi kategorisinde yürüttüğümüz proje, müşteri geri bildirimlerinin analiz edilerek belirli hizmet yönleri veya ürün özellikleriyle ilgili duyguların sınıflandırılmasını hedeflemektedir. Bu doğrultuda, üç ana model geliştirdik:

Projeyi gerçekleştirirken, özelleştirilmiş duygu analizi modeli yerine ABSA modelinin daha uygun olduğuna karar verdik. ABSA modeli, NER modelinden aldığı varlıklar üzerinde çalışarak, yorumları doğru entity'ye atfetme ve ilgili hizmet yönlerine göre duygu analizi yapma görevini başarıyla yerine getirdi.

Çeşitli hiperparametreler, aktivasyon fonksiyonları ve optimizasyon fonksiyonları deneyerek, modelin doğruluğunu artırdık. Farklı mimarilerdeki modelleri deneyerek en iyi performansı elde etmeye çalıştık. Özellikle Türkçe dilindeki ima cümlelerini de veri setine ekleyerek, bu zorlu alanda önemli bir adım attık.

### Gelecekteki İyileştirme Alanları ve Öneriler

1. *Türkçe'nin İma Cümleleri Üzerine Çalışmalar*: İma cümleleri, duyguları dolaylı yoldan belirttiği için modelin duygu tespiti yapması genellikle zor olmaktadır. Bu alanda daha fazla veri ve model optimizasyonu yaparak, ima cümlelerinin analizi iyileştirilebilir.

2. *Sektör Bazlı Performans Analizi*: Aynı sektörde çalışan firmalar hakkında yapılan olumlu ve olumsuz yorumlar, hangi şirketlerin hangi alanlarda daha iyi olduğunu gösterebilir. Bu analiz, firmaların kendilerini geliştirmeleri gereken alanları görmelerine yardımcı olabilir.

3. *Spesifik Sektörlerde Çalışma Önerileri*: Belirli sektörlerdeki olumsuz yorumlar, bu alanlarda yapılması gereken geliştirmeler için öneriler sunabilir. Örneğin, müşteri hizmetleri ile ilgili sıkça olumsuz yorumlar alan bir sektör, bu alana yönelik iyileştirmeler yapabilir.

4. *Veri Setlerinin Geliştirilmesi*: Hazırladığımız spesifik ve nadir bulunan veri setleri, Türkçe Doğal Dil İşleme alanında önemli bir etki yaratmaktadır. Bu veri setlerini genişleterek ve daha fazla örnek ekleyerek, modellerin doğruluğunu ve genel performansını artırabiliriz.

### TDDi'ye Katkısı

*Spesifik Veri Setleri*: Özellikle ima cümleleri için hazırladığımız veri seti, daha önce bu alanda yapılmamış bir çalışmayı temsil etmektedir. Bu sayede, Türkçe'deki duygu tespitine yönelik zorluklar aşılabilir ve daha doğru analizler yapılabilir.

*Model Performansı*: Özelleştirilmiş ABSA modelimiz, NER modelinden aldığı varlıklar sayesinde başarılı bir şekilde çalışmaktadır. Bu, diğer araştırmacılara ve uygulayıcılara yol gösterici olabilir.

## 10. Referanslar

- [Exploiting BERT for End-to-End Aspect-based Sentiment Analysis](https://arxiv.org/abs/1910.00883)
- [Aspect-Based Sentiment Analysis using BERT](https://aclanthology.org/W19-6120/)
- [Context-Guided BERT for Targeted Aspect-Based Sentiment Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/17659)
- [Modelling Context and Syntactical Features for Aspect-based Sentiment Analysis](https://aclanthology.org/2020.acl-main.293/)
- [Aspect Based Twitter Sentiment Analysis on Vaccination and Vaccine Types in COVID-19 Pandemic With Deep Learning](https://ieeexplore.ieee.org/abstract/document/9640526?casa_token=9aSeVTLCdZoAAAAA:c3ZQugvAolVRaGuCghXpusXndgoerFNHxOEMhcprgWmdk8MhTmxIPOt-Oy1O0j-Z-iB3c-ZFkmQ)
- [The Effect of BERT, ELECTRA and ALBERT Language Models on Sentiment Analysis for Turkish Product Reviews](https://ieeexplore.ieee.org/abstract/document/9559007?casa_token=yi6g1vtJjqMAAAAA:sIOwqyPR0_aCvD9rv44bd8zhwKpIPQg3hyoBtVspstyWKJqxzQU2kch40IgmkrNW0CGIVP8JqMA)

## 11. Bağımlılıklar

### Sanal Ortamın Oluşturulması

Proje bağımlılıklarını izole bir ortamda yönetmek için bir sanal ortam oluşturun.

      python -m venv myenv
      source myenv/bin/activate  # MacOS/Linux
      myenv\Scripts\activate  # Windows

### CUDA 12.1 için

      pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

### Proje için gerekli kütüphaneleri ve paketleri yükleyin:

      pip install -r requirements.txt

### Model Dosyasının Dizinine Gitme

      cd path/to/your/model_directory

### Model Dosyasının Çalıştırılması

      python main.py


Bu içerikler sanal ortamın oluşturulmasından başlayarak gerekli bağımlılıkların kurulmasına kadar tüm adımları içermektedir.
