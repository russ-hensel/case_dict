# -*- coding: utf-8 -*-

"""
This file shows three implementations using a dictionary to help manage
the calling of buttons.  In this case I am using just one row of a
grid for 4 buttons.

A little trick with a lambda allows us to sent the button instance to
a single function that is the callback for all the buttons.

The button is then looked up in a dict which contains the "real"
function we wish to call.

The implementation grow a bit more abstract first repeating a lot of code,
then using global variables, and finally using a class along with the
global case_dict

For a real interface there would be a bit more code, and more flexible code,
but the point of this is to show how the case_dict can be used.

examples are:
    ex_buttons_with_attributes_in_grid()
    ex_buttons_with_attributes_in_grid_2()
    ex_buttons_with_builder_class()

    with a bunch of helper functions used by some of the examples
"""

import  tkinter as Tk
import  sys



case_dict   = {}     # provides for switch statement or case statement
                     # substitute key is a button, value is a function to be called
                     # used by callback_with_button


# --------------
def callback_function(  ):
        print( "callback_function" )

# --------------
def cb_1( a_button ):
    """
    a callback function for button 1, just
    prints cb_1 to show it has be called.
    make it anything you want for your application
    """
    print( "cb_1" )

# --------------
def cb_2( a_button ):
    """
    like cb_1 but for button 2
    """
    print( "cb_2" )

def cb_3( a_button ):
    """
    like cb_1 but for button n
    """
    print( "cb_3" )

# --------------
def cb_4( a_button ):
    """
    like cb_1 but for button n
    """
    print( "cb_4" )

# --------------
def cb_5( a_button ):
    """
    like cb_1 but for button n
    """
    print( "cb_5" )

# --------------
def callback_with_button( a_button ):
    """
    this will be our universal callback function
    actually just a 'way station' as it uses case_dict to call another function
    the "real" callback function
    a_button passed on just to show we can
    a_button could also be a subclass of button which might contain more information.
    """
    case_dict[ a_button ]( a_button )
    """
    above equivalent to
    real_cb_function  =  case_dict[ a_button ]
    real_cb_function( a_button )
    """

# ----------------------------------------
def set_callback( a_button, a_function ):
    """
    a_function to set the callback in case_dict for a_button
    a bit indirect as this seems to 'hide' the parm a_button
    perhaps a closure?

    """
    global case_dict

    a_button.config( command = lambda: callback_with_button( a_button ) )
    case_dict[a_button] = a_function

# ----------------------------------------
def ex_buttons_with_attributes_in_grid():
    print("""
    ================ ex_buttons_with_attributes_in_grid() look at appearance attributes
    """)
    global case_dict

    root = Tk.Tk()
    root.title( "ex_buttons_with_attributes_in_grid()" )
    parent_frame   = root   # in this case
 
    ix_row   = 0
    ix_col   = -1

    # --------------
    ix_col          += 1
    txt              = "Button 1"    # text for button label 
    cb_for_button    = cb_1

    a_button = Tk.Button( parent_frame , width=10, height=2, text = txt )
    a_button.grid( row = ix_row, column = ix_col   )
    a_button.config( text  = txt  )
    a_button.config( state = Tk.NORMAL )

    set_callback( a_button, cb_for_button )

    # --------------
    ix_col          += 1
    txt              = "Button 2"
    cb_for_button    = cb_2

    a_button = Tk.Button( parent_frame , width=10, height=2, text = txt )
    a_button.grid( row = ix_row, column = ix_col   )
    a_button.config( text  = txt  )
    a_button.config( state = Tk.NORMAL )

    set_callback( a_button, cb_for_button )

   # --------------
    ix_col          += 1
    txt              = "Button 3"
    cb_for_button    = cb_3

    a_button = Tk.Button( parent_frame , width=10, height=2, text = txt )
    a_button.grid( row = ix_row, column = ix_col   )
    a_button.config( text  = txt  )
    a_button.config( state = Tk.NORMAL )

    set_callback( a_button, cb_for_button )

    # --------------
    ix_col          += 1
    txt              = "Button 4"
    cb_for_button    = cb_4

    a_button = Tk.Button( parent_frame , width=10, height=2, text = txt )
    a_button.grid( row = ix_row, column = ix_col   )
    a_button.config( text  = txt  )
    a_button.config( state = Tk.NORMAL )

    set_callback( a_button, cb_for_button )

    root.mainloop()

