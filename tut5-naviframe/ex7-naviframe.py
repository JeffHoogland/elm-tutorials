import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.image import Image
from efl.elementary.label import Label
from efl.elementary.button import Button
from efl.elementary.box import Box
from efl.elementary.naviframe import Naviframe

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex7", "Naviframe", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        staticImage = staticImage = Image(self)
        staticImage.size_hint_weight = EXPAND_BOTH
        staticImage.file_set("images/logo.png")
        staticImage.tooltip_text_set("A picture!")
        staticImage.show()
        
        ourLabel = ourLabel = Label(self)
        ourLabel.size_hint_weight = EXPAND_BOTH
        ourLabel.text = "Hey look some text!"
        ourLabel.show()
        
        self.nf = Naviframe(self, size_hint_weight=EXPAND_BOTH,
                               size_hint_align=FILL_BOTH)
        self.nf.show()
        
        buttonOne = Button(self)
        buttonOne.size_hint_weight = EXPAND_BOTH
        buttonOne.text = "Show image"
        buttonOne.callback_clicked_add(self.buttonPressed, staticImage)
        buttonOne.show()
        
        buttonTwo = Button(self)
        buttonTwo.size_hint_weight = EXPAND_BOTH
        buttonTwo.text = "Show label"
        buttonTwo.callback_clicked_add(self.buttonPressed, ourLabel)
        buttonTwo.show()
        
        buttonBox = Box(self)
        buttonBox.size_hint_weight = EXPAND_HORIZ
        buttonBox.horizontal_set(True)
        buttonBox.pack_end(buttonOne)
        buttonBox.pack_end(buttonTwo)
        buttonBox.show()
        
        mainBox = Box(self)
        mainBox.size_hint_weight = EXPAND_BOTH
        mainBox.pack_end(self.nf)
        mainBox.pack_end(buttonBox)
        mainBox.show()
        
        self.nf.item_simple_push(staticImage)
        
        self.resize_object_add(mainBox)
        
    def buttonPressed(self, btn, ourObject):
        self.nf.item_simple_push(ourObject)

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()

