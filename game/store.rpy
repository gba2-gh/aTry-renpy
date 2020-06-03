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
