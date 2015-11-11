import efl.elementary as elm
from efl.elementary.window import StandardWindow

from elmextensions import SearchableList
from elmextensions import StandardPopup

from listitems import ListItems

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex10", "Searchable List", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        searchList = SearchableList(self)
        searchList.size_hint_weight = EXPAND_BOTH
        searchList.ourList.callback_activated_add(self.listItemSelected)
        
        ListItems.sort()
        
        for it in ListItems:
            searchList.item_append(it)
        
        searchList.show()
        
        self.resize_object_add(searchList)
    
    def listItemSelected(self, ourList, ourItem):
        ourPopup = StandardPopup(self, "You selected %s"%ourItem.text, "ok")
        ourPopup.show()

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()

