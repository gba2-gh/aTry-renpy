#renpy
#store mechanics and IA
init -2 python:

    import random

define current_turn = 0
define store_reputation = 0.1
define objectsFav_prob = 0.5

define requests = 0
define shopper_states = []
define enter_shop_prob=[]
define clients =[]
define time_elapsed =0



label store_open:
    python:
        #reset variables
        del clients[:]
        del enter_shop_prob[:]
        del shopper_states[:]
        requests = 0
        time_elapsed = 0
        #Crear lista con la probabilidad de que cada tipo de comprador entre a la tienda
        ##for shopper in all_shoppers: ##BUG STORE.SHOPPER
        enter_shop_prob.append(enter_shop_prob_func(girl_shopper))
        clients.append(0)
    #"brake"

label clients_requests:
    python:
        for i in range(len(enter_shop_prob)):
            if client_enter_shop(enter_shop_prob[i] ):
                clients[i] +=1

        for i in range(len(clients)):
            if request_petition(clients[i] * 3):
                shopper_states.append(get_shopper_state(all_shoppers[i]))
                requests +=1
        time_elapsed +=1

    call screen store_open_screen


screen store_open_screen():

    timer 1 repeat True action Call("clients_requests")

    use shop_request(shopper_states)

    text "Prob: [enter_shop_prob]%"
    text "Clients: [clients]" ypos 100 xpos
    text "Requests: [requests]" ypos 200
    text "Timer: [time_elapsed]" xpos 1700
    text "shoppers: [lenn] " ypos 800
    text "states: [shopper_states]" ypos 900
    text "inv_m1: [inventory_m1]" ypos 1000
    textbutton "Close" xpos 1700 ypos 300 action [Jump("start")]

screen shop_request(shopper_states):
    $xcord = 500
    $ycord =800
    for state in shopper_states:
        if state[0] == 1:#comprar
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
