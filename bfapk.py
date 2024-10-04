from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from pyaxmlparser import APK
import subprocess


def select_file():
    global filename
    filename = filedialog.askopenfilename()
    print("File:", filename)
    selected_file_text.delete(1.0, END)
    selected_file_text.insert(END, "Seçilen Dosya:\n" + filename)



def decompile_apk():
    global filename
    if not filename:
        messagebox.showerror("File Error", "Lütfen bir APK dosyası seçin.")
        return

    # Dosyanın uzantısını kontrol et
    if not filename.endswith('.apk'):
        messagebox.showerror("File Error", "Bu dosya APK değil!")
        return

    # Seçilen dosyanın dizinini al
    directory = os.path.dirname(filename)

    # Apktool kullanarak apk dosyasını decompile et
    process = subprocess.Popen(["apktool", "d", filename, "-o", f"{directory}/output_folder"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        messagebox.showinfo("Decompile Successful", "APK parçalandı!")
        # Main aktiviteyi göster
        show_main_activity(directory)
    else:
        messagebox.showerror("Decompile Error", f"APK parçalanırken bir hata oluştu:\n{stderr.decode()}")


def show_main_activity(directory):
    # APK'nin yolunu al
    apk_path = os.path.join(directory, "output_folder", "AndroidManifest.xml")

    # APK'yi aç
    a = APK(apk_path)

    # Ana aktiviteyi bul
    main_activity = a.get_main_activity()

    # Ana aktiviteyi göster
    messagebox.showinfo("Main Activity", f"Ana aktivite: {main_activity}")

    # Decompiled dosyanın dizinini göster
    decompiled_path = os.path.join(directory, "output_folder")
    selected_file_text.insert(END, "\n\nDecompile Edilen Dosya Dizini:\n" + decompiled_path)

def compile_apk():
    global filename
    if not filename:
        messagebox.showerror("File Error", "Lütfen bir APK dosyası seçin.")
        return

    # Seçilen dosyanın dizinini al
    directory = os.path.dirname(filename)

    # Apktool kullanarak decompile edilen dosyayı yeniden compile et
    process = subprocess.Popen(["apktool", "b", f"{directory}/output_folder", "-o", f"{directory}/compiled_apk.apk"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        messagebox.showinfo("Compile Successful", "APK Onarıldı!")
    else:
        messagebox.showerror("Compile Error", f"APK Onarılırken bir hata oluştu:\n{stderr.decode()}")


master = Tk()
# Görseli yükle ve PhotoImage nesnesine dönüştür
background_image = Image.open("mtrx.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Canvas oluştur ve arka plan rengini beyaz yap
canvas = Canvas(master, height=650, width=750, bg='white')
canvas.pack()

# Arkaplan görselini canvas üzerine yerleştir
canvas.create_image(0, 0, anchor=NW, image=background_photo)

master.title("BlackFes DecApk")

frame_ust = Frame(master, bg='black')
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

select_file_button = Button(frame_ust, text="Dosya Seç", command=select_file)
select_file_button.pack(side=LEFT, padx=(10, 5), pady=10)  # Parçala butonunu sol tarafta yerleştir

logo_img = Image.open("bfust.png")
logo_img = logo_img.resize((600, 70), Image.BILINEAR)
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = Label(master, image=logo_photo, bg='grey')
logo_label.image = logo_photo
logo_label.place(relx=0.5, rely=0.05, anchor=CENTER)


frame_alt_sag = Frame(master, bg='black')
frame_alt_sag.place(relx=0.1, rely=0.21, relwidth=0.8, relheight=0.7)

selected_file_text = Text(frame_alt_sag, bg='black', fg='green', font=("Terminal", 8), wrap=WORD)
selected_file_text.pack(side=TOP, padx=10, pady=(30, 5), fill=BOTH, expand=True)


alt_sol_button = Button(frame_ust, text="Parçala!", command=decompile_apk)
alt_sol_button.pack(side=LEFT, padx=(5, 10), pady=10)  # Parçala butonunu sol tarafta yerleştir

onar_button = Button(frame_ust, text="Onar", command=compile_apk)
onar_button.pack(side=LEFT, padx=(5, 10), pady=10)

filename = None


master.mainloop()
