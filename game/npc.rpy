#renpy
#NPCs
init -2 python:
    all_shoppers=[]
    class shopper(store.object):
        #nombre, budget, confianza con el vendedor, % preferido de compra, % maximo a aceptar, % minimo a aceptar, turno en que aparece mas seguido,
        def __init__(self, name, budget = 0, trust = 0.1, pref_hag= 0, max_hag= 0, min_hag= 0, fav_turn= 0, random = 2, items=[], img=""):
            global all_shoppers
            self.name = name
            self.budget = budget
            self.trust = trust
            self.pref_hag =  pref_hag
            self.max_hag = max_hag
            self.min_hag = min_hag
            self.fav_turn = fav_turn
            self.items = items
            if self not in all_shoppers:
                all_shoppers.append(self)


##############
#CREAR COMPRADORES
init python:
    girl_shopper = shopper("Girl", budget = 3000, pref_hag = 140, max_hag = 180, min_hag=40, fav_turn = 0, items=[apple])
