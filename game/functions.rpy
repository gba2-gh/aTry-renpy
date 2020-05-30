#functions

init python:
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
