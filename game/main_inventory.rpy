#renpy
#inventory system
screen inventory_text(item, info): #Despliega informaciòn sobre los objetos
    vbox:
        xpos 1200
        ypos 60
        text "[item]"
        spacing 1
        text "[info]"

#desplegar inventarios
screen inventory_display(inv_s, inv_r , max, xcord, ycord ): #Despliega los objetos en la lista del inventario(inventario, maximos espacios en el grid de la gui, cordx, cordy)

    $z=0
    for item in inv_s[1:]:
        $fname= item[0].fname
        $qty = item[1]
        $idle_img = item[0].img
        $info = item[0].info
        vbox:
            xpos xcord
            ypos ycord
            imagebutton idle Transform (idle_img, zoom =0.15) hovered Show("inventory_text", item=fname, info=info) unhovered Hide("inventory_text") action Function(swap_inventory, inv_s, inv_r, item[0], 1)
            text "{color=#000000} x[qty]{/color}"

        if z<max-1:
            $xcord+=250
            $z+=1
        else:
            $ycord+=220
            $xcord -= (max-1)*250
            $z=0

screen display_storage():
    $z=0
    $xcord=160
    $ycord=85
    for item in storage_list[1:]:
        $fname= item[0].fname
        $qty = item[1]
        $idle_img = item[0].img
        $info = item[0].info
        vbox:
            xpos xcord
            ypos ycord
            imagebutton idle Transform (idle_img, zoom =0.15) hovered Show("inventory_text", item=fname, info=info) unhovered Hide("inventory_text") action NullAction()
            text "{color=#000000} x[qty]{/color}"

        if z<3:
            $xcord+=250
            $z+=1
        else:
            $ycord+=220
            $xcord -= (3)*250
            $z=0

# screen swap_to_inventory(item, qty):
#     imagebutton idle "images/inventory/inventory_close.png"  action [Hide("swap_to_inventory")]
#     imagebutton idle "images/gui/inventory_change.png" xalign 0.5 yalign 0.5 action NullAction()
#     $fname = item.fname
#     vbox:
#         xalign 0.5
#         yalign 0.4
#         if renpy.get_screen("inventory_m1"):
#             text "Move from Storage to M1"
#             text "[fname]: [qty]"
#             hbox:
#                 textbutton "Aceptar" action [Function(swap_inventory, storage_list, inventory_m1, item, qty), Hide("swap_to_inventory")]
#                 textbutton "decrese" action SetVariable("qty", qty-1)
#         elif renpy.get_screen("inventory_m2"):
#             text "Move from Storage to M2"
#             text "[fname]: [qty]"
#             hbox:
#                 textbutton "Aceptar" action [Function(swap_inventory, storage_list, inventory_m2, item, qty), Hide("swap_to_inventory")]
#
# screen swap_to_storage(inv, item, qty):
#     imagebutton idle "images/inventory/inventory_close.png"  action [Hide("swap_to_storage")]
#     imagebutton idle "images/gui/inventory_change.png" xalign 0.5 yalign 0.5 action NullAction()
#     $fname = item.fname
#     $qty=qty
#     vbox:
#         xalign 0.5
#         yalign 0.4
#         text "Move to Storage"
#         text "[fname]: [qty]"
#         hbox:
#             textbutton "Accept" action [Function(swap_inventory, inv, storage_list, item, qty), Hide("swap_to_storage")]
#             textbutton "decrese" action SetVariable("qty", qty-1)



##################################################################################################################################################################
screen inventory_main(): #inventario principal del jugador
    modal True
    imagebutton idle "images/inventory/inventory_close.png"  action [Hide("inventory_main"),Hide("display_storage"), Hide("inventory_m1"), Hide("inventory_m2")]
    imagebutton idle Transform("images/inventory/inventory_m.png") xpos 80 ypos 50 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_m_cuadro.png") xpos 80 ypos 50 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_text.png") xpos 1200 ypos 50 action NullAction()


screen inventory_m1(): #inventario de mesa 1

    imagebutton idle Transform("images/inventory/inventory_s.png") xpos 1200 ypos 420 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_s_cuadro.png") xpos 1200 ypos 420 action NullAction()
    use inventory_main
    use inventory_display(storage_list, inventory_m1, 4, 160, 85)
    use inventory_display(inventory_m1, storage_list, 2, 1300, 470)
    textbutton "swap" ypos 400 action [SensitiveIf(isin_inventory(storage_list, apple)), Function(swap_inventory, storage_list, inventory_m1, apple, 1)]


screen inventory_m2(): #inventario de mesa 2

    imagebutton idle Transform("images/inventory/inventory_s.png") xpos 1200 ypos 420 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_s_cuadro.png") xpos 1200 ypos 420 action NullAction()
    use inventory_main
    use inventory_display(storage_list, inventory_m2, 4, 160, 85)
    use inventory_display(inventory_m2, storage_list, 2, 1300, 470 )
    textbutton "SWAP" ypos 400 action [SensitiveIf(isin_inventory(storage_list, apple)), Function(swap_inventory, storage_list, inventory_m2, apple, 1)]
