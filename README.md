✨ Yenilikler & Özellikler
⏱️ Dinamik Çalışma Kronometresi: Masada çalışma materyalleri (kitap, laptop vb.) tespit edildiği andan itibaren çalışma sürenizi saniye saniye hesaplar.

🍎 Apple Silicon (M1/M2/M3) Optimizasyonu: MPS (Metal Performance Shaders) desteği ile Mac cihazlarda düşük güç tüketimi ve yüksek FPS.

⚠️ Akıllı Dikkat Dağıtıcı Filtresi: Telefonu sadece "görmekle" kalmaz; eğer 2 saniyeden uzun süre elinizde tutarsanız sizi görsel bir alarm (kırmızı ekran) ile uyarır.

💧 Hidrasyon Desteği: Görüş alanında bir su şişesi yoksa, sağlığınız için ekranda nazik bir hatırlatıcı belirir.

📊 Durum Bilgisi: O anki modunuzu (Çalışıyor/Mola) ve aktif çalışma sürenizi gerçek zamanlı olarak ekrana yansıtır.

🛠️ Teknoloji Yığını
Core AI: Ultralytics YOLOv11 Nano (Hız ve doğruluk dengesi için optimize edildi).

Vision: OpenCV (Görüntü işleme ve görsel geri bildirim).

Engine: Python 3.10+

Hardware Acceleration: M1 Mac (MPS) & NVIDIA (CUDA) desteği.

🧠 Mantık Katmanı (Logic Layer) Nasıl Çalışır?
Proje, ham veriyi işleyerek anlamlı kararlar verir:

Zaman Kilidi (Time-Latch): Süre sayaçları her karede sıfırlanmaz. Nesne ilk tespit edildiğinde bir "başlangıç damgası" vurulur ve nesne kaybolana kadar bu damga üzerinden fark hesaplanır.

Hassas Tespit: map(int, box.xyxy[0]) kullanılarak koordinatlar tam sayıya çevrilir, bu da daha akıcı ve titremeyen kutular sağlar.

Hata Payı Yönetimi: Anlık nesne kaybolmalarında (false negative) kronometrenin hemen sıfırlanmaması için esnek bir kontrol mekanizmasına sahiptir.

📦 Kurulum ve Çalıştırma
1. Depoyu Klonlayın

Bash
git clone https://github.com/mehmetemindemir/focus-flow.git
cd focus-flow
2. Bağımlılıkları Yükleyin

Bash
pip install ultralytics opencv-python
3. Uygulamayı Başlatın

Bash
python main.py


📈 Yol Haritası (Future Roadmap)
[ ] FastAPI & Streamlit: Projeyi bir web arayüzüne taşımak.

[ ] Daily Analytics: Gün sonunda "Bugün ne kadar odaklı çalıştın?" raporu oluşturmak (Matplotlib entegrasyonu).

[ ] Pose Estimation: YOLOv11-Pose ile kambur duruş uyarısı eklemek.

[ ] Flutter App: Bildirimlerin mobil telefona "Bildirim" olarak düşmesi.
