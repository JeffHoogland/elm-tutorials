import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.label import Label
from efl.elementary.button import Button
from efl.elementary.box import Box

from efl.evas import EVAS_HINT_EXPAND
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex2", "Hello Elementary", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        ourLabel = Label(self)
        ourLabel.size_hint_weight = EXPAND_BOTH
        ourLabel.text = "Hello Elementary!"
        ourLabel.show()
        
        ourButton = Button(self)
        ourButton.size_hint_weight = EXPAND_BOTH
        ourButton.text = "Goodbye Elementary"
        ourButton.callback_clicked_add(self.buttonPressed)
        ourButton.show()
        
        ourBox = Box(self)
        ourBox.size_hint_weight = EXPAND_BOTH
        ourBox.pack_end(ourLabel)
        ourBox.pack_end(ourButton)
        ourBox.show()
        
        self.resize_object_add(ourBox)
    
    def buttonPressed(self, btn):
        elm.exit()

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()
