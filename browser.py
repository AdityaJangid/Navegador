import commands, gtk, webkit
a = commands.getoutput("xdpyinfo  | grep -oP 'dimensions:\s+\K\S+'")
b,c = a.split('x')


class  Browser(gtk.Window):
    def __init__(self):
        super(Browser, self).__init__()
        # created our main window
        self.set_default_size(int(b)-100, int(c)-100)

        self.navigation = gtk.HBox()

        #create back, forward, refresh, and search pannel
        #back button
        self.back = gtk.ToolButton(gtk.STOCK_GO_BACK)
        self.frwd = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        self.refresh = gtk.ToolButton(gtk.STOCK_REFRESH)
        self.address_bar = gtk.Entry()


       # #what to do with buttons
        self.back.connect("clicked" , self.go_back)
        self.frwd.connect("clicked" , self.go_frwd)
        self.refresh.connect("clicked" , self.refresh_page)
        self.address_bar.connect("activate" , self.load_page)

        self.navigation.pack_start(self.back, False)
        self.navigation.pack_start(self.frwd, False)
        self.navigation.pack_start(self.refresh, False)
        self.navigation.pack_start(self.address_bar)


        #create view for web pages



        fixed = gtk.Fixed()
        fixed.put(self.back, 0,0)
        fixed.put(self.frwd, 33,0)
        fixed.put(self.refresh, 60,0)
        fixed.put(self.address_bar,110,000 )



        #destroy process when close window
        self.connect('destroy', lambda w: gtk.main_quit())


        #show all things
        self.add(fixed)
        self.show_all()
    def go_back(self, arg1):
        print("test of button for go back")

    def go_frwd(self):
        print("test of button for go forward")
 
    def refresh_page(self, arg1):
        """TODO: Docstring for go_back.
        """
        print("test of button for go refresh page")
 
    def load_page(self, arg1):
        """TODO: Docstring for go_back."""
        print("test of button for go page  ")


Browser()
gtk.main()
