import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
                           choices = ['Vanilla','chocolate','strawberry'] )
easygui.msgbox("You pesked" + flavor)
                 