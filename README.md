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
1. ABSA (Aspect-Based Sentiment Analysis) Veri Kümesi
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

ABSA Veri Seti Formatı:
text: Analiz edilen yorumun tam metni.
entities: Yorumdaki şirketler ve bu şirketlerle ilişkili duyguların belirtildiği bir liste.
oentity: Şirket adı.
osentiment: Şirketle ilişkili duygu (olumlu, olumsuz, nötr).
2. NER (Named Entity Recognition) Veri Kümesi
NER veri kümesi, metindeki önemli varlıkların (firmalar) tanınması ve sınıflandırılması için kullanılır. Veri kümesinde her satır, bir kelime ve bu kelimenin entity tipini (B-organization, I-organization, O) içerir. Örneğin, "vodafone", "turk telekom" ve "türknet" gibi kuruluş adları B-organization veya I-organization olarak etiketlenmiştir.

NER Veri Seti Formatı:
Özelleşmiş isterlere göre dizayn edilmiş organizasyon bazlı conLL formatında NER veri seti, her satırda bir kelime ve o kelimenin etiketini içerecek şekilde düzenlenmiştir. Bir cümle veya metin parçasının sonu boş bir satırla ayrılmıştır. Etiketler, organizasyon isimlerinin başlangıcını ("B-organization") ve devamını ("I-organization") belirtir.
B-organization: Bir organizasyon isminin başlangıcını belirtir.
I-organization: Organizasyon isminin devamını belirtir.
O: Organizasyon adı olmayan diğer kelimeleri belirtir.


   words,label
turk,B-organization
telekom,I-organization
müşteri,O
hizmetleri,O
kötü,O
olsa,O
da,O
türknet,B-organization
müşteri,O
hizmetleri,O
oldukça,O
ortalama.,O

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

## Duygu Analizi

### Duygu Analizi Yöntemleri ve Kullanılan Model
Duygu analizi için kullanılan yöntemler ve modeller detaylandırılmıştır. ABSA modeli kullanılarak, firma isimlerine atfedilen duygu tonları belirlenmiştir.

### Metin İçerisinde Firma İsimlerine Atfedilen Duyguların Tespiti
Metinlerde geçen firma isimlerine atfedilen pozitif, negatif veya nötr duygular tespit edilmiştir. Bu tespitler, müşteri geri bildirimlerinin ve firma algısının anlaşılmasında önemli rol oynamaktadır.

### Duygu Dağılımının ve Sonuçların Görselleştirilmesi
Duygu dağılımı ve analiz sonuçları, çeşitli görselleştirme teknikleri kullanılarak sunulmuştur. Grafikler ve tablolar, analiz sonuçlarının daha anlaşılır ve yorumlanabilir hale gelmesini sağlamıştır.

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

## Sonuçlar ve Analiz

### NER Modeli Performans Metrikleri
NER modelinin performans metrikleri sunulmuş ve modelin doğruluğu, hassasiyeti ve güvenilirliği değerlendirilmiştir. Elde edilen sonuçlar ve bu sonuçların proje hedefleriyle uyumu analiz edilmiştir.

### ABSA Modeli Performans Metrikleri
ABSA modelinin performans metrikleri detaylandırılmış ve modelin duygu analizi konusundaki başarısı değerlendirilmiştir. Elde edilen bulgular, modelin performansını ve güvenilirliğini ortaya koymaktadır.

### En Başarılı Modellerin Confusion Matrix ve ROC Eğrisi
En başarılı modellerin confusion matrix ve ROC eğrisi sunulmuş ve bu modellerin performansı detaylı bir şekilde analiz edilmiştir. Bu görseller, modellerin doğruluğunu ve hassasiyetini daha iyi anlamamıza yardımcı olmaktadır.

## Sonuç ve Gelecek Çalışmalar

### Projenin Sonuçları ve Genel Değerlendirme
Projenin genel sonuçları değerlendirilmiş ve elde edilen bulgular özetlenmiştir. Proje hedeflerine ne ölçüde ulaşıldığı ve projenin başarısı analiz edilmiştir.

### Gelecekteki İyileştirme Alanları ve Öneriler
Projenin gelecekteki iyileştirme alanları ve bu alanlarda yapılabilecek çalışmalar önerilmiştir. Bu öneriler, projenin daha da geliştirilmesi ve daha geniş bir etki yaratması için yol gösterici olacaktır.

### TDDi'ye Katkısı
Projenin TDDi'ye katkısı değerlendirilmiş ve elde edilen bulguların TDDi'nin genel hedefleriyle nasıl uyumlu olduğu analiz edilmiştir. Projenin TDDi'ye sağladığı değer ve gelecekteki projelere katkıları özetlenmiştir.

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
