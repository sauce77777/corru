###Final Project
###version 0.01
###Corrugator troubleshooter, includes a section for quality and one for mechnical

from tkinter import *


def quality():
    root=Tk()
    root.title("Wet end quality")
    root.geometry("400x400")

    Label(root,text="What quality issues are we having?").pack()
    Button(root, text="Warp", command=warp).pack()
    Button(root, text="Blowout", command=blowout).pack()
    Button(root, text="Edge Damage", command=notch).pack()
    Button(root, text="Delamination", command=blowout).pack()
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()



###modules for various symptoms for quality issues

def blowout(): ###blowout is where there is air in between top and medium liner
    root=Tk()
    root.title("Blowout solutions")
    root.geometry("400x400")

    Label(root,text="Blowing out is usually caused by less than ideal alignment at single facer").pack()
    Label(root,text=" ").pack()
    Label(root,text="1. Ensure web is not lined up on the groove of corrugating roll").pack()
    Label(root,text="2. Ensure glue dam is lined up properly").pack()
    Label(root,text="3. Ensure there is no starch buildup").pack()
    Label(root,text="4. Decrease line speed").pack()
    Label(root,text=" ").pack()
    Label(root,text="If none of these work, cry for help to supervisor").pack()
    Button(root, text="Exit", command=root.destroy).pack()


    
def notch(): ###edge damage is where there are notches on the wide of the web
    root=Tk()
    root.title("Edge damage solutions")
    root.geometry("400x400")
    
    Label(root,text="Edge damage can be caused by a variety of things ranging from raw stock or single facer lineup").pack()
    Label(root,text=" ").pack()
    Label(root,text="1. Ensure there is enough steam applied to the medium at the single facer").pack()
    Label(root,text="2. Ensure the liners are not damaged").pack()
    Label(root,text="3. Ensure the glue dam is not out too far").pack()
    Label(root,text="4. Pour hydraulic fluid onto notched side at single facer").pack()
    Label(root,text="5. Decrease line speed").pack()
    Label(root,text=" ").pack()
    Label(root,text="If none of these work, cry for help to supervisor").pack()
    Button(root, text="Exit", command=root.destroy).pack()



def bonding():      ###delamination is where there the liner do not bond properly to one another
    root=Tk()
    root.title("Delamination solutions")
    root.geometry("400x400")

    Label(root,text="Delamination issues usually stem from starch or temperature problems").pack()
    Label(root,text=" ").pack()
    Label(root,text="1. Ensure glue dam is lined up properly").pack()
    Label(root,text="2. Ensure interface pad is down at doublebacker").pack()
    Label(root,text="3. Ensure clamp is down at hot plate").pack()
    Label(root,text="4. Check if corrugating roll temerature is too low (below 280F)").pack()
    Label(root,text="if so, check if boiler is down").pack()
    Label(root,text="5. Ensure starch viscotty is within tolerance (33-43 seconds).").pack()
    Label(root,text="if too low, increase primary starch).").pack()
    Label(root,text="6. Decrease line speed").pack()
    Label(root,text=" ").pack()
    Label(root,text="If none of these work, cry for help to supervisor").pack()
    Button(root, text="Exit", command=root.destroy).pack()
    


######warp tend to be the most common problem with many variants that requires different solutions; it will have additional steps later on
def warp():
    root=Tk()
    root.title("Warp solutions")
    root.geometry("400x400")
    
    Label(root, text="What kind of warp are we having?").pack()
    Button(root, text="side to side", command=side).pack()
    Button(root, text="end to end", command=end).pack()
    Button(root, text="Exit", command=root.destroy).pack()

def end():      ###end to end warp is where boards warp from one end to another
    root=Tk()
    root.title("Warp solutions")
    root.geometry("400x400")
    
    Label(root,text="End-to-end up or end-to-end down?").pack()
    Button(root, text="end-to-end up", command=eup).pack()
    Button(root, text="end-to-end down", command=edown).pack()
    Button(root, text="Exit", command=root.destroy).pack()

