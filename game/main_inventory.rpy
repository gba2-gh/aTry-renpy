#renpy
#inventory system
screen inventory_text(item, info): #Despliega informaciòn sobre los objetos
    vbox:
        xpos 1200
        ypos 60
        text "[item]"
        spacing 1
        text "[info]"

#desplegar inventarios secundarios
screen inventory_display(inv, max, xcord, ycord): #Despliega los objetos en la lista del inventario(inventario, maximos espacios en el grid de la gui, cordx, cordy)

    $z=0
    for i in inv:
        $item = i[0].fname
        $qty = i[1]
        $idle_img = i[0].img
        $info = i[0].info
        vbox:
            xpos xcord
            ypos ycord
            imagebutton idle Transform (idle_img, zoom =0.15) hovered Show("inventory_text", item=item, info=info) unhovered Hide("inventory_text") action Show("swap_to_storage", inv=inv, item=i[0], qty=qty)
            text "{color=#000000} x[qty]{/color}"

        if z<max-1:
            $xcord+=250
            $z+=1
        else:
            $ycord+=220
            $xcord = 150
            $z=0


screen swap_to_inventory(item, qty):
    imagebutton idle "images/inventory/inventory_close.png"  action [Hide("swap_to_inventory")]
    imagebutton idle "images/gui/inventory_change.png" xalign 0.5 yalign 0.5 action NullAction()
    $fname = item.fname
    vbox:
        xalign 0.5
        yalign 0.4
        if renpy.get_screen("inventory_m1"):
            text "Move from Storage to M1"
            text "[fname]: [qty]"
            hbox:
                textbutton "Aceptar" action [Function(swap_inventory, storage_list, inventory_m1, item, qty), Hide("swap_to_inventory")]
                textbutton "decrese" action SetVariable("qty", qty-1)
        elif renpy.get_screen("inventory_m2"):
            text "Move from Storage to M2"
            text "[fname]: [qty]"
            hbox:
                textbutton "Aceptar" action [Function(swap_inventory, storage_list, inventory_m2, item, qty), Hide("swap_to_inventory")]

screen swap_to_storage(inv, item, qty):
    imagebutton idle "images/inventory/inventory_close.png"  action [Hide("swap_to_storage")]
    imagebutton idle "images/gui/inventory_change.png" xalign 0.5 yalign 0.5 action NullAction()
    $fname = item.fname
    $qty=qty
    vbox:
        xalign 0.5
        yalign 0.4
        text "Move to Storage"
        text "[fname]: [qty]"
        hbox:
            textbutton "Accept" action [Function(swap_inventory, inv, storage_list, item, qty), Hide("swap_to_storage")]
            textbutton "decrese" action SetVariable("qty", qty-1)



##################################################################################################################################################################
screen inventory_main(): #inventario principal del jugador
    modal True
    imagebutton idle "images/inventory/inventory_close.png"  action [Hide("inventory_main"), Hide("inventory_m1"), Hide("inventory_m2")]
    imagebutton idle Transform("images/inventory/inventory_m.png") xpos 80 ypos 50 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_m_cuadro.png") xpos 80 ypos 50 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_text.png") xpos 1200 ypos 50 action NullAction()
    $xcord=160
    $ycord=85
    $z=0
    for i in storage_list:
        $item = i[0].fname
        $qty = i[1]
        $idle_img = i[0].img
        $info = i[0].info
        vbox:
            xpos xcord
            ypos ycord
            imagebutton idle Transform (idle_img, zoom =0.15) hovered Show("inventory_text", item=item, info=info) unhovered Hide("inventory_text") action Show("swap_to_inventory", item=i[0], qty=qty)
            text "{color=#000000} x[qty]{/color}"

        if z<4-1:
            $xcord+=250
            $z+=1
        else:
            $ycord+=220
            $xcord = 150
            $z=0


screen inventory_m1(): #inventario de mesa 1

    imagebutton idle Transform("images/inventory/inventory_s.png") xpos 1200 ypos 420 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_s_cuadro.png") xpos 1200 ypos 420 action NullAction()
    use inventory_main
    use inventory_display(inventory_m1, 2, 1300, 470)
    textbutton "swap" ypos 400 action [SensitiveIf(isin_inventory(storage_list, apple)), Function(swap_inventory, storage_list, inventory_m1, apple, 1)]


screen inventory_m2(): #inventario de mesa 2

    imagebutton idle Transform("images/inventory/inventory_s.png") xpos 1200 ypos 420 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_s_cuadro.png") xpos 1200 ypos 420 action NullAction()
    use inventory_main
    use inventory_display(inventory_m2, 2, 1300, 470 )
    textbutton "SWAP" ypos 400 action [SensitiveIf(isin_inventory(storage_list, apple)), Function(swap_inventory, storage_list, inventory_m2, apple, 1)]
