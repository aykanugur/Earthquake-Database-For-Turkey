
import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import Email


class Login(Tk): #MAIN WINDOW(FIRST PART)
    def __init__(self):
        super().__init__()
        self.configure(bg="#FFFFFF")
        self.title("DEPREM VERI TABANI GIRIS EKRANI")
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 488) // 2
        y = (screen_height - 557) // 2
        self.geometry(f'{488}x{557}+{x}+{y}')

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(
            r"***********************") #ENTER YOUR PATH TO IMAGES

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=557,
            width=488,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=112.5,
            y=244.0,
            width=262.0,
            height=39.0
        )

        # Save PhotoImage references as self attributes
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(243.5, 333.5, image=self.entry_image_2)
        self.entry_2 = Entry(show="*",
                             bd=0,
                             bg="#D9D9D9",
                             fg="#000716",
                             highlightthickness=0)
        self.entry_2.place(
            x=112.5,
            y=313.0,
            width=262.0,
            height=39.0
        )

        self.canvas.create_text(
            110.0,
            225.0,
            anchor="nw",
            text="İsim:",
            fill="#000000",
            font=("Inter BlackItalic", 15 * -1)
        )

        self.canvas.create_text(
            109.0,
            290.0,
            anchor="nw",
            text="Parola:",
            fill="#000000",
            font=("Inter BlackItalic", 15 * -1)
        )

        self.canvas.create_text(
            165.0,
            30.0,
            anchor="nw",
            text="DEPREM VERI TABANI",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(self,
                          image=self.button_image_2,
                          borderwidth=0,
                          highlightthickness=0,
                          command= lambda : self.signIn(),
                          relief="flat")
        button_2.place(
            x=139.0,
            y=390.0,
            width=209.0,
            height=54.0
        )

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(
            244.0,
            138.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.canvas.create_image(
            243.5,
            264.5,
            image=self.entry_image_1
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(self,
                          image=self.button_image_1,
                          borderwidth=0,
                          highlightthickness=0,
                          command=lambda : self.signUp(),
                          relief="flat")
        button_1.place(
            x=137.0,
            y=464.0,
            width=213.0,
            height=50.0
        )

    def signUp(self): #TO OPEN SUB WINDOW (REGISTER)
        import Register
        register = Register.Register(self)
        self.withdraw()
        register.protocol("WM_DELETE_WINDOW", lambda: self.openMain(register)) #ADD PROTOCOL WHEN YOU CLICK (X)


    def show_warning(self, uyari):
        messagebox.showwarning("Uyarı", uyari) #CREATE MSG BOX TO SHOW WARNINGS

    def openMain(self,register): #when you done in sub window, to show login window and destroy sub one
        self.deiconify()
        register.destroy()

    def signIn(self): # to sign in
        email = self.entry_1.get()
        password = self.entry_2.get()
        try:
            Email.email = email
            user = Email.auth_firebase.sign_in_with_email_and_password(email, password) #LOGIN TO USER DATA BASE
            self.destroy()#DESTROY MAIN
        except Exception as e:
            msg = e.args[1]
            msg = msg.split("\n")
            self.show_warning(f"SISTEME GIRIS HATASI: {msg[3]}")
            print(str(e))
        finally:
            try:
                self.entry_1.delete(0, tk.END)
                self.entry_2.delete(0, tk.END)
            except Exception as e: #IF THERE IS NO ERROR TO LOGIN WE DESTROY OUR WINDOW AND THIS CAUSE EXCEPTION (DELETE OBJECT WHICH IS NOT EXISTS)
                pass




