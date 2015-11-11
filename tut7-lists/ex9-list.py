import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.list import List

from elmextensions import StandardPopup

from listitems import ListItems

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex9", "List", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())
        
        self.lastSelected = None
        
        ourList = List(self)
        ourList.size_hint_weight = EXPAND_BOTH
        ourList.callback_item_focused_add(self.listItemSelected)
        
        ListItems.sort()
        
        for it in ListItems:
            ourList.item_append(it)
        
        ourList.go()
        ourList.show()
        
        self.resize_object_add(ourList)
    
    def listItemSelected(self, ourList, ourItem):
        if self.lastSelected != ourItem.text:
            self.lastSelected = ourItem.text
            ourPopup = StandardPopup(self, "You selected %s"%ourItem.text, "ok")
            ourPopup.show()

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()

