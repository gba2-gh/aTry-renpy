#renpy
#inventory system

screen inventory_text(item, info): #Despliega informaciòn sobre los objetos
    vbox:
        xpos 1200
        ypos 60
        text "[item]"
        spacing 1
        text "[info]"

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
            imagebutton idle Transform (idle_img, zoom =0.15) hovered Show("inventory_text", item=item, info=info) unhovered Hide("inventory_text") action NullAction()
            text "{color=#000000} x[qty]{/color}"

        if z<max-1:
            $xcord+=250
            $z+=1
        else:
            $ycord+=220
            $xcord = 150
            $z=0

screen inventory_main(): #inventario principal del jugador
    modal True
    imagebutton idle "images/inventory/inventory_close.png"  action [Hide("inventory_main"), Hide("inventory_m1")]
    imagebutton idle Transform("images/inventory/inventory_m.png") xpos 80 ypos 50 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_m_cuadro.png") xpos 80 ypos 50 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_text.png") xpos 1200 ypos 50 action NullAction()
    use inventory_display(p_inventory, 4, 150, 85 )


screen inventory_m1(): #inventario de mesa 1

    imagebutton idle Transform("images/inventory/inventory_s.png") xpos 1200 ypos 420 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_s_cuadro.png") xpos 1200 ypos 420 action NullAction()
    use inventory_main
    use inventory_display(m1_inventory, 2, 1300, 470 )
    textbutton "swap" ypos 400 action [SensitiveIf(isin_inventory(p_inventory, apple)), Function(swap_inventory, p_inventory, m1_inventory, apple, 1)]
