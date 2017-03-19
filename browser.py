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
        self.back = gtk.ToolButton(gtk.STOCK_GO_BACK)
        self.frwd = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        self.address_bar = gtk.Entry()


        fixed = gtk.Fixed()
        fixed.put(self.back, 0,0)
        fixed.put(self.frwd, 30,0)
        fixed.put(self.address_bar, )



        #close process when close window
        self.connect('destroy', lambda w: gtk.main_quit())


        #show all things
        self.add(fixed)
        self.show_all()


Browser()
gtk.main()
