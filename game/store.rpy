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
define shopper_state = 0
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

    timer 1 repeat True action  SetVariable( "clients_girl", If(client_enter_shop(100),  clients_girl +1, clients_girl))
    timer 1.1 repeat True action If(request_petition(clients_girl * 3),  [Show("shop_request", shopper=girl_shopper),SetVariable("requests",  requests +1)] , NullAction() )
    # timer 1 repeat True action  SetVariable( "clients_boy", If(client_enter_shop(enter_shop_prob_girl[2]),  clients_boy +1, clients_boy))
    # timer 1.2 repeat True action  SetVariable( "requests", If(request_petition(clients_boy * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_lad", If(client_enter_shop(enter_shop_prob_girl[3]),  clients_lad +1, clients_lad))
    # timer 1.3 repeat True action  SetVariable( "requests", If(request_petition(clients_lad * 3),  requests +1, requests))
    # timer 1 repeat True action  SetVariable( "clients_gal", If(client_enter_shop(enter_shop_prob_girl[5]),  clients_gal +1, clients_gal))
    # timer 1.4 repeat True action  SetVariable( "requests", If(request_petition(clients_gal * 3),  requests +1, requests))


    text "Clients: [clients_girl]" ypos 100 xpos
    text "Clients: [clients_boy]" ypos 100 xpos 300
    text "Clients: [clients_lad]" ypos 100 xpos 600
    text "Clients: [clients_gal]" ypos 100 xpos 900
    text "Requests: [requests]" ypos 200
    text "Timer: [time_elapsed]" xpos 1700


screen shop_request(shopper):

    $shopper_state= get_shopper_state(shopper)

    if shopper_state == 0:#comprar
        $item = item_picked[0].fname
        $mesa= item_picked[1]
        if mesa == 1:
            textbutton "[item]: [mesa] : buy" xpos 500 ypos 500  action Hide("shop_request")
        if mesa == 2:
            textbutton "[item]: [mesa] : buy" xpos 800 ypos 500  action Hide("shop_request")
    elif shopper_state == 1:#Pedir
        textbutton " pedir" xpos 500 ypos 800  action Hide("shop_request")
    elif shopper_state == 2:#Vender
        textbutton "vender " xpos 700 ypos 800  action Hide("shop_request")
    elif shopper_state == 3:#Hacer encargo
        textbutton "encargo " xpos 900 ypos 800  action Hide("shop_request")

#screen store_buy():
