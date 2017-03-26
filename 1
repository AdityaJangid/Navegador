import commands, gtk, webkit
a = commands.getoutput("xdpyinfo  | grep -oP 'dimensions:\s+\K\S+'")
b,c = a.split('x')


class  Browser(gtk.Window):
    def __init__(self):
        super(Browser, self).__init__()
        # created our main window
        self.set_icon_from_file('why.png')
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
        self.view = gtk.ScrolledWindow()
        self.webview = webkit.WebView()
        self.webview.open('http://www.google.com')
        self.webview.connect('title-changed', self.change_title)
        self.webview.connect('load-committed', self.change_url)
        self.view.add(self.webview)


        #Added everything and initialize
        self.container = gtk.VBox()
        self.container.pack_start(self.navigation, False)
        self.container.pack_start(self.view)

        self.add(self.container)

        self.show_all()

#        fixed = gtk.Fixed()
#        fixed.put(self.back, 0,0)
#        fixed.put(self.frwd, 33,0)
#        fixed.put(self.refresh, 60,0)
#        fixed.put(self.address_bar,110,000 )
#        fixed.put(self.container, 500,500)
#


        #destroy process when close window
        self.connect('destroy', lambda w: gtk.main_quit())


        #show all things
#        self.add(fixed)
    def go_back(self, arg1):
        self.webview.go_back()

    def go_frwd(self):
        self.webview.go_forward()
 
    def refresh_page(self, arg1):
        self.webview.reload()
 
    def load_page(self, widget):
        add = self.address_bar.get_text()
        if add.startswith('http://') or add.startswith('https://'):
            self.webview.open(add)
        else:
            add = 'http://' + add
            self.address_bar.set_text(add)
            self.webview.open(add)


    def change_title(self, widget, frame, title):
        self.set_title("Navigador" + title)
    def change_url(self, widget, frame):
        uri = frame.get_uri()
        self.address_bar.set_text(uri)



Browser()
gtk.main()
