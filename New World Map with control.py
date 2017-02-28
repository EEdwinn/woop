class House():
    def __init__(self,the_name,N,S,E,W,U,D,O,T,the_description):
        self.name=the_name
        self.description=the_description
        self.north=N
        self.south=S
        self.east=E
        self.west=W
        self.up=U
        self.down=D
        self.open=O
        self.teleport=T
        
    def move(self,direction):
        global node
        node=globals()[getattr(self,direction)]
        
house=House('House','front_door',None,None,None,None,\
None,None,None,"There is a brown  house.")

front_door=House('Front of Door',None,'House',None,None,None,\
None,None,'in_house',"You are in front of a door.")

in_house=House('In House','living_room','front_door',None,None,\
None,None,None,None,"You are now in the house.There is a hallway at the left.")

living_room=House('Living Room',None,None,None,'bath_room',None,None,\
None,None,'You are in the living room.This is where you wish your family spend time with you')

bath_room=House('Bathroom',None,None,'living_room','your_room',None,None,None,None,\
'It smells bad in here')

your_room=House('Your Room',None,None,'bath_room',None,None,None,'secret_door',None,\
'It is were you make magic things happen.Their is a door.')

secret_door=House('Secret Door',None,None,None,None,None,'stairs',None,None,\
'You are in front of the secret door.Open it and see where you go.')

stairs=House('Stairs',None,'secret_door',None,'secret_lab',None,None,None,None,\
'You are in a dark hallway it looks like their is light at the bottom')

secret_lab=House('Secret Lab',None,None,None,'teleporter',None,None,None,None,\
'There is maps in the wall,blue prints and weird liquids.Their is what appears to look like a teleporter.')

teleporter=House('Teleporter',None,None,None,None,None,None,'military_base',None,\
'You are now in the teleporter,teleport to go to a different place.Remember in order to comeback you will have to find the teleporter in your new location to get back')

military_base=House('Military Base','shooting_range',None,None,None,None,None,None,None,\
'You teleported to a militarty base in Afghanistan.Looks like you are in in the middle of desert.d')

shooting_range=House('Shooting Range',"You Die",'military_base','weapon_room',None,None,None,None,None,\
'You are in front of the shooting range ,their are soldiers practicing their shot')

weapon_room=House('Weapon Room','bath_room2',None,None,'shooting_range',None,None,\
None,None,'You are in the weapon room.There are guns,lethals any gun you can think of.')

bath_room2=House('Portable Restroom',None,'weapon_room',None,'cabin',None,None,None,\
None,'You are in the restroom.There is a toilet ')

cabin=House('Cabin','in_cabin',None,'bath_room2',None,None,None,\
None,None,'You are now in the cabin.It is a two story cabin it looks like it is  a house.')

in_cabin=House('In Cabin',None,'cabin','stairs2',None,None,None,None,\
None,'You are in the cabin their is now much downstairs.At the corner there is a stairs')

stairs2=House('Stairs',None,None,None,None,None,None,None,None,\
'You are by the stairs go up to go to the second floor.')





import sys

node=House
is_alive = True
directions=['north','south','east','west','up','down','open','teleport']
short_directions=['n','s','e','w','u','d','o','t']
#Controller
while is_alive:
    
    #Print room name and decription
    print node.name
    print node.description
    command=raw_input('>')
    if command in ['quit','q','exit']:
        sys.exit(0)
        
    #Allows us to change node
    if command in short_directions:
        command=directions[short_directions.index(command)]
    try:
        
        node.move(command)
    except:
        print "You can't"
        