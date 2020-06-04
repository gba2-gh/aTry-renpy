#renpy
#store mechanics and IA
init -2 python:

    import random

define current_turn = 0
define trust_weight = 1
define store_reputation = 0.1
define store_reputation_weight = 1
define objectsFav_prob = 0.5
define objectsFav_prob_weight = 1
define prob_turn_weight = 1
define clients_girl = 0
define clients_boy = 0
define clients_lad = 0
define clients_gal = 0
define requests = 0
define shopper_states = []
define item_picked = 0




label store_open:

python:
    enter_shop_prob_girl=[]
    for i in range(11):
        enter_shop_prob_girl.append(enter_shop_prob_func(girl_shopper))


#$enter_shop_prob_girl =  enter_shop_prob_func(girl_shopper)

call screen store_open


screen store_open:


    text "Prob: [enter_shop_prob_girl]%"
    timer 1 repeat True action  SetVariable( "time_elapsed", time_elapsed +1)

    timer 1 repeat True action  SetVariable( "clients_girl", If(client_enter_shop(enter_shop_prob_girl[1] ),  clients_girl +1, clients_girl))
    timer 1.1 repeat True action If(request_petition(clients_girl * 3),  [AddToSet(shopper_states, get_shopper_state(girl_shopper)) ,SetVariable("requests",  requests +1)] , NullAction() )
    # timer 1 repeat True action  SetVariable( "clients_boy", If(client_enter_shop(enter_shop_prob_girl[2]),  clients_boy +1, clients_boy))
    # timer 1.2 repeat True action  SetVariable( "requests", If(request_petition(clients_boy * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_lad", If(client_enter_shop(enter_shop_prob_girl[3]),  clients_lad +1, clients_lad))
    # timer 1.3 repeat True action  SetVariable( "requests", If(request_petition(clients_lad * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_gal", If(client_enter_shop(enter_shop_prob_girl[5]),  clients_gal +1, clients_gal))
    # timer 1.4 repeat True action  SetVariable( "requests", If(request_petition(clients_gal * 3),  requests +1, requests))

    use shop_request(shopper_states)
    text "Clients: [clients_girl]" ypos 100 xpos
    text "Clients: [clients_boy]" ypos 100 xpos 300
    text "Clients: [clients_lad]" ypos 100 xpos 600
    text "Clients: [clients_gal]" ypos 100 xpos 900
    text "Requests: [requests]" ypos 200
    text "Timer: [time_elapsed]" xpos 1700
    text "states: [shopper_states]" ypos 900
    text "states: [inventory_m1]" ypos 1000



screen shop_request(shopper_states):
    $xcord = 500
    $ycord =800
    for state in shopper_states:
        if state[0] == 1:#comprar
            #$remove_inventory_id(state[2][1], state[2][0], 1)
            $item_name = state[2][0].fname
            $shelf= state[2][1]
            if shelf == 1:
                textbutton "[item_name]: [shelf] : buy" xpos 500 ypos 500  action RemoveFromSet(shopper_states, shopper_states[shopper_states.index(state)])
            if shelf == 2:
                textbutton "[item_name]: [shelf] : buy" xpos 800 ypos 500  action RemoveFromSet(shopper_states, shopper_states[shopper_states.index(state)])
        if state[0] == 2:#Pedir
            textbutton "[state[1].name]: pedir" xpos xcord ypos ycord  action RemoveFromSet(shopper_states, shopper_states[shopper_states.index(state)])
        elif state[0] == 3:#Vender
            textbutton "[state[1].name]:vender " xpos xcord ypos ycord action RemoveFromSet(shopper_states, shopper_states[shopper_states.index(state)])
        elif state[0] == 4:#Hacer encargo
            textbutton "[state[1].name]:encargo " xpos xcord ypos ycord  action RemoveFromSet(shopper_states, shopper_states[shopper_states.index(state)])
        $xcord +=50

#screen store_buy():
