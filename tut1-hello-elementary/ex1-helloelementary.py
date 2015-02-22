import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.label import Label

from efl.evas import EVAS_HINT_EXPAND
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex1", "Hello Elementary", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        ourLabel = Label(self)
        ourLabel.size_hint_weight = EXPAND_BOTH
        ourLabel.text = "Hello Elementary!"
        ourLabel.show()
        
        self.resize_object_add(ourLabel)

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()
