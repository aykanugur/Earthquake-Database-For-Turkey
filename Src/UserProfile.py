
from pathlib import Path
from tkinter import  Canvas, Entry,  Button, PhotoImage,ttk
from tkinter import Toplevel
from firebase_admin import auth,db
#THIS CLASS IS SUB WINDOW OF MENU
class UserProfile(Toplevel):
    def __init__(self,email,parent):
        super().__init__(parent)
        self.user_uid = auth.get_user_by_email(email).uid
        self.ref = db.reference('users/' + self.user_uid)
        user_data = self.ref.get()
        self.parent = parent
        user_data_array = []
        self.password = None
        for i in user_data.values(): #DATA FROM DATA_BASE (USER DATA)
            user_data_array.append(i)
        self.city = user_data_array[0]
        self.email = user_data_array[1]
        self.gender = user_data_array[2]
        self.name = user_data_array[3]
        self.surname = user_data_array[4]

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"***********************") #IMAGES PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.configure(bg="#FFF2F2")   #WINDOW SETTINGS
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 488) // 2
        y = (screen_height - 792) // 2
        self.geometry(f'{488}x{792}+{x}+{y}')

        self.canvas = Canvas(
            self,
            bg="#FFF2F2",
            height=792,
            width=488,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            243.5,
            264.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(self,
            bd=0,
            bg="#E5E0FF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=112.5,
            y=244.0,
            width=262.0,
            height=39.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            243.5,
            333.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(self,
            bd=0,
            bg="#E5E0FF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=112.5,
            y=313.0,
            width=262.0,
            height=39.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            243.5,
            404.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(self,
            bd=0,
            bg="#E5E0FF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=112.5,
            y=384.0,
            width=262.0,
            height=39.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            243.5,
            476.5,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(self,
            bd=0,
            bg="#E5E0FF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=112.5,
            y=456.0,
            width=262.0,
            height=39.0
        )

        self.canvas.create_text(
            106.0,
            214.0,
            anchor="nw",
            text="Email:",
            fill="#000000",
            font=("Inter BlackItalic", 15 * -1)
        )

        self.canvas.create_text(
            113.0,
            285.0,
            anchor="nw",
            text="Şifre:",
            fill="#000000",
            font=("Inter BlackItalic", 15 * -1)
        )

        self.canvas.create_text(
            115.0,
            354.0,
            anchor="nw",
            text="İsim:",
            fill="#000000",
            font=("Inter BlackItalic", 15 * -1)
        )

        self.canvas.create_text(
            111.0,
            503.0,
            anchor="nw",
            text="Sehir:",
            fill="#000000",
            font=("Inter BlackItalic", 15 * -1)
        )

        self.canvas.create_text(
            86.0,
            605.0,
            anchor="nw",
            text="Cinsiyet:",
            fill="#000000",
            font=("Inter BlackItalic", 15 * -1)
        )

        self.canvas.create_text(
            100.0,
            426.0,
            anchor="nw",
            text="Soy isim:",
            fill="#000000",
            font=("Inter BlackItalic", 15 * -1)
        )

        self.canvas.create_text(
            86.0,
            30.0,
            anchor="nw",
            text="DEPREM VERI TABANI KULLANICI BILGILERI",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.updateEverything(),
            relief="flat"
        )
        self.button_1.place(
            x=131.0,
            y=722.0,
            width=226.0,
            height=38.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            150.0,
            130.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self. image_2 = self.canvas.create_image(
            222.34536743164062,
            87.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            224.34536743164062,
            130.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            224.34536743164062,
            167.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            249.34536743164062,
            80.0,
            anchor="nw",
            text="{}".format(self.email),
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            108.34536743164062,
            194.0,
            anchor="nw",
            text="{} {}".format(self.name, self.surname),
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            249.34536743164062,
            121.0,
            anchor="nw",
            text="Şehir : {}".format(self.city),
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            249.34536743164062,
            158.0,
            anchor="nw",
            text="Cinsiyet : {}".format(self.gender),
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        def on_select(event):
            selected_city = self.comboBox.get()
            self.city = selected_city

        self.sehirler = [
            "ADANA", "ADIYAMAN", "AFYONKARAHISAR", "AGRI", "AMASYA", "ANKARA", "ANTALYA", "ARTVIN", "AYDIN",
            "BALIKESIR",
            "BILECIK", "BINGOL", "BITLIS", "BOLU", "BURDUR", "BURSA", "CANAKKALE", "CANKIRI", "CORUM", "DENIZLI",
            "DIYARBAKIR",
            "EDIRNE", "ELAZIG", "ERZINCAN", "ERZURUM", "ESKISEHIR", "GAZIANTEP", "GIRESUN", "GUMUSHANE", "HAKKARI",
            "HATAY",
            "ISPARTA", "MERSIN", "ISTANBUL", "IZMIR", "KARS", "KASTAMONU", "KAYSERI", "KIRKLARELI", "KIRSEHIR",
            "KOCAELI",
            "KONYA", "KUTAHYA", "MALATYA", "MANISA", "KAHRAMANMARAS", "MARDIN", "MUGLA", "MUS", "NEVSEHIR", "NIGDE",
            "ORDU",
            "RIZE", "SAKARYA", "SAMSUN", "SIIRT", "SINOP", "SIVAS", "TEKIRDAG", "TOKAT", "TRABZON", "TUNCELI",
            "SANLIURFA",
            "USAK", "VAN", "YOZGAT", "ZONGULDAK", "AKSARAY", "BAYBURT", "KARAMAN", "KIRIKKALE", "BATMAN", "SIRNAK",
            "BARTIN",
            "ARDAHAN", "IGDIR", "YALOVA", "KARABUK", "KILIS", "OSMANIYE", "DUZCE"
        ]
        self.comboBox = ttk.Combobox(state="readonly", values=self.sehirler,master=self)
        self.comboBox.place(x=112.5,
                       y=530.0,
                       width=262.0,
                       height=39.0)
        self.comboBox.bind("<<ComboboxSelected>>", on_select)

        def on_select_gender(event):
            self.gender = self.comboBox_gender.get()

        self.cinsiyetler = ["ERKEK", "KADIN", "BELIRTMEK ISTEMIYORUM"]
        self.comboBox_gender = ttk.Combobox(state="readonly", values=self.cinsiyetler,master=self)
        self.comboBox_gender.place(x=112.5,
                              y=640.0,
                              width=262.0,
                              height=39.0)
        self.comboBox_gender.bind("<<ComboboxSelected>>", on_select_gender)

    def updateEverything(self): # WHEN YOU CLICKED THE BUTTON THIS METHOD IS WORKING

        if self.entry_1.get() != "":
            self.email = self.entry_1.get()
        if self.entry_2.get() != "":
            self.password = self.entry_2.get()
            auth.update_user(self.user_uid, password=self.password)
        if self.entry_3.get() != "":
            self.name = self.entry_3.get()
        if self.entry_4.get() != "":
            self.surname = self.entry_4.get()
        auth.update_user(self.user_uid, email=self.email)
        self.ref.set({
            'name': self.name,
            'city': self.city,
            'surname': self.surname,
            'email': self.email,
            'gender': self.gender
        })
        #USER DATA BASE UPDATED
        self.parent.updatedVal() #CHANGE VARIABLES IN PARENT WINDOW (MENU)
        self.destroy()






