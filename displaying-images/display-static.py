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

#New Code

    #Creates an Image object that displays an image
    ic = elementary.Image(window)

    #Use the os module to get the current path to our .py file. Our image is relative to our .py We do this because it is best to use the absolute file path to images for the best results.
    location = os.path.dirname(os.path.abspath(__file__))

    #Tell our icon to auto-fill open space
    ic.size_hint_weight_set(evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND)
    ic.size_hint_align_set(evas.EVAS_HINT_FILL, evas.EVAS_HINT_FILL)

    #Here we set the image we want our icon to display
    ic.file_set("%s/images/logo.png"%location)

    #Optional, lets add mouse over text to our image
    ic.tooltip_text_set("Look a pretty picture!")

    #Lets show our icon
    ic.show()

    box.pack_end(windytax)
    #Pack our icon between our text and button
    box.pack_end(ic)
    box.pack_end(button)

#End New Code

    window.resize_object_add(box)

    window.resize(300,300)

    window.show()

def button_pressed(button, arg1, arg2):
    print arg1, arg2

    elementary.exit()

if __name__ == "__main__":
    hello_elementary()

    elementary.run()

    elementary.shutdown()
