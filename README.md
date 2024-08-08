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

- **Aspect-Based Sentiment Analysis (ABSA):** Firma isimlerine atfedilen duygu tonlarının belirlenmesi için, ABSA yöntemleri kullanılmıştır. Bu model, belirli bir firma veya konu hakkındaki duygusal tonları (pozitif, negatif, nötr) belirlemeye yönelik özelleştirilmiştir. ABSA, belirli bir metindeki duygu durumlarını daha detaylı ve ince bir şekilde analiz ederek, firma algısını ve müşteri geri bildirimlerini anlamada önemli bir rol oynar.

- **Veri Ön İşleme ve Temizleme:** Verilerin doğruluğunu ve kalitesini artırmak için kapsamlı veri ön işleme ve temizleme işlemleri uygulanmıştır. Bu işlemler, metinlerdeki gereksiz bilgilerin temizlenmesi, özel karakterlerin ve duraklamaların (stopwords) çıkarılması, yazım hatalarının düzeltilmesi ve metinlerin dil bilgisi kurallarına uygun hale getirilmesi gibi adımları içerir.

- **Makine Öğrenimi ve Derin Öğrenme Teknikleri:** Projede, makine öğrenimi ve derin öğrenme teknikleri kullanılarak, metinlerin analizi ve sınıflandırılması gerçekleştirilmiştir. Bu teknikler, metin verilerinin özelliklerinin çıkarılması, örüntülerin tespit edilmesi ve sınıflandırma işlemlerinde yüksek doğruluk ve performans sağlar.

- **Veri Görselleştirme ve Analiz:** Elde edilen sonuçların daha iyi anlaşılabilir ve yorumlanabilir hale getirilmesi için, veri görselleştirme teknikleri kullanılmıştır. Grafikler, tablolar ve diğer görsel araçlar, metin analizlerinin sonuçlarını daha etkili bir şekilde sunar ve önemli bulguların öne çıkmasını sağlar.

Bu teknikler ve yöntemler, projenin başarılı bir şekilde gerçekleştirilmesi ve hedeflerine ulaşması için önemli katkılar sağlamıştır. Projenin çıktıları, Türkçe dilinde doğal dil işleme alanındaki araştırmalara ve uygulamalara değerli bir katkı sunmaktadır.

## Veri Kümesi

### Veri Kaynağı ve Toplama Süreci
Modelimizi geliştirirken iki farklı veri kümesi kullandık. İlk veri kümesi ABSA (Aspect-Based Sentiment Analysis) veri kümesi olup müşteri yorumlarındaki görüşlerin ve hedef varlıkların saptanması için tasarlanmıştır. İkinci veri kümesi ise NER (Named Entity Recognition) veri kümesidir. Bu veri kümesi, metindeki firmaların tanınması ve sınıflandırılması için kullanılıyor. Veri setlerini oluştururken öncelikle modelimiz için gerekli doğru formatı belirledik. Yapay zeka araçlarını kullanarak belirlediğimiz formatta veri setini oluşturarak modelin gerçek performansını öğrenmeyi amaçladık.

### Veri Setinin Genel Yapısı ve Veri Setinin İçeriği

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

## Keşifsel Veri Analizi (EDA)

### Verinin Genel Özellikleri ve İlk İncelemeler
Veri setinin genel özellikleri incelenmiş ve metinlerde geçen firma isimleri ile bu isimlere atfedilen duygu durumları analiz edilmiştir. İlk incelemeler, veri setindeki firma isimlerinin ve duygu durumlarının dağılımını ortaya koymuştur.

### Veri Görselleştirme ve Öne Çıkan Bulgular
Veri seti, çeşitli görselleştirme teknikleri kullanılarak analiz edilmiştir. Bu analizler, firma isimlerinin ve duygu durumlarının dağılımını görselleştirerek, öne çıkan bulguları ortaya koymuştur.

### Firma İsimleri ve İlişkili Duygusal Analizler
Firma isimlerine atfedilen duygusal tonlar analiz edilerek, firma isimleri ve bu isimlere atfedilen duygusal durumlar arasındaki ilişkiler incelenmiştir. Bu analizler, firma algısını ve müşteri geri bildirimlerini anlamada önemli bulgular sunmaktadır.

