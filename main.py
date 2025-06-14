import qrcode
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

OUTPUT_FOLDER = "output"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def generate_qr():
    data = entry_data.get().strip()
    filename = entry_filename.get().strip()

    if not data:
        messagebox.showwarning("هشدار", "لطفاً یک متن یا لینک وارد کنید.")
        return

    if not filename:
        filename = "qr_code"

    if not filename.endswith(".png"):
        filename += ".png"

    path = os.path.join(OUTPUT_FOLDER, filename)

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)

    show_qr(path)
    messagebox.showinfo("موفقیت", f"کد QR با موفقیت ذخیره شد:\n{path}")

def show_qr(image_path):
    img = Image.open(image_path)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

def clear():
    entry_data.delete(0, END)
    entry_filename.delete(0, END)
    qr_label.config(image='')

root = Tk()
root.title("تولیدکننده کد QR - نسخه گرافیکی")
root.geometry("400x450")
root.resizable(False, False)

Label(root, text="🔹 متن یا لینک را وارد کنید:", font=("B Nazanin", 12)).pack(pady=5)
entry_data = Entry(root, width=40, font=("Arial", 12))
entry_data.pack(pady=5)

Label(root, text="🔹 نام فایل خروجی:", font=("B Nazanin", 12)).pack(pady=5)
entry_filename = Entry(root, width=40, font=("Arial", 12))
entry_filename.pack(pady=5)

Button(root, text="✅ تولید کد QR", command=generate_qr, bg="green", fg="white", width=20).pack(pady=10)
Button(root, text="🧹 پاک کردن", command=clear, width=20).pack()

qr_label = Label(root)
qr_label.pack(pady=15)

Label(root, text="ساخته شده با ❤️ توسط مهندس محمد جواد نوروزی", font=("Arial", 10, "italic")).pack(pady=5)

root.mainloop()
