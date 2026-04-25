🚀 Focus-Flow: AI Productivity Tracker (YOLOv11)
Focus-Flow, çalışma ortamınızı gerçek zamanlı olarak analiz eden ve verimliliğinizi artırmak için tasarlanmış bir yapay zeka asistanıdır. YOLOv11 nesne tespit modelini kullanarak odak durumunuzu takip eder ve dikkatiniz dağıldığında sizi uyarır.

✨ Özellikler
Gerçek Zamanlı Odak Takibi: Çalışma masanızdaki nesneleri (Kitap, Laptop, Telefon) anlık olarak tanır.

Akıllı Uyarı Sistemi: Telefon tespit edildiğinde görsel uyarılar vererek odak kaybını önler.

Sağlık Hatırlatıcıları: Çalışma sırasında su içmeyi unutursanız ekranda hatırlatıcılar çıkarır.

Yüksek Performans: YOLOv11 Nano modeli sayesinde ASUS (NVIDIA) ve MacBook Air M1 cihazlarda yüksek FPS ile çalışır.

🛠️ Teknoloji Yığını
AI/Vision: Ultralytics YOLOv11

Framework: Python 3.x

Library: OpenCV, Time

Hardware: ASUS Laptop (NVIDIA GPU Optimized) & M1 Mac Support

📦 Kurulum
Depoyu Klonlayın:

Bash
git clone https://github.com/kullanici-adin/focus-flow.git
cd focus-flow
Gerekli Kütüphaneleri Yükleyin:

Bash
pip install ultralytics opencv-python
Projeyi Çalıştırın:

Bash
python main.py
🧠 Mantık Katmanı (Logic Layer)
Bu proje sadece nesne tespiti yapmaz, aynı zamanda tespit edilen nesneler arasında bir mantık kurar:

Dikkat Dağıtıcı Kontrolü: cell phone sınıfı 2 saniyeden uzun süre tespit edilirse ekran kırmızıya döner.

Çalışma Modu: book veya laptop görüldüğünde sistem "ÇALIŞIYOR" moduna geçer.

Hydration Alert: Görüntüde bottle yoksa su içme hatırlatıcısı aktif kalır.

📈 Gelecek Planları
[ ] Flutter Entegrasyonu: Mobil uygulama üzerinden anlık bildirimler göndermek.

[ ] FastAPI Backend: Görüntü işlemeyi sunucu tarafına taşıyarak daha hafif bir istemci oluşturmak.

[ ] Duruş Analizi: YOLOv11-Pose kullanarak çalışma sırasında yanlış oturuş uyarısı eklemek.

🤝 Katkıda Bulunma
Bu bir öğrenci projesidir ve her türlü katkıya açıktır. Herhangi bir sorunuz varsa bir Issue açmaktan çekinmeyin!

Geliştiren: Mehmet Emin Demir - Gümüşhane Üniversitesi Yazılım Mühendisliği Öğrencisi