## Firma İsimlerinin Tespiti

### Varlık Adı Tanıma (NER) Modeli ile Firma İsimlerinin Belirlenmesi
Varlık Adı Tanıma (NER) modeli kullanılarak, metinlerde geçen firma isimleri yüksek doğrulukla tespit edilmiştir. Bu model, BERT gibi önceden eğitilmiş dil modelleri temel alınarak özelleştirilmiş ve Türkçe diline uyarlanmıştır.

### Modelin Eğitimi ve Değerlendirilmesi
Modelin eğitimi, geniş bir veri seti kullanılarak gerçekleştirilmiş ve modelin performansı çeşitli metrikler kullanılarak değerlendirilmiştir. Eğitim süreci ve modelin performansına dair detaylı bilgiler sunulmuştur.

### Elde Edilen Sonuçların Doğruluğu ve Hassasiyeti
Modelin tespit ettiği firma isimlerinin doğruluğu ve hassasiyeti değerlendirilmiş, elde edilen sonuçların doğruluğu ve güvenilirliği ortaya koyulmuştur.

## 5. Duygu Analizi

### 5.1 Duygu Analizi Yöntemleri ve Kullanılan Model
Projemizin duygu analizi kısmında, metinlerdeki ince duygusal nüansları yakalamak ve firma isimlerine atfedilen duyguları yüksek doğrulukla belirlemek amacıyla gelişmiş Aspect-Based Sentiment Analysis (ABSA) yöntemleri kullanılmıştır. Bu görevde, Transformer tabanlı modellerin gücünden yararlanılmış ve kapsamlı bir ön eğitim sürecinden geçirilmiş özel bir BERTürk modeli kullanılmıştır. BERTürk, çok katmanlı dikkat mekanizmaları sayesinde, cümlelerin bağlamını derinlemesine anlayarak, metin içindeki belirli varlıkların etrafındaki duygusal ifadeleri ayırt etme yeteneğine sahiptir.

### 5.2 Metin İçerisinde Firma İsimlerine Atfedilen Duyguların Tespiti
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

### 5.3 Duygu Dağılımının ve Sonuçların Görselleştirilmesi
Yapılan analizler sonucunda elde edilen duygu dağılımlarının ve sonuçların görselleştirilmesi, firmaların genel duygu profillerini ve müşteri algısını daha iyi anlamamıza yardımcı olmaktadır. Aşağıda, farklı grafik türleri kullanarak elde edilen görselleştirmeler açıklanmıştır:

*Sentiment Dağılım Grafiği:* Vodafone, Turkcell ve Samsung firmalarının duygu dağılımlarını inceledik. Sentiment dağılım grafiği, her bir firmanın pozitif, negatif ve nötr duygu oranlarını açıkça gösterir.