ex_buttons_with_attributes_in_grid()

# ----------------------------------------
def button_maker( a_frame, cb_for_button, ix_row, ix_col, cb_function ):
    """
    make and configure a button using provided parameters
    """
    a_button = Tk.Button( a_frame , width=10, height=2, text = cb_for_button )
    a_button.grid( row = ix_row, column = ix_col   )
    a_button.config( state = Tk.NORMAL )

    set_callback( a_button, cb_function )

# ----------------------------------------
def ex_buttons_with_attributes_in_grid_2():
    print("""
    ================ ex_buttons_with_attributes_in_grid_2()  using a helper function
    """)
    global case_dict

    root = Tk.Tk()
    root.title( "ex_buttons_with_attributes_in_grid_2()" )
    parent_frame   = root   # parent frame is frame where buttons are placed

    ix_row   = 0       # row in grid
    ix_col   = -1      # column in grid

    # --------------
    ix_col          += 1
    txt              = "Button 1"
    cb_for_button    = cb_1
    button_maker( parent_frame, txt, ix_row, ix_col, cb_for_button )

    # --------------
    ix_col          += 1
    txt              = "Button 2"
    cb_for_button    = cb_2
    button_maker( parent_frame, txt, ix_row, ix_col, cb_for_button )

   # --------------
    ix_col          += 1
    txt              = "Button 3"
    cb_for_button    = cb_3
    button_maker( parent_frame, txt, ix_row, ix_col, cb_for_button )

    # --------------
    ix_col          += 1
    txt              = "Button 4"
    cb_for_button    = cb_4
    button_maker( parent_frame, txt, ix_row, ix_col, cb_for_button )

    root.mainloop()

#ex_buttons_with_attributes_in_grid_2()

# -----------------------------------
class ButtonBuilder( ):
    """
    a class for building buttons with a dict for the case statement
    calling them
    also lays out the buttons in a grid advancing a column at a time
    """
    # --------------
    def __init__( self, parent_frame, case_dict  ):
        self.parent_frame = parent_frame
        self.case_dict    = case_dict
        self.reset()

    # --------------
    def reset( self ):
        """
        so far just the grid placement instance variables... later ?
        """
        self.ix_row  = 0
        self.ix_col  = 0
        """
        change these from outside the class instance to skip around in grid
        else you will just increment as in make_button()
        """
    # --------------
    def make_button( self, button_text, cb_function ):
        """
        make a button using parameters and instance variables
        we could make width.... instance variable and let user set but lets
        keep simple for now
        """
        a_button                = Tk.Button( self.parent_frame , width=10, height=2, text = button_text )
        a_button.grid( row        = self.ix_row, column = self.ix_col   )
        a_button.config( state   = Tk.NORMAL )
        a_button.config( command = lambda: callback_with_button( a_button ) )
        self.case_dict[a_button] = cb_function

        #self.ix_row  += 1   just incrementing by column now
        self.ix_col  += 1
        return a_button

# ----------------------------------------
def ex_buttons_with_builder_class():
    print("""
    ================ ex_buttons_with_builder_class()
    use a class to assist in button building
    """)

    root         = Tk.Tk()
    root.title( "ex_buttons_with_builder_class()" )
    parent_frame   = root   # in this case

    global case_dict
    case_dict      = {}
    button_builder   = ButtonBuilder( parent_frame = parent_frame, case_dict = case_dict )

    # --------------
    txt              = "Button 1"
    cb_for_button    = cb_1
    button_builder.make_button(  button_text = txt,  cb_function = cb_for_button )

    # --------------
    txt              = "Button 2"
    cb_for_button    = cb_2
    button_builder.make_button(  button_text = txt,  cb_function = cb_for_button )

    # --------------
    txt              = "Button 3"
    cb_for_button    = cb_3
    button_builder.make_button(  button_text = txt,  cb_function = cb_for_button )

    # --------------
    txt              = "Button 4"
    cb_for_button    = cb_4
    button_builder.make_button(  button_text = txt,  cb_function = cb_for_button )

    root.mainloop()


ex_buttons_with_builder_class()


 
