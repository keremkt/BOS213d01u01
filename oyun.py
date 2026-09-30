import tkinter as tk
import random
from tkinter import messagebox

class SayiTahminOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Sayı Tahmin Oyunu")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        # Arka planda 1 ile 100 arasında rastgele bir sayı tutuluyor
        self.hedef_sayi = random.randint(1, 100)
        self.deneme_sayisi = 0

        # Arayüz Elemanları (Kullanıcıdan veri alan ve veri gösteren kısımlar)
        self.baslik_etiketi = tk.Label(root, text="1 ile 100 arasında bir sayı tuttum.\nHadi tahmin et!", font=("Arial", 12))
        self.baslik_etiketi.pack(pady=15)

        # Kullanıcıdan verinin alındığı girdi kutusu
        self.tahmin_girisi = tk.Entry(root, font=("Arial", 14), width=10, justify="center")
        self.tahmin_girisi.pack(pady=5)

        # Tetikleyici buton
        self.tahmin_butonu = tk.Button(root, text="Tahmin Et", command=self.tahmin_kontrol, font=("Arial", 11, "bold"), bg="#4CAF50", fg="white")
        self.tahmin_butonu.pack(pady=10)

        # Sonucun (verinin) kullanıcıya döndürüldüğü etiket
        self.sonuc_etiketi = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.sonuc_etiketi.pack(pady=5)

        self.yeniden_butonu = tk.Button(root, text="Yeniden Oyna", command=self.oyunu_sifirla, font=("Arial", 10), state=tk.DISABLED)
        self.yeniden_butonu.pack(pady=5)

    def tahmin_kontrol(self):
        try:
            # Girdi kutusundan veriyi al ve tam sayıya çevir
            tahmin = int(self.tahmin_girisi.get())
            self.deneme_sayisi += 1

            # Mantıksal karşılaştırma ve kullanıcıya veri (sonuç) döndürme
            if tahmin < self.hedef_sayi:
                self.sonuc_etiketi.config(text="Daha büyük bir sayı gir! ⬆️", fg="blue")
            elif tahmin > self.hedef_sayi:
                self.sonuc_etiketi.config(text="Daha küçük bir sayı gir! ⬇️", fg="red")
            else:
                self.sonuc_etiketi.config(text=f"Tebrikler! 🎉 {self.deneme_sayisi}. denemede buldun!", fg="green")
                self.tahmin_butonu.config(state=tk.DISABLED)
                self.yeniden_butonu.config(state=tk.NORMAL)
        except ValueError:
            # Kullanıcı harf veya boşluk girerse hata ver
            messagebox.showwarning("Hata", "Lütfen sadece sayı girin!")
        
        # Her tahminden sonra girdi kutusunu temizle
        self.tahmin_girisi.delete(0, tk.END)

    def oyunu_sifirla(self):
        # Oyunu başlangıç ayarlarına döndür
        self.hedef_sayi = random.randint(1, 100)
        self.deneme_sayisi = 0
        self.sonuc_etiketi.config(text="")
        self.tahmin_butonu.config(state=tk.NORMAL)
        self.yeniden_butonu.config(state=tk.DISABLED)
        self.tahmin_girisi.delete(0, tk.END)

# Siyah konsol ekranı yerine modern bir pencere açar
if __name__ == "__main__":
    pencere = tk.Tk()
    oyun = SayiTahminOyunu(pencere)
    pencere.mainloop()
