#Definir clase item

init -2 python:
    import renpy.store as store
    import renpy.exports as renpy
    from operator import attrgetter
# calse item
init -2 python:
    all_items=[]
    class item(store.object):
        #nombre, fancy name, tipo, descripcion, imagen, precio base, precio real, comerciable
        def __init__(self, name, fname, info, type,  img= "", bprice =0, rprice=0, com=True, qty=0):
            global all_items
            self.name = name
            self.fname = fname
            self.type = type
            self.info = info
            self.img = img
            self.bprice = bprice
            self.rprice = rprice
            self.com = True
            self.qty=qty
            if self not in all_items:
                all_items.append(self)

        def add_qty(self, plus):
            self.qty +=plus


##############
#CREAR OBJETOS
init python:
    apple = item("apple", "Apple", "An apple", "food", bprice=2, rprice = 2, img = "images/items/apple_img.png")
    egg = item("egg", "Egg", "An egg", "food", bprice=1, rprice = 1, img ="images/items/apple_img.png")
    fish = item("fish", "Fish", "Raw Fish", "food", bprice=16, rprice=16, img ="images/items/apple_img.png")
