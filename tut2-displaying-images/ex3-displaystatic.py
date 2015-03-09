import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.image import Image

from efl.evas import EVAS_HINT_EXPAND
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex3", "Static Image", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        ourImage = Image(self)
        ourImage.size_hint_weight = EXPAND_BOTH
        ourImage.file_set("images/logo.png")
        ourImage.tooltip_text_set("A picture!")
        ourImage.show()
        
        self.resize_object_add(ourImage)

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()
