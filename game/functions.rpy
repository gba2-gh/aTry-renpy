#renpy
#functions

init python:

#########INVENTORY
    def add_inventory(inv, item, qty):
        if item.stack == True:
            if (isin_inventory(inv, item)):
                for i in inv[1:]:
                    if i[0].name == item.name:
                        i[1] += qty
            else:
                inv.append([item, qty])
        else:
            inv.append([item, qty])



    def remove_inventory(inv, item, qty):
        for i in inv[1:]:
            if( item in i):
                i[1] -= qty #excepcion para qty> i
                if(i[1] <=0):
                    del inv[inv.index(i)]

    def remove_inventory_id(inv_id, item, qty):
        if inv_id == 1:
            remove_inventory(inventory_m1, item, qty)
        elif inv_id == 2:
            remove_inventory(inventory_m2, item, qty)

    def isin_inventory(inv, item):
        for i in inv[1:]:
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

    def search_for_items(shopper, inventory):
        items=[]
        for item_i in shopper.fav_items:
            for item_j in inventory[1:]:
                if item_i == item_j[0]:
                    items.append([item_j[0],inventory[0]])  #inventory[0] ==shelf

        return items

    def get_shopper_state(shopper): #Esta función pasa [estado del npc, tipo de npc y el objeto elegido]
        rand = random.randint(0,100)
        items_to_choose =[]
        if rand <= 70:#compra
            items_to_choose += search_for_items(shopper,inventory_m1)
            items_to_choose += search_for_items(shopper,inventory_m2)
            #items_to_choose += [[apple, 1], [apple, 2]]
            if len(items_to_choose) > 0:
                item_picked= random.choice(items_to_choose)
                #remove_inventory_id(item_picked[1], item_picked[0], 1)
                return [1, shopper, item_picked] #Comprar
            else:
                return [0]
        elif 70 < rand <= 80:
            item_picked =0
            return [2, shopper, item_picked] #Pedir
        elif 80 < rand <= 90:
            item_picked=0
            return [3, shopper, item_picked] #Vender
        elif 90 < rand <= 100:
            item_picked=0
            return [4, shopper, item_picked] #Encargo
