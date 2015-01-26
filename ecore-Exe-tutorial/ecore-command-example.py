"""
A simple example on how to use ecore.Exe to interact with a command

Usage:
    python ecore-command-example-py <command>
    
Text you put in the entry box is piped to the running command when you press the send button
"""

import sys
from efl import ecore
from efl import evas
from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
from efl import elementary
from efl.elementary.window import Window, ELM_WIN_DIALOG_BASIC
from efl.elementary.box import Box
from efl.elementary.button import Button
from efl.elementary.entry import Entry

EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL
FILL_HORIZ = EVAS_HINT_FILL, 0.5
ALIGN_CENTER = 0.5, 0.5

class ourCommand(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.cmd_exe = None
        
        win = self.win = Window("ecore-ex", ELM_WIN_DIALOG_BASIC)
        win.title = "Ecore Example"
        win.size_hint_weight = evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND
        win.size_hint_align = evas.EVAS_HINT_FILL, evas.EVAS_HINT_FILL
        win.resize(300, 200)
        win.callback_delete_request_add(lambda o: elementary.exit())
        win.show()
        win.activate()
        
        self.sendEntry = Entry(win, size_hint_weight=EXPAND_BOTH, size_hint_align=FILL_BOTH)
        self.sendEntry.show()
        
        self.sendButton = Button(win, size_hint_weight=EXPAND_HORIZ,
                              size_hint_align=FILL_HORIZ)
        self.sendButton.text = "Send!"
        self.sendButton.callback_pressed_add(self.sendPressed)
        self.sendButton.show()
        
        box = Box(win, size_hint_weight=EXPAND_HORIZ,
                           size_hint_align=FILL_HORIZ)
        box.pack_end(self.sendEntry)
        box.pack_end(self.sendButton)
        box.show()
        
        win.resize_object_add(box)
        
        self.run_command(cmd)
    
    def sendPressed(self, btn):
        print "Sending Data: %s"%(self.sendEntry.text)
        if self.cmd_exe:
            ourResult = self.cmd_exe.send("%s\n"%self.sendEntry.text)
            print("Send Success: %s"%ourResult)
        self.sendEntry.text = ""
        
    def run_command(self, command):
        self.cmd_exe = cmd = ecore.Exe(
            command,
            ecore.ECORE_EXE_PIPE_READ |
            ecore.ECORE_EXE_PIPE_ERROR |
            ecore.ECORE_EXE_PIPE_WRITE
        )
        cmd.on_add_event_add(self.command_started)
        cmd.on_data_event_add(self.received_data)
        cmd.on_error_event_add(self.received_error)
        cmd.on_del_event_add(self.command_done)
        
    def command_started(self, cmd, event, *args, **kwargs):
        print("Command started.\n")

    def received_data(self, cmd, event, *args, **kwargs):
        print("Output: %s"%event.data)

    def received_error(self, cmd, event, *args, **kwargs):
        print("Error: %s" % event.data)

    def command_done(self, cmd, event, *args, **kwargs):
        print("Command done.")
        elementary.exit()


if __name__ == "__main__":
    cmd = " ".join(sys.argv[1:])

    elementary.init()

    start = ourCommand(cmd)

    elementary.run()
    elementary.shutdown()
