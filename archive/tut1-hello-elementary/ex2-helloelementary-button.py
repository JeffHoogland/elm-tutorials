import elementary, evas

def hello_elementary():
    window = elementary.StandardWindow("hello world", "Hello Elementary")

    window.callback_delete_request_add(lambda o: elementary.exit())

    windytax = elementary.Label(window)

    windytax.text = '<b>Hello Elementary!</b>'

    windytax.show()

    #Create an elementary button object
    button = elementary.Button(window)

    #Set some text for our button
    button.text = "Goodbye Elementary"

    #callback_pressed_add tells our button a callback to run when our button is pressed, the first argument is the function run and the following arguments are things to pass to the callback
    button.callback_pressed_add(button_pressed, "argument1", "argument2")

    #Show our button
    button.show()

    #Since we now have multiple objects we want to display on our window, we can position these objects using an elementary box which is a container object that you can "pack" items into.

    #Create a box
    box = elementary.Box(window)

    #Tell our box to fill all open space in our window
    box.size_hint_weight_set(evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND)
    box.size_hint_align_set(evas.EVAS_HINT_FILL, evas.EVAS_HINT_FILL)

    #Show our box
    box.show()

    #Lets pack our label and then button into our box!
    box.pack_end(windytax)
    box.pack_end(button)

    #This time lets use our box instead of just our label
    window.resize_object_add(box)

    window.resize(300,300)

    window.show()

#Our callback when the button is pressed. The first argument for this function will be the elementary button object. The rest of the arguments are the custom things we passed above
def button_pressed(button, arg1, arg2):
    #Show the content of our arguments in terminal
    print arg1, arg2

    #Lets have our button close the application, so run:
    elementary.exit()

if __name__ == "__main__":
    hello_elementary()

    elementary.run()

    elementary.shutdown()
