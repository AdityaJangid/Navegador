import gtk
class btn(gtk.Window):
    def __init__(self, *args, **kwargs):
        super(btn, self).__init__(*args, **kwargs)
        self.set_default_size(233,300)
        self.btnn = gtk.Button("print('hello world') ")
        

        self.btnn.connect("button_press_event", self.hello)
    
    def hello(self,widget, event):
        print("testing button")

    
        self.add(self.btnn)
        self.show_all()
        self.connect('destroy', lambda w: gtk.main_quit())
btn()
gtk.main()
