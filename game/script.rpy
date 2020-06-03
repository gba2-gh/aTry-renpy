#this code is trying to be a love letter to renpy, i have noticed that most gamesmade with the engine are shit. The reason is obvious
#Renpy is easy, very easy so every kind of beginner can use, with no programming background at all. Now this is not a bad, quite the contrary
#actually, the porpuse of an engine is to create and with renpy pretty much everyones can create.
#Of course, this is a double-edged sword, with a lot of beginners creating content most of the game sthat come out of it are, to be blunt,
#really bad


define e = Character("Eileen")
define time_elapsed=0

label start:
    $storage_list =[] #player inventory
    $inventory_m1 =[[apple, 3]] #mesa1
    $inventory_m2 =[]

    $storage_list=[[apple,9], [egg, 1], [egg, 1], [egg, 1]]
    $add_inventory(storage_list, fish, 3)

    call screen inicial

    return

screen inicial():
    add "images/main_scene.png"
    textbutton "Storage" action [Show("inventory_main"),Show("display_storage")]
    textbutton "mesa 1" xpos 200 action [Show("inventory_m1")]
    textbutton "mesa 2" xpos 350 action [Show("inventory_m2")]
    textbutton "Open Store!" xpos 550 action [Jump("store_open"), Notify("The store is open")]
    textbutton "Remove from main inv" ypos 200 action Function(remove_inventory, storage_list, apple, 1)

screen store_open:

    text "Prob: [enter_shop_prob_girl]%"
    timer 1 repeat True action  SetVariable( "time_elapsed", time_elapsed +1)

    timer 1 repeat True action  SetVariable( "clients_girl", If(client_enter_shop(enter_shop_prob_girl[1]),  clients_girl +1, clients_girl))
    timer 1.1 repeat True action  SetVariable( "requests", If(request_petition(clients_girl * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_boy", If(client_enter_shop(enter_shop_prob_girl[2]),  clients_boy +1, clients_boy))
    # timer 1.2 repeat True action  SetVariable( "requests", If(request_petition(clients_boy * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_lad", If(client_enter_shop(enter_shop_prob_girl[3]),  clients_lad +1, clients_lad))
    # timer 1.3 repeat True action  SetVariable( "requests", If(request_petition(clients_lad * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_gal", If(client_enter_shop(enter_shop_prob_girl[5]),  clients_gal +1, clients_gal))
    # timer 1.4 repeat True action  SetVariable( "requests", If(request_petition(clients_gal * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_girl", If(client_enter_shop(enter_shop_prob_girl[6]),  clients_girl +1, clients_girl))
    # timer 1 repeat True action  SetVariable( "requests", If(request_petition(clients_girl * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_girl", If(client_enter_shop(enter_shop_prob_girl[7]),  clients_girl +1, clients_girl))
    # timer 1 repeat True action  SetVariable( "requests", If(request_petition(clients_girl * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_girl", If(client_enter_shop(enter_shop_prob_girl[8]),  clients_girl +1, clients_girl))
    # timer 1 repeat True action  SetVariable( "requests", If(request_petition(clients_girl * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_girl", If(client_enter_shop(enter_shop_prob_girl[9]),  clients_girl +1, clients_girl))
    # timer 1 repeat True action  SetVariable( "requests", If(request_petition(clients_girl * 3),  requests +1, requests))

    text "Clients: [clients_girl]" ypos 100 xpos
    text "Clients: [clients_boy]" ypos 100 xpos 300
    text "Clients: [clients_lad]" ypos 100 xpos 600
    text "Clients: [clients_gal]" ypos 100 xpos 900
    text "Requests: [requests]" ypos 200
    text "Timer: [time_elapsed]" xpos 1700
