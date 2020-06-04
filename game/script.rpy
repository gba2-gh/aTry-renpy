#this code is trying to be a love letter to renpy, i have noticed that most gamesmade with the engine are shit. The reason is obvious
#Renpy is easy, very easy so every kind of beginner can use, with no programming background at all. Now this is not a bad, quite the contrary
#actually, the porpuse of an engine is to create and with renpy pretty much everyones can create.
#Of course, this is a double-edged sword, with a lot of beginners creating content most of the game sthat come out of it are, to be blunt,
#really bad

init:
    $storage_list =[] #player inventory
    $inventory_m1 =[1] #mesa1, primer elemento identifica la lista
    $inventory_m2 =[2]
    
    $storage_list=[0, [apple,9], [egg, 1], [egg, 1], [egg, 1]]
    $add_inventory(storage_list, fish, 3)
    $add_inventory(inventory_m1, apple, 50)

define e = Character("Eileen")
define time_elapsed=0

label start:
    call screen inicial

    return

screen inicial():
    add "images/main_scene.png"
    textbutton "Storage" action [Show("inventory_main"),Show("display_storage")]
    textbutton "mesa 1" xpos 200 action [Show("inventory_m1")]
    textbutton "mesa 2" xpos 350 action [Show("inventory_m2")]
    textbutton "Open Store!" xpos 550 action [Jump("store_open"), Notify("The store is open")]
    textbutton "Remove from main inv" ypos 200 action Function(remove_inventory, storage_list, apple, 1)
