import cv2
from ultralytics import YOLO
import time

# 1. Modeli Yükle (YOLOv11 Nano - Hızlı ve M1 dostu)
model = YOLO('yolo11n.pt')

# 2. Kamera Bağlantısını Aç
cap = cv2.VideoCapture(0)

# Değişkenler
phone_detected_start = 0
is_distracted = False

print("Focus-Flow Başlatıldı! Çıkmak için 'q' tuşuna basın.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Görüntüyü YOLOv11 ile tara
    # stream=True ve device='mps' (M1 Mac hızlandırması için) eklenebilir
    results = model(frame, verbose=False)

    # Tespit edilen nesneleri kontrol et
    current_classes = []
    
    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            current_classes.append(label)

            # Sadece ilgilendiğimiz nesneleri kutu içine alalım (Opsiyonel)
            if label in ['cell phone', 'book', 'bottle', 'laptop']:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

    # --- MANTIK KATMAMI (LOGIC LAYER) ---

    # 1. Telefon tespiti uyarısı
    if 'cell phone' in current_classes:
        if not is_distracted:
            phone_detected_start = time.time()
            is_distracted = True
        
        # Eğer telefon 2 saniyeden uzun süredir ekrandaysa uyarı ver
        if time.time() - phone_detected_start > 2:
            cv2.putText(frame, "DIKKAT: TELEFONU BIRAK VE ODAKLAN!", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            # Ekranı kırmızı bir çerçeveyle kapla
            cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[2]), (0, 0, 255), 10)
    else:
        is_distracted = False

    # 2. Çalışma durumu tespiti
    if 'book' in current_classes or 'laptop' in current_classes:
        cv2.putText(frame, "MOD: CALISIYOR", (50, 450), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # 3. Su içme hatırlatıcısı (Basit mantık)
    if 'bottle' not in current_classes:
        cv2.putText(frame, "Hatirlatma: Su icmeyi unutma!", (50, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    # Görüntüyü göster
    cv2.imshow("Focus-Flow: AI Productivity Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()