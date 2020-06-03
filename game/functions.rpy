#renpy
#functions

init python:

#########INVENTORY
    def add_inventory(inv, item, qty):
        if item.stack == True:
            if (isin_inventory(inv, item)):
                for i in inv:
                    if i[0].name == item.name:
                        i[1] += qty
            else:
                inv.append([item, qty])
        else:
            inv.append([item, qty])



    def remove_inventory(inv, item, qty):
        for i in inv:
            if( item in i):
                i[1] -= qty #excepcion para qty> i
                if(i[1] <=0):
                    del inv[inv.index(i)]

    def isin_inventory(inv, item):
        for i in inv:
            if item in i:
                return True
        return False

    def swap_inventory(inv_s, inv_r, item, qty):
        if (isin_inventory(inv_s, item)):
            remove_inventory(inv_s, item, qty)
            add_inventory(inv_r, item, qty)#excepcion para que quepa en inv_r

############STORE
    def client_enter_shop(enter_shop_prob):
        if (random.randint(1,101) > (100 - enter_shop_prob)):
            return True
        else:
            return False

    def request_petition(prob):
        if (random.randint(1,101)  > 100 - prob):
            return True
            #TODO request()
        else:
            return False
    def enter_shop_prob_func(shopper):
        if shopper.fav_turn == current_turn :
            prob_turn = 1
        elif shopper.fav_turn == current_turn -1 or shopper.fav_turn == current_turn +1:
            prob_turn = 0.7
        else:
            prob_turn = 0.3

        enter_shop_prob = shopper.trust *(trust_weight) + store_reputation * (store_reputation_weight) + prob_turn * (prob_turn_weight) + objectsFav_prob * (objectsFav_prob_weight)
        enter_shop_prob *= (25 + random.randint(0,3) - random.randint(0,3) )
        return enter_shop_prob