def eup():            ###eup stands for end to end up           
    root=Tk()
    root.title("end-to-end up solutions")
    root.geometry("400x400")

    Label(root, text="End-to-end warp is usually caused by improper brake tensions").pack()
    Label(root, text="    ").pack()
    Label(root, text="1. Check if EOL tension is too high (above 200lbs); if so:").pack()
    Label(root, text="Decrease EOL tension to no lower than 100lbs    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="2. Check if bottom liner brake tension is too low (below 125lbs); if so").pack()
    Label(root, text="Increase bottom liner brake tension up to 200lbs    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()

def edown():            ###edown stands for end to end down              
    root=Tk()
    root.title("end-to-end down solutions")
    root.geometry("400x400")

    Label(root, text="End-to-end warp is usually caused by improper brake tensions").pack()
    Label(root, text="    ").pack()
    Label(root, text="1. Check if EOL tension is too low (below 100lbs); if so:").pack()
    Label(root, text="Increase EOL tension up to than 200lbs    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="2. Check if bottom liner brake tension is too high (below 200lbs); if so").pack()
    Label(root, text="Decrease bottom liner brake tension down to 125lbs    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()

def side():         ###side to side warp is where boards warp from one side to another   
    root=Tk()
    root.title("Warp solutions")
    root.geometry("400x400")
    
    Label(root,text="Side-to-side up or side-to-side down?").pack()
    Button(root, text="side-to side-up", command=sup).pack()
    Button(root, text="side-to side-down", command=sdown).pack()
    Button(root, text="Exit", command=root.destroy).pack()


def sup():          ###sup is side to side up
    root=Tk()
    root.title("Side-to-side up solutions")
    root.geometry("400x400")

    Label(root, text="Up warp is usually result of excessive moisture in web:").pack()
    Label(root, text="    ").pack()
    Label(root, text="1. Check if top liner brake tension is too low (below 120lbs); if so:").pack()
    Label(root, text="increase up to 200lbs:").pack()
    Label(root, text="    ").pack()
    Label(root, text="2. Check if top liner temperature is low (below 160F); if so:").pack()
    Label(root, text="add wrap at top preheater").pack()
    Label(root, text="max out single facer wrap arm").pack()
    Label(root, text="    ").pack()
    Label(root, text="3. Check if web temperature s too low (below 175F); if so:").pack()
    Label(root, text="increase web preheater at triplestack").pack()
    Label(root, text="    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="if none of the above work, try these:").pack()
    Label(root, text="4. Reduce glue roll gap at single facer").pack()
    Label(root, text="5. Decrease bottom brake tension").pack()
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()

def sdown():             ###sdown is side to side down
    root=Tk()
    root.title("Side-to-side down warp solutions")
    root.geometry("400x400")

    Label(root, text="Up warp is usually result of lack of moisture in web").pack()
    Label(root, text="    ").pack()
    Label(root, text="1. Check if top liner brake tension is too high (above 200lbs); if so:").pack()
    Label(root, text="decrease down to 125lbs:").pack()
    Label(root, text="    ").pack()
    Label(root, text="2. Check if top liner temperature is high (above 190F); if so:").pack()
    Label(root, text="unwrap top preheater").pack()
    Label(root, text="unwrap single facer wrap arm").pack()
    Label(root, text="    ").pack()
    Label(root, text="3. Check if web temperature s too high (below 200F); if so:").pack()
    Label(root, text="unwrap web preheater at triplestack").pack()
    Label(root, text="    ").pack()
    Label(root, text="4.Check if bottom liner temperature is too low (below 160F), if so:").pack()
    Label(root, text="add wrap to bottom liner preheater at triplestack    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="    ").pack()
    Label(root, text="If none of the above work, try these   ").pack()
    Label(root, text="5. Increase glue roll gap at single facer").pack()
    Label(root, text="6. Increase bottom brake tension").pack()
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()

###some simple mechanical issues... moral of the story, call maintenance, they get paid more
def mechanical():
    root=Tk()
    root.title("Mechanical issues")
    root.geometry("400x400")

    Label(root,text="What mechanical issues are we having?").pack()
    Button(root, text="Stuck trolley", command=trolley).pack()
    Button(root, text="Irresponsive control panel", command=panel).pack()
    Button(root, text="Random E-stops", command=estop).pack()
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()

def trolley():      ##trolleys that moves rolls in and out of the machines tend to get stuck
    root=Tk()
    root.title("Trolley issues")
    root.geometry("400x400")
    
    Label(root,text="Our trolleys are junk, check in this order").pack()
    Label(root,text=" ").pack()
    Label(root,text="1. Trolley chain fell off its track an is stuck on edge; in this scenario; use a pry bar to unstuck it.").pack()
    Label(root,text="2. There is too much debris in the tracks and physically restricting its movement; clean out debris").pack()
    Label(root,text="3. The roll might be too heavy; see if it'll move without roll on it, or push with forklift").pack()
    Label(root,text="4. The chain is broken; call maintenance and go to break").pack()
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()

def panel():            ###the control panel that controls roll stands tend to become non responsive
    root=Tk()
    root.title("Control panel issues")
    root.geometry("400x400")
    
    Label(root,text="Control panels issues are usually electrical, check things in this order").pack()
    Label(root,text=" ").pack()
    Label(root,text="1. Is another key in on-position on the control panel? These control panels are ran on the same hydraulic lines; only one button can move at once.").pack()
    Label(root,text="2. Did the control panel kick out?").pack()
    Label(root,text="3. Is there a hydraulic leak?").pack()
    Label(root,text="4. Else, call maintenance").pack()
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()

def estop():            ###the machines itself tend to go through phases of emergency stopping randomly when it shouldn't do so
    root=Tk()
    root.title("Random E-stops")
    root.geometry("400x400")
    
    Label(root,text="E-stop issues can be tricky to diagnose, check things in this order").pack()
    Label(root,text=" ").pack()
    Label(root,text="1. Would it restart? if so, it's electrical").pack()
    Label(root,text="2. Is there a hydraulic leak?").pack()
    Label(root,text="3. Is the glue roll turning?").pack()
    Label(root,text="4. Call maintenance").pack()
    Label(root,text=" ").pack()
    Label(root,text="Side note: Is someone hitting e-stop on purpose? (y/n)").pack()
    
    Label(root, text="    ").pack()
    Button(root, text="Exit", command=root.destroy).pack()


root=Tk()
root.title("Corrugator Wet End Troubleshooter")
root.geometry("400x400")

Label(root,text="What problems are we having?").pack()
Button(root, text="Board Quality", command=quality).pack()
Button(root, text="Mechanical", command=mechanical).pack()

Label(root, text="    ").pack()
Button(root, text="Exit", command=root.destroy).pack()

###Sauce 11 Dec 2021
