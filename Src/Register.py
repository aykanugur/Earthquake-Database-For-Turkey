import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, Button, PhotoImage, messagebox, ttk
import Email
from firebase_admin import db,auth

class Register(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="#FFFFFF")
        self.title("DEPREM VERI TABANI KAYIT EKRANI")
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 488) // 2
        y = (screen_height - 792) // 2
        self.geometry(f'{488}x{792}+{x}+{y}')
        self.parent = parent
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"***********************") #ENTER YOUR PATH TO IMAGES

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=792,
            width=488,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(243.0, 146.0, image=self.image_image_1)

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(243.5, 264.5, image=self.entry_image_1)
        self.entry_1 = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=112.5, y=244.0, width=262.0, height=39.0)

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(243.5, 333.5, image=self.entry_image_2)
        self.entry_2 = Entry(self, show="*", bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=112.5, y=313.0, width=262.0, height=39.0)

        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(243.5, 404.5, image=self.entry_image_3)
        self.entry_3 = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=112.5, y=384.0, width=262.0, height=39.0)

        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(243.5, 476.5, image=self.entry_image_4)
        self.entry_4 = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=112.5, y=456.0, width=262.0, height=39.0)

        self.canvas.create_text(106.0, 214.0, anchor="nw", text="Email:", fill="#000000", font=("Inter BlackItalic", 15 * -1))
        self.canvas.create_text(113.0, 285.0, anchor="nw", text="Şifre:", fill="#000000", font=("Inter BlackItalic", 15 * -1))
        self.canvas.create_text(115.0, 354.0, anchor="nw", text="İsim:", fill="#000000", font=("Inter BlackItalic", 15 * -1))
        self.canvas.create_text(100.0, 426.0, anchor="nw", text="Soyad:", fill="#000000", font=("Inter BlackItalic", 15 * -1))
        self.canvas.create_text(111.0, 503.0, anchor="nw", text="Sehir:", fill="#000000", font=("Inter BlackItalic", 15 * -1))
        self.canvas.create_text(86.0, 605.0, anchor="nw", text="Cinsiyet:", fill="#000000", font=("Inter BlackItalic", 15 * -1))
        self.canvas.create_text(111.0, 30.0, anchor="nw", text="DEPREM VERI TABANI KAYIT EKRANI", fill="#000000", font=("Inter SemiBold", 15 * -1))

        self.sehirler = [
            "ADANA", "ADIYAMAN", "AFYONKARAHISAR", "AGRI", "AMASYA", "ANKARA", "ANTALYA", "ARTVIN", "AYDIN",
            "BALIKESIR", "BILECIK", "BINGOL", "BITLIS", "BOLU", "BURDUR", "BURSA", "CANAKKALE", "CANKIRI", "CORUM",
            "DENIZLI", "DIYARBAKIR", "EDIRNE", "ELAZIG", "ERZINCAN", "ERZURUM", "ESKISEHIR", "GAZIANTEP", "GIRESUN",
            "GUMUSHANE", "HAKKARI", "HATAY", "ISPARTA", "MERSIN", "ISTANBUL", "IZMIR", "KARS", "KASTAMONU", "KAYSERI",
            "KIRKLARELI", "KIRSEHIR", "KOCAELI", "KONYA", "KUTAHYA", "MALATYA", "MANISA", "KAHRAMANMARAS", "MARDIN",
            "MUGLA", "MUS", "NEVSEHIR", "NIGDE", "ORDU", "RIZE", "SAKARYA", "SAMSUN", "SIIRT", "SINOP", "SIVAS",
            "TEKIRDAG", "TOKAT", "TRABZON", "TUNCELI", "SANLIURFA", "USAK", "VAN", "YOZGAT", "ZONGULDAK", "AKSARAY",
            "BAYBURT", "KARAMAN", "KIRIKKALE", "BATMAN", "SIRNAK", "BARTIN", "ARDAHAN", "IGDIR", "YALOVA", "KARABUK",
            "KILIS", "OSMANIYE", "DUZCE"
        ]

        self.comboBox = ttk.Combobox(self, state="readonly", values=self.sehirler)
        self.comboBox.place(x=112.5, y=530.0, width=262.0, height=39.0)
        self.comboBox.bind("<<ComboboxSelected>>", self.on_select_city)

        self.cinsiyetler = ["ERKEK", "KADIN", "BELIRTMEK ISTEMIYORUM"]
        self.comboBox_gender = ttk.Combobox(self, state="readonly", values=self.cinsiyetler)
        self.comboBox_gender.place(x=112.5, y=640.0, width=262.0, height=39.0)
        self.comboBox_gender.bind("<<ComboboxSelected>>", self.on_select_gender)

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.signUp, relief="flat")
        self.button_1.place(x=131.0, y=722.0, width=226.0, height=38.0)

        self.gender = ""
        self.city = ""

    def on_select_city(self, event):
        self.city = self.comboBox.get()

    def on_select_gender(self, event):
        self.gender = self.comboBox_gender.get()

    def show_warning(self, uyari):
        messagebox.showwarning("Uyarı", uyari)

    def signUp(self):

        email = self.entry_1.get()
        password = self.entry_2.get()
        name = self.entry_3.get()
        surname = self.entry_4.get()
        try:
            Email.email = email
            user = Email.auth_firebase.create_user_with_email_and_password(email,password)
            user_uid = auth.get_user_by_email(email).uid
            ref = db.reference('users/' + user_uid)
            ref.set({
                'name': name,
                'city': self.city,
                'surname': surname,
                'email': email,
                'gender': self.gender
            })
            user = Email.auth_firebase.sign_in_with_email_and_password(email, password)
            self.parent.destroy()
        except Exception as e:
            self.show_warning(str(e))
        finally:
            try:
                self.entry_1.delete(0, tk.END)
                self.etry_2.delete(0, tk.END)
            except Exception as a:
              pass

