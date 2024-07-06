import re

import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import time
from tkinter.ttk import Treeview
import Email
import UserProfile
from firebase_admin import auth,db

#SECOND MAIN
class Menu(Tk):
    def __init__(self):
        super().__init__()
        self.depremDataFrame = pd.DataFrame(
            columns=['Tarih', 'Saat', 'Enlem', 'Boylam', 'Derinlik', 'MD', 'ML', 'MW', 'Yer'])
        self.city = None
        self.email = None
        self.gender = None
        self.name = None
        self.surname = None
        self.user_uid = auth.get_user_by_email(Email.email).uid
        self.user = auth.get_user(self.user_uid)
        self.ref = db.reference('users/' + self.user_uid) #CREATE REF
        self.updateVariables() #TO UPDATE VARIABLES COME FROM USER DATA BASE
        self.simpledepremdataframe = pd.DataFrame(columns = ['Tarih', 'Saat',"Buyukluk","Sehir"])
        self.order = True
        self.is_simple = False
        self.AccessData()

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(
            r"***********************") #ENTER YOUR PATH TO IMAGES

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.title("MENU")
        self.geometry("905x750")
        self.configure(bg="#E8D4D4")

        self.canvas = Canvas(
            self,
            bg="#E8D4D4",
            height=750,
            width=905,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            708.0,
            1393.0,
            750.0,
            fill="#8EA7E9",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1230.0,
            42.0,
            fill="#8EA7E9",
            outline="")
        unvan = None
        if (self.gender == "ERKEK"):
            unvan = "Bey"
        elif (self.gender == "KADIN"):
            unvan = "Hanım"
        else:
            unvan = ""
        self.msg = ""
        if ((time.localtime().tm_hour > 19) or time.localtime().tm_hour < 6):
            self.msg = "İyi Akşamlar"
        elif (time.localtime().tm_hour < 19 and time.localtime().tm_hour > 11):
            self.msg = "Tünaydınlar"
        else:
            self.msg = "Günaydın"

        self.text_hi = self.canvas.create_text(  # to do change text
            9.0,
            47.0,
            anchor="nw",
            text="{2}\n{0} {1} ".format(self.name, unvan, self.msg),
            fill="#000000",
            font=("Inter ExtraBold", 50 * -1)
        )


        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openUserProfileToplevelWindow(),
            relief="flat"
        )
        button_2.place(
            x=668.0,
            y=74.0,
            width=226.0,
            height=38.0
        )
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("Simple.png"))
        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: decideSimpleOrNot(),
            relief="flat"
        )



        def decideSimpleOrNot():
            if self.is_simple:
                self.setTree(self.depremDataFrame, 1, 0) #1 mean yes, 0 mean no
                self.is_simple = False
            else:
                self.setTree(self.simpledepremdataframe, 1, 1)
                self.is_simple = True

        button_3.place(
            x=320.0,
            y=235.0,
            width=226.0,
            height=38.0
        )

        self.canvas.create_text(
            145.0,
            297.0,
            anchor="nw",
            text="SON DEPREMLER",
            fill="#000000",
            font=("Itim Regular", 20 * -1)
        )

        self.canvas.create_text(
            547.0,
            297.0,
            anchor="nw",
            text="SON DEPREMLER(SEHRINIZ)",
            fill="#000000",
            font=("Itim Regular", 20 * -1)
        )
        self.canvas.create_rectangle(
            460.0,
            341.0,
            893.0,
            733.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            9.0,
            341.0,
            442.0,
            733.0,
            fill="#D9D9D9",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            647.0,
            87.0,
            image=self.image_image_1
        )
        self.setTree(dataframe=self.depremDataFrame)

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            110.0,
            309.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            520.0,
            305.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            850.0,
            305.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            350.0,
            309.0,
            image=self.image_image_6
        )

        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 905) // 2
        y = (screen_height - 750) // 2
        self.geometry(f'{905}x{750}+{x}+{y}')

    def sortValuesInList(self, col, dataframe):
        # Toggle sorting order
        self.order = not self.order

        # Sort DataFrame
        dataframe.sort_values(col, ascending=self.order, inplace=True)

        # Clear Treeview
        for item in self.genelDepremlerListBox.get_children():
            self.genelDepremlerListBox.delete(item)

        # Insert sorted data into Treeview
        for index, row in dataframe.iterrows():
            self.genelDepremlerListBox.insert("", "end", values=list(row))

    def sortValuesInList2(self, col, dataframe):
        # Toggle sorting order
        self.order = not self.order

        # Sort DataFrame
        dataframe.sort_values(col, ascending=self.order, inplace=True)

        # Clear Treeview
        for item in self.genelDepremlerListSehirBox.get_children():
            self.genelDepremlerListSehirBox.delete(item)

        # Insert sorted data into Treeview
        if self.is_simple:
            for index, row in dataframe.iterrows():
                values = list(row)
                if (values[len(values) - 1] == self.city) or (values[len(values) - 2] == self.city):
                    self.genelDepremlerListSehirBox.insert("", "end", values=values)
        else:
            for index, row in dataframe.iterrows():
                line = " ".join(map(str, row))
                pattern = r'\(.*?\)'
                matches = re.findall(pattern, line)
                city = str([s[1:-1] for s in matches])
                city = city.strip('[]')
                city = city.strip("''")
                if city == self.city:
                    self.genelDepremlerListSehirBox.insert("", "end", values=list(row))

    def setTree(self, dataframe, destroyValue=0, matchValue=0):
        if destroyValue == 1:
            self.genelDepremlerListSehirBox.destroy()
            self.genelDepremlerListBox.destroy()

        self.genelDepremlerListBox = Treeview()
        self.genelDepremlerListBox["columns"] = list(dataframe.columns)
        self.genelDepremlerListBox.place(x=9.0, y=341.0, width=442.0, height=733.0)
        self.genelDepremlerListBox["show"] = "headings"

        self.genelDepremlerListBox["columns"] = list(dataframe.columns)
        for col in dataframe.columns:
            self.genelDepremlerListBox.heading(col, text=col,
                                               command=lambda c=col: self.sortValuesInList(c, dataframe))
            self.genelDepremlerListBox.column(col, width=20)

        for index, row in dataframe.iterrows():
            self.genelDepremlerListBox.insert("", "end", values=list(row))

        self.genelDepremlerListBox.place(x=9, y=341, width=433.0, height=392.0)

        self.genelDepremlerListSehirBox = Treeview(self)
        self.genelDepremlerListSehirBox["columns"] = list(dataframe.columns)
        self.genelDepremlerListSehirBox["show"] = "headings"

        for col in dataframe.columns:
            self.genelDepremlerListSehirBox.heading(col, text=col,
                                                    command=lambda c=col: self.sortValuesInList2(c,
                                                                                                 dataframe=dataframe))
            self.genelDepremlerListSehirBox.column(col, width=20)

        if matchValue == 0:
            for index, row in dataframe.iterrows():
                line = " ".join(map(str, row))
                pattern = r'\(.*?\)'
                matches = re.findall(pattern, line)
                city = str([s[1:-1] for s in matches])
                city = city.strip('[]')
                city = city.strip("''")
                if city == self.city:
                    self.genelDepremlerListSehirBox.insert("", "end", values=list(row))
        else:
            for index, row in dataframe.iterrows():
                values = list(row)
                if (values[len(values) - 1] == self.city) or (values[len(values) - 2] == self.city):
                    self.genelDepremlerListSehirBox.insert("", "end", values=values)

        self.genelDepremlerListSehirBox.place(x=460.0, y=341.0, width=433.0, height=392.0)

    def openUserProfileToplevelWindow(self):

        userprofile = UserProfile.UserProfile(Email.email,self)
        self.withdraw()
        userprofile.protocol("WM_DELETE_WINDOW", lambda: self.openMainMenu(userprofile))

    def updatedVal(self):
        self.updateVariables()
        unvan = None

        if (self.gender == "ERKEK"):
            unvan = "Bey"
        elif (self.gender == "KADIN"):
            unvan = "Hanım"
        else:
            unvan = ""

        self.canvas.itemconfig(self.text_hi,text="{2}\n{0} {1} ".format(self.name, unvan, self.msg))
        self.setTree(dataframe=self.depremDataFrame)
        self.deiconify()

    def openMainMenu(self, userprofile):
        self.deiconify()
        userprofile.destroy()

    def updateVariables(self):
        user_data = self.ref.get()
        user_data_array = []
        for i in user_data.values():
            user_data_array.append(i)
        self.city = user_data_array[0]
        self.email = user_data_array[1]
        self.gender = user_data_array[2]
        self.name = user_data_array[3]
        self.surname = user_data_array[4]
    def AccessData(self):
        pattern = r'\(.*?\)'
        url = 'http://www.koeri.boun.edu.tr/scripts/lst6.asp' #WEBSITE WHICH WE PULL DATA
        page = requests.get(url)
        bs = BeautifulSoup(page.content, 'html.parser')
        bs.prettify()
        text = None
        for i in bs.find_all('pre'):
            text = i.text
        dataFromWeb = np.array(text.split('\n'))
        dataFromWeb = dataFromWeb[7:len(dataFromWeb) - 2]
        for i in dataFromWeb:
            text = i.replace('\n', '')
            components = text.split()
            newDataSeries = pd.Series({
                "Tarih": components[0],
                "Saat": components[1],
                "Enlem": components[2],
                "Boylam": components[3],
                "Derinlik": components[4],
                "MD": components[5],
                "ML": components[6],
                "MW": components[7],
                "Yer": ' '.join(components[8:])
            })
            matches = re.findall(pattern, ' '.join(components[8:]))
            city = str([s[1:-1] for s in matches])
            city = str([s[1:-1] for s in matches])
            city = city.strip('[]')
            city = city.strip("''")
            newDataSeriesSimple = pd.Series({"Tarih": components[0],"Saat": components[1],"Buyukluk": components[6],"Sehir": city})
            self.simpledepremdataframe = self.simpledepremdataframe._append(newDataSeriesSimple,ignore_index=True)
            self.depremDataFrame = self.depremDataFrame._append(newDataSeries, ignore_index=True)
        self.depremDataFrame.index.name = 'INDEXES'
        self.simpledepremdataframe.index.name = 'INDEXES'









