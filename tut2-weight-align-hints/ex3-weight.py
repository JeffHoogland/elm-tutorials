import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.label import Label
from efl.elementary.button import Button
from efl.elementary.box import Box

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex3", "Weight Example", size=(300, 400))
        self.callback_delete_request_add(lambda o: elm.exit())
        
        ourButton = Button(self)
        ourButton.size_hint_weight = (0, 0)
        ourButton.size_hint_align = FILL_BOTH
        ourButton.text = "Button 1"
        ourButton.show()
        
        ourButton2 = Button(self)
        ourButton2.size_hint_weight = EXPAND_BOTH
        ourButton2.size_hint_align = FILL_BOTH
        ourButton2.text = "Button 2"
        ourButton2.show()
        
        ourButton3 = Button(self)
        ourButton3.size_hint_weight = (0, 0.5)
        ourButton3.size_hint_align = FILL_BOTH
        ourButton3.text = "Button 3"
        ourButton3.show()
        
        ourBox = Box(self)
        ourBox.size_hint_weight = EXPAND_BOTH
        ourBox.pack_end(ourButton)
        ourBox.pack_end(ourButton2)
        ourBox.pack_end(ourButton3)
        ourBox.show()
        
        self.resize_object_add(ourBox)

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()
