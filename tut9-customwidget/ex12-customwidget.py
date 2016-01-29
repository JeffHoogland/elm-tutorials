import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.frame import Frame
from efl.elementary.image import Image


from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class PictureFrame(Frame):
    def __init__(self, parent_widget, ourText=None, image=None, *args, **kwargs):
        Frame.__init__(self, parent_widget, *args, **kwargs)
        
        self.text = ourText
        
        self.ourImage = Image(self)
        self.ourImage.size_hint_weight = EXPAND_BOTH
        
        if image:
			self.ourImage.file_set(image)
        
        self.content_set(self.ourImage)
    
    def file_set(self, image):
        self.ourImage.file_set(image)

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex12", "Custom Widget", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())
        
        ourPictureFrame = PictureFrame(self)
        ourPictureFrame.size_hint_weight = EXPAND_BOTH
        ourPictureFrame.text = "A Custom Picture Frame"
        ourPictureFrame.file_set("images/logo.png")
        ourPictureFrame.show()
        
        self.resize_object_add(ourPictureFrame)

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()


