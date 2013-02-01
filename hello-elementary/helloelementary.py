#Import module the Elementary library so we can use it.
import elementary

#Import module for the canvas library Evas, when using Elementary you'll require only a few pre-defined variables from here which are shown later.
import evas

#A function that creates and shows an elementary window
def hello_elementary():
    #Creates a "Standard" elementary window. The first argument is the name of our window. The second argument is the title displayed on the window bar
    window = elementary.StandardWindow("hello world", "Hello Elementary")

    #callback_delete_request_add tells our window what to do when it's "close" button is pressed
    window.callback_delete_request_add(lambda o: elementary.exit())

    #Content for our window. Creates a "Label" object which display text in our window. Whenever we create an elementary widget object we must provide a parent canvas object (in this example and in most cases the window) as input.
    windytax = elementary.Label(window)

    #Widget size hints can be set to tell evas how they should be sized/positioned. Usually the hint functions take two parameters: for horizontal and vertical axis.
    #size_hint_weight tells Evas how much space our widget wants when space is being allocated
    windytax.size_hint_weight_set(evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND)
    #size_hint_align tells Evas how the object should be aligned, with 0.0 being left/top, 0.5 center and 1.0 right/bottom. There is also a special value EVAS_HINT_FILL which makes the widget fill it's entire allocated space.
    windytax.size_hint_align_set(evas.EVAS_HINT_FILL, evas.EVAS_HINT_FILL)

    #Define what text our window should display
    windytax.text = '<b>Hello Elementary!</b>'

    #If we want to see our object we need to tell it to be shown
    windytax.show()

    #resize_object_add makes our label object change size based on the size of our window
    window.resize_object_add(windytax)

    #resize takes an ordered pair as input for the size for our window, the dimenions are pixel by pixel
    window.resize(300,300)

    #Finally lets tell our window object to show up just like we did with our label
    window.show()

#Runs when our script is run
if __name__ == "__main__":
    #Runs our function which creates our window
    hello_elementary()

    #Starts an elementary event loop which displays all elementary objects we've created. Our code stays at this point until elementary.exit() is called
    elementary.run()

    #Once elementary is done running lets shut everything off to finish the application
    elementary.shutdown()
