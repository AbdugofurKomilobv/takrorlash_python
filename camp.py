import cv2

def open_camera():
    cap = cv2.VideoCapture(0)  # 0 - default kamera

    if not cap.isOpened():
        print("Kamera ochilmadi!")
        return

    print("Kamera ishga tushdi. Chiqarish uchun 'q' bosing.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kadr o'qib bo'lmadi.")
            break

        cv2.imshow("Kamera", frame)

        # 'q' tugmasi bosilsa, chiqish
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Funktsiyani chaqirish
open_camera()
