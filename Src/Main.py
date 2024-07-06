import sys
import Login
import Email
import Menu
#START THE FIRST PART OF APP
loginMainWindow = Login.Login()
loginMainWindow.mainloop()
#END OF FIRST PART
if Email.email is not None: #START SECOND PART IF YOU SIGN IN OR SIGN UP
    menu = Menu.Menu()
    menu.mainloop()
    sys.exit(0)