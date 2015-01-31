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

    fsb = elementary.FileselectorButton(window)

    fsb.text = "Change Image"

    fsb.tooltip_text_set("Click Me!")

    fsb.callback_file_chosen_add(change_image, ic, window)

    fsb.show()

    box.pack_end(windytax)
    box.pack_end(ic)
    box.pack_end(fsb)
    box.pack_end(button)

    window.resize_object_add(box)

    window.resize(500,300)

    window.show()

#New Code
#This time we also pass the window object to our change image function. The reason for this is that our popup object needs a parent window object
def change_image(fsb, file_selected, image, window):
    if file_selected:
        validExtensions = [".png", ".jpg", ".gif"]

        fileName, fileExtension = os.path.splitext(file_selected)

        if fileExtension in validExtensions:
            image.file_set(file_selected)
        else:
            #if we have an invalid extension lets give the user a popup message telling them why the image didn't change

            #Create a popup message
            popup = elementary.Popup(window)

            #Set the title of our popup
            popup.part_text_set("title,text", "Invalid File Extension")

            #Set the text of our popup
            popup.text = "File %s has an invalid file extension of %s"%(fileName, fileExtension)

            #Create a button object
            bt = elementary.Button(window)

            #Set it's text
            bt.text = "OK"

            #Define a callback that is called when the button is clicked, lets pass our popup object to this call back so we can close the popup when the user presses OK
            bt.callback_clicked_add(bnt_close, popup)

            #Sets content for our popup. The first argument is an arbitrary name for the content piece and the second argument is the elementary object you would like displayed for the content
            popup.part_content_set("button1", bt)

            #Show the popup to our user
            popup.show()

#The callback for our popup's OK button. The first agurment is the button object itself and the second object is the popup we passed to it
def bnt_close(bt, popup):
    #Lets delete the popup so it goes away
    popup.delete()

#End New Code

def button_pressed(button, arg1, arg2):
    print arg1, arg2

    elementary.exit()

if __name__ == "__main__":
    hello_elementary()

    elementary.run()

    elementary.shutdown()