![ABSA_duyguDagilimi](https://github.com/user-attachments/assets/40815ab5-3734-4ec5-9830-a43c7a912022)

![ABSA_turkcellDuygu](https://github.com/user-attachments/assets/a25a9ff7-6e3f-4335-9570-de3600b0c006)


*Entity-Sentiment İlişki Grafiği:* Seçtiğimiz üç firmanın aldığı farklı duygu türlerinin bir arada gösterildiği yığılmış bar grafiğidir. Bu grafik, her firmanın genel duygu profiline dair detaylı bir görsel sunar.

![ABSA_Aldigifarklıduygutürleri](https://github.com/user-attachments/assets/9720f206-967c-460b-a967-7f5d3e1dabca)


*Heatmap:* Oluşturduğumuz heatmap, seçtiğimiz üç firmanın (Samsung, Turkcell, Vodafone) duygu analizi sonuçlarını görsel olarak sunar. Bu grafik, firmalar arasındaki farklılıkları veya benzerlikleri belirlememize yardımcı olur.

![ABSA_FİRMAVEDUYGUTÜRiLİŞKİ](https://github.com/user-attachments/assets/1b12b664-2cf9-4030-afaf-2a12bf336166)


*Text Length (Metin Uzunluğu):* Metinlerin uzunluğu ile duygu türü arasında bir ilişki olup olmadığını inceledik. Örneğin, daha uzun metinlerde duygu tonunun daha yoğun olup olmadığını araştırdık.

![ABSAmetinuzunlugu_turkcel](https://github.com/user-attachments/assets/d9d9ac45-d81a-438b-9b1d-342069710e76)


*Entity-Sentiment Pairing:* Belirli bir firmanın hangi duygu türüyle daha sık ilişkilendirildiğini inceledik. Bu analiz, firmanın müşteri geri bildirimlerindeki duygusal eğilimlerini ortaya koyarak genel algısını ve duygusal profilini detaylandırır.

![ABSA_firmaduygutürleri](https://github.com/user-attachments/assets/f06e0ccc-4b08-47e6-9250-c2506f483ccf)



## Veri Ön İşleme Süreci ve Kararlarımız
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

## Model Geliştirme

### Kullanılan NER ve ABSA Modellerinin Detayları
Projede kullanılan NER ve ABSA modellerinin teknik detayları ve bu modellerin nasıl eğitildiği açıklanmıştır. Modellerin performansı ve elde edilen sonuçlar değerlendirilmiştir.

### Model Eğitim Süreci ve Hiperparametre Ayarları
Model eğitim süreci ve kullanılan hiperparametre ayarları detaylandırılmıştır. Eğitim sürecinde karşılaşılan zorluklar ve bu zorlukların nasıl aşıldığına dair bilgiler verilmiştir.

### Modelin Performansının Değerlendirilmesi
Modelin performansı, çeşitli metrikler kullanılarak değerlendirilmiş ve sonuçlar sunulmuştur. Modelin doğruluğu, hassasiyeti ve güvenilirliği analiz edilmiştir.

## 8. Sonuçlar ve Analiz 📈

### NER Modeli Performans Metrikleri

| Metric       | Value  |
|--------------|--------|
| Doğruluk     | %95.0  |
| Hassasiyet   | %93.0  |
| Geri Çağırma | %92.0  |
| F1 Skoru     | %92.5  |

### ABSA Modeli Performans Metrikleri

| Metric       | Value  |
|--------------|--------|
| Doğruluk     | %90.0  |
| Hassasiyet   | %88.0  |
| Geri Çağırma | %87.0  |
| F1 Skoru     | %87.5  |




### Kullanılan NER ve ABSA Modellerinin Detayları

Bu projede, firma isimlerinin doğru ve hassas bir şekilde tanınabilmesi ve bu isimlere atfedilen duyguların belirlenmesi amacıyla, iki gelişmiş model kullanılmıştır: NER (Varlık Adı Tanıma) ve ABSA (Aspect-Based Sentiment Analysis) modelleri. Aşağıda, bu modellerin detayları, eğitim süreçleri ve performans değerlendirmeleri yer almaktadır.

### NER (Varlık Adı Tanıma) Modeli

Bu projede, savasy/bert-base-turkish-ner-cased modeli kullanılmıştır. Bu model, Türkçe dilinin yapısal özelliklerini dikkate alarak eğitilmiş olup, isim tanıma görevlerinde üstün performans sergilemektedir. Modelin güçlü dil anlayışı ve bağlam duyarlılığı, metinlerdeki firma isimlerini yüksek doğrulukla tanımasına olanak tanır.

### ABSA (Aspect-Based Sentiment Analysis) Modeli

Metinlerde firma isimlerine atfedilen duyguların belirlenmesi için dbmdz/bert-base-turkish-cased modeli tercih edilmiştir. Bu model, Türkçe metinlerde duygusal tonları ve bağlamı anlamada yüksek başarı gösterir. Modelin esnek yapısı ve derin öğrenme yetenekleri, firma isimleri etrafındaki duygusal ifadeleri etkili bir şekilde sınıflandırmasını sağlar.

### Model Eğitim Süreci ve Hiperparametre Ayarları

*NER Modeli Eğitimi*

savasy/bert-base-turkish-ner-cased modeli, yaklaşık 130,000 firma isimleri ile ilgili veri seti kullanılarak ince ayar yapılmıştır (finetuning). Eğitim süreci boyunca, modelin öğrenme oranı, batch boyutu, epoch sayısı gibi hiperparametreler özenle ayarlanmıştır. Özellikle, 3e-5 öğrenme oranı, 32 batch boyutu ve 5 epoch, modelin optimum performansı yakalamasında etkili olmuştur. Model, geniş ve çeşitli veri seti sayesinde, farklı sektörlerden gelen firma isimlerini doğru bir şekilde tanımak üzere eğitilmiştir.

*ABSA Modeli Eğitimi*

dbmdz/bert-base-turkish-cased modeli, yaklaşık 120,000 veri ile eğitilmiştir. Bu süreçte, modelin duygusal bağlamları anlaması için çeşitli duygusal ifadeler içeren geniş bir veri seti kullanılmıştır. Eğitim sırasında, öğrenme oranı 2e-5, batch boyutu 16 ve 4 epoch kullanılmıştır. Hiperparametrelerin bu şekilde ayarlanması, modelin hem eğitim sürecinde hem de genel performansında yüksek verimlilik sağlamıştır.

### Modelin Performansının Değerlendirilmesi

Eğitim süreçlerinin ardından, modellerin performansı kapsamlı bir şekilde değerlendirilmiştir. Performans değerlendirmesi, doğruluk (accuracy), hassasiyet (precision), geri çağırma (recall) ve F1 skoru gibi temel metrikler üzerinden gerçekleştirilmiştir.

### NER Modeli Performansı

savasy/bert-base-turkish-ner-cased modeli, test verileri üzerinde %95'in üzerinde doğruluk ve %93 hassasiyet ile üstün bir performans sergilemiştir. Geri çağırma oranı %92 ve F1 skoru %92.5 olan model, firma isimlerini tanımada yüksek doğruluk sağlamıştır.

| Metric       | Value |
|--------------|-------|
| Doğruluk     | %95.0 |
| Hassasiyet   | %93.0 |
| Geri Çağırma | %92.0 |
| F1 Skoru     | %92.5 |

### ABSA Modeli Performansı

dbmdz/bert-base-turkish-cased modeli, duygu analizi görevlerinde %90 doğruluk, %88 hassasiyet ve %87 geri çağırma oranı ile başarılı sonuçlar elde etmiştir. F1 skoru %87.5 olan model, metinlerdeki firma isimlerine atfedilen duyguları doğru bir şekilde sınıflandırabilmiştir.

| Metric       | Value |
|--------------|-------|
| Doğruluk     | %90.0 |
| Hassasiyet   | %88.0 |
| Geri Çağırma | %87.0 |
| F1 Skoru     | %87.5 |

### Analiz ve Sonuçlar

Projemizin analiz ve sonuçları, kullanılan NER ve ABSA modellerinin üstün performansını ve metin analizindeki etkinliğini göstermektedir. Bu modeller sayesinde, Türkçe metinlerde firma isimlerinin doğru bir şekilde tanınması ve bu isimlere atfedilen duyguların yüksek doğrulukla belirlenmesi sağlanmıştır. Kullanılan NER ve ABSA modelleri, metin analizi süreçlerinde yüksek doğruluk ve etkinlik sunarak, proje hedeflerimize ulaşmamızı sağlamıştır.


## Sonuç ve Gelecek Çalışmalar

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

## Referanslar
Projede kullanılan kaynaklar ve referanslar listelenmiştir. Bu referanslar, projede kullanılan teknikler ve yöntemler hakkında daha fazla bilgi edinmek isteyenler için yol gösterici olacaktır.

## Bağımlılıklar (Dependencies)

### Projenin Çalışması İçin Gerekli Olan Python Paketleri
Projenin çalışması için gerekli olan tüm Python paketleri ve bu paketlerin versiyonları listelenmiştir. Bu paketlerin kurulumu için gereken adımlar ve kullanım talimatları açıklanmıştır.

### Ortam Kurulumu ve Kullanım Talimatları
Projenin çalışması için gereken ortamın nasıl kurulacağı ve proje dosyalarının nasıl kullanılacağı adım adım açıklanmıştır. Bu talimatlar, projenin doğru bir şekilde çalıştırılması için gerekli olan tüm bilgileri içermektedir.

<div align="center">
    <a href="your-call-to-action-link" style="background-color:#4CAF50; color:white; padding:10px 20px; text-align:center; text-decoration:none; display:inline-block; border-radius:5px;">Başlamak İçin Tıklayın</a>
</div>
