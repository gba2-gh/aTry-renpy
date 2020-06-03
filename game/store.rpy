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

    timer 1 repeat True action  SetVariable( "clients_girl", If(client_enter_shop(enter_shop_prob_girl[1]),  clients_girl +1, clients_girl))
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
    python:
        rand = random.randint(1,101)
        items_to_buy =[]
        if rand < 100:#comprar
            for item_i in shopper.fav_items:
                for item_j in inventory_on_sale:
                    if item_i == item_j[0]:
                        items_to_buy.append(item_j[0])

            if len(items_to_buy) > 0:
                item_to_buy=random.choice(items_to_buy)
                flag = "found"
            else:
                flag= "not found"
                #TODO pedir()

    textbutton "[item_to_buy.fname]" xpos 500 ypos 500  action Hide("shop_request")
