import commands
import gtk 
a = commands.getoutput("xdpyinfo  | grep -oP 'dimensions:\s+\K\S+'")
b,c = a.split('x')
class  Browser(gtk.Window):
    def __init__(self):
        super(Browser, self).__init__()
        # created our main window
        self.set_default_size(int(b)-100, int(c)-100)

        #create back, forward, refresh, and search pannel
        #back button











        self.show_all()

Browser()
gtk.main()

