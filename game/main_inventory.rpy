#renpy
#inventory system

screen mainInventory():
    modal True
    imagebutton idle "images/inventory/inventory_close.png"  action [Hide("mainInventory"), Hide("m1_inventory")]
    imagebutton idle Transform("images/inventory/inventory_m.png") xpos 80 ypos 50 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_m_cuadro.png") xpos 80 ypos 50 action NullAction()

    $xcord=150
    $ycord=85
    $z=0
    for i in p_inventory:
        $item = i[0].fname
        $qty = i[1]
        $idle = i[0].img
        vbox:
            xpos xcord
            ypos ycord
            add Transform (idle, zoom =0.15)
            text "{color=#000000} x[qty]{/color}"

        if z<3:
            $xcord+=250
            $z+=1
        else:
            $ycord+=220
            $xcord = 150
            $z=0




screen m1_inventory():

    imagebutton idle Transform("images/inventory/inventory_s.png") xpos 1200 ypos 420 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_s_cuadro.png") xpos 1200 ypos 420 action NullAction()
    imagebutton idle Transform("images/inventory/inventory_text.png") xpos 1200 ypos 50 action NullAction()
    textbutton "swap" ypos 400 action [SensitiveIf(isin_inventory(p_inventory, apple)), Function(swap_inventory, p_inventory, m1_inventory, apple, 1)]
    $xcord=1300
    $ycord=470
    $z=0
    for i in m1_inventory:
        $item = i[0].fname
        $qty = i[1]
        $idle = i[0].img
        vbox:
            xpos xcord
            ypos ycord
            add Transform (idle, zoom =0.15)
            text "{color=#000000} x[qty]{/color}"

        if z<3:
            $xcord+=250
            $z+=1
        else:
            $ycord+=220
            $xcord = 150
            $z=0
