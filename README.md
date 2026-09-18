<div align="center">

# ♟️ CHESS AI

### Deep learning tabanlı satranç oynayan yapay zekâ modeli

<p>
Chess AI, satranç pozisyonlarını analiz ederek uygun hamleleri tahmin etmeyi amaçlayan
derin öğrenme tabanlı bir yapay zekâ projesidir.
</p>

<br>

<img src="https://img.shields.io/badge/Python-AI-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
<img src="https://img.shields.io/badge/Chess-AI-black?style=for-the-badge">
<img src="https://img.shields.io/badge/CNN-Model-blueviolet?style=for-the-badge">

<br><br>

<img src="https://img.shields.io/badge/Status-Experimental-orange?style=flat-square">
<img src="https://img.shields.io/badge/Domain-Computer%20Vision%20%26%20AI-blue?style=flat-square">
<img src="https://img.shields.io/badge/Language-Python-yellow?style=flat-square">

</div>

---

## 📖 Proje Hakkında

**Chess AI**, satranç tahtasındaki pozisyonları değerlendirerek bir sonraki hamleyi tahmin etmeyi amaçlayan bir yapay zekâ projesidir.

Proje, klasik satranç motorlarından farklı olarak hamle seçim sürecinde öğrenilmiş bir model kullanmayı hedeflemektedir.

Amaç, satranç konumlarını makine öğrenmesi perspektifinden ele alarak modelin taş dağılımlarını, pozisyon ilişkilerini ve olası hamleleri öğrenmesini sağlamaktır.

---

## 🧠 Model Yaklaşımı

Projede derin öğrenme tabanlı bir yaklaşım kullanılmaktadır.

Modelin temel amacı:

* Satranç tahtasını sayısal olarak temsil etmek
* Taşların konumlarını analiz etmek
* Pozisyon içerisindeki ilişkileri öğrenmek
* Olası hamleler arasından uygun hamleyi tahmin etmek
* Eğitim verisinden satranç örüntülerini öğrenmek

Model mimarisinde **Convolutional Neural Network (CNN)** yaklaşımı kullanılmaktadır.

---

<div align="center">

## 🛠️ Kullanılan Teknolojiler

<br>

<img src="https://skillicons.dev/icons?i=python,pytorch,git,github" />

<br><br>

</div>

### Artificial Intelligence

**Deep Learning · CNN · Model Training · Inference**

### Programming

**Python**

### Framework

**PyTorch**

### Development

**Git · GitHub**

---

## ♟️ Neden CNN?

Satranç tahtası doğal olarak **8×8'lik uzamsal bir yapı** içerir.

Bu nedenle CNN tabanlı modeller, taşların yalnızca tek tek konumlarını değil aynı zamanda birbirlerine göre konumlarını da öğrenmek için kullanılabilir.

Örneğin model:

* Taşların korunup korunmadığını
* Taş yoğunluğunu
* Merkez kontrolünü
* Saldırı ilişkilerini
* Savunma yapılarını
* Pozisyonel örüntüleri

eğitim verisinden öğrenebilir.

---

## 🎯 Projenin Amacı

Bu proje yalnızca güçlü bir satranç botu üretmek için değil, aynı zamanda derin öğrenme modellerinin karar verme problemlerinde nasıl kullanılabileceğini araştırmak amacıyla geliştirilmiştir.

Proje kapsamında özellikle:

* Veri ön işleme
* Satranç pozisyonlarının temsil edilmesi
* CNN mimarileri
* Model eğitimi
* Tahmin sistemleri
* Yapay zekâ ile karar verme

konularına odaklanılmaktadır.

---

## 🔄 Genel Çalışma Mantığı

<div align="center">

```text
Chess Position
      ↓
Board Representation
      ↓
Neural Network
      ↓
Position Analysis
      ↓
Move Prediction
      ↓
Selected Move
```

</div>

Model, mevcut satranç pozisyonunu girdiye dönüştürür ve öğrendiği örüntülere göre uygun hamleyi tahmin etmeye çalışır.

---

## 📊 Eğitim Süreci

Model satranç pozisyonları ve bu pozisyonlarda oynanan hamleler üzerinden eğitilmektedir.

Genel eğitim süreci:

```text
Chess Games
     ↓
Position Extraction
     ↓
Data Encoding
     ↓
Model Training
     ↓
Evaluation
     ↓
Move Prediction
```

Eğitim sürecinde modelin farklı satranç konumlarını tanıması ve daha tutarlı hamle tahminleri üretmesi hedeflenmektedir.

---

## 🔬 Deneysel Proje

Bu proje araştırma ve öğrenme amacıyla geliştirilmiştir.

Modelin performansı:

* Eğitim verisinin büyüklüğüne
* Veri kalitesine
* Kullanılan model mimarisine
* Eğitim süresine
* Hiperparametrelere

bağlı olarak değişebilir.

Bu nedenle proje klasik Stockfish benzeri brute-force tabanlı satranç motorlarının yerine geçmekten çok, **neural network tabanlı satranç karar sistemlerini deneyimlemeye yönelik bir çalışma** niteliğindedir.

---


## 🚀 Gelecek Planları

Projenin ilerleyen aşamalarında modelin yalnızca hamle tahmini yapması değil, pozisyonların genel gücünü değerlendirebilmesi de hedeflenmektedir.

Planlanan geliştirmeler arasında:

* Position evaluation
* Self-play
* Reinforcement Learning
* Daha derin neural network mimarileri
* Move ranking
* Oyun sonu analizi

bulunmaktadır.

---

## 🧪 Öğrenme Hedefleri

Bu proje ile aşağıdaki konular üzerinde pratik yapılmaktadır:

* Deep Learning
* CNN mimarileri
* Tensor işlemleri
* Classification problemleri
* Model eğitimi
* Satranç verisinin işlenmesi
* AI decision making
* Neural network optimization

---

<div align="center">

## 👨‍💻 Developer

### Deniz Sarp Yazıcıoğlu

**Software Engineer · Backend · AI · Systems Programming**

<br>

<img src="https://img.shields.io/badge/Python-Developer-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
<img src="https://img.shields.io/badge/Chess-AI-000000?style=for-the-badge">

<br><br>

---

**Chess AI ♟️**

*Exploring chess through neural networks.*

</div>
