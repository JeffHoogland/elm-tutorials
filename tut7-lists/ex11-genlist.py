import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.genlist import Genlist, GenlistItem, GenlistItemClass

from elmextensions import StandardPopup

from listitems import ListItems

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class GLIC(GenlistItemClass):
    def __init__(self):
        GenlistItemClass.__init__(self, item_style="default")
        
    def text_get(self, gl, part, data):
        return data["itemName"]

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex11", "Genlist List", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())
        
        ourList = Genlist(self)
        ourList.size_hint_weight = EXPAND_BOTH
        ourList.callback_activated_add(self.listItemSelected)
        
        ListItems.sort()
        
        for it in ListItems:
            li = GenlistItem(item_data={"itemName":it}, item_class=GLIC())
            li.append_to(ourList)
        
        ourList.show()
        
        self.resize_object_add(ourList)
    
    def listItemSelected(self, ourList, ourItem):
        ourPopup = StandardPopup(self, "You selected %s"%ourItem.data["itemName"], "ok")
        ourPopup.show()

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()

