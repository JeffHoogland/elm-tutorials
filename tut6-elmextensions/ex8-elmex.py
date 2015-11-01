import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.box import Box

from elmextensions import StandardButton
from elmextensions import StandardPopup
from elmextensions import AboutWindow

from aboutvars import *

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex8", "ElmEx - Button and Popup", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        ourButton = StandardButton(self, "Show Popup", "start-here", self.buttonPressed)
        ourButton.size_hint_weight = EXPAND_HORIZ
        ourButton.size_hint_align = FILL_BOTH
        ourButton.show()
        
        ourButton2 = StandardButton(self, "Show About", "dialog-information", self.button2Pressed)
        ourButton2.size_hint_weight = EXPAND_HORIZ
        ourButton2.size_hint_align = FILL_BOTH
        ourButton2.show()
        
        mainBox = Box(self)
        mainBox.size_hint_weight = EXPAND_BOTH
        mainBox.size_hint_align = FILL_BOTH
        mainBox.pack_end(ourButton)
        mainBox.pack_end(ourButton2)
        mainBox.show()
        
        self.resize_object_add(mainBox)
        
    def buttonPressed(self, btn):
        ourPopup = StandardPopup(self, "Press OK to close this message.", "ok")
        ourPopup.show()
    
    def button2Pressed(self, btn):
        AboutWindow(self, title="About Window", standardicon="dialog-information", \
                        version="1.0", authors=AUTHORS, \
                        licen=LICENSE, webaddress="https://github.com/JeffHoogland/python-elm-extensions", \
                        info=INFO)

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()

