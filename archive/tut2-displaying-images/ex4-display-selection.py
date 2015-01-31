import elementary, evas, os

def hello_elementary():
    window = elementary.StandardWindow("hello world", "Hello Elementary")

    window.callback_delete_request_add(lambda o: elementary.exit())

    windytax = elementary.Label(window)

    windytax.text = '<b>Hello Elementary!</b>'

    windytax.show()

    button = elementary.Button(window)

    button.text = "Goodbye Elementary"

    button.callback_pressed_add(button_pressed, "argument1", "argument2")

    button.show()

    box = elementary.Box(window)

    box.size_hint_weight_set(evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND)
    box.size_hint_align_set(evas.EVAS_HINT_FILL, evas.EVAS_HINT_FILL)
    
    box.show()

    ic = elementary.Image(window)

    location = os.path.dirname(os.path.abspath(__file__))

    ic.size_hint_weight_set(evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND)
    ic.size_hint_align_set(evas.EVAS_HINT_FILL, evas.EVAS_HINT_FILL)

    ic.file_set("%s/images/logo.png"%location)

    ic.tooltip_text_set("Look a pretty picture!")

    ic.show()

#New Code

    #Creates a "FileselectorButton" object. This is a button (just like we have created before) except that when it is click it automatically opens a file selector window
    fsb = elementary.FileselectorButton(window)

    #We can set the text of our fsb just like a normal button text
    fsb.text = "Change Image"

    #Tooltip for mouse over
    fsb.tooltip_text_set("Click Me!")

    #This tells our file selector window what to do when our user selects a file. The first argument is the callback function we want run and our second argument is our image object we want to change the display of
    fsb.callback_file_chosen_add(change_image, ic)

    #Show our button
    fsb.show()

    box.pack_end(windytax)
    box.pack_end(ic)
    #Pack our file selector button between our image and button
    box.pack_end(fsb)
    box.pack_end(button)

    window.resize_object_add(box)

    window.resize(300,300)

    window.show()

#Our fileselector callback. The file argument is the fileselectbutton object. The second argument is the full path to the file that was selected. The final argument is the image object we passed to this callback
def change_image(fsb, file_selected, image):
    #Check to make sure a file of some sort was selected. If nothing was selected file_selected will equal None type
    if file_selected:
        #These are the extensions we will allow our program to display
        validExtensions = [".png", ".jpg", ".gif"]

        #Use the os module to easily get the extension of our file
        fileName, fileExtension = os.path.splitext(file_selected)

        #If the extension is in our validExtenions lets check the image we are displaying!
        if fileExtension in validExtensions:
            image.file_set(file_selected)

#End New Code

def button_pressed(button, arg1, arg2):
    print arg1, arg2

    elementary.exit()

if __name__ == "__main__":
    hello_elementary()

    elementary.run()

    elementary.shutdown()
