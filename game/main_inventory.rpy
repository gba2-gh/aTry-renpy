#renpy
#inventory system

screen mainInventory():
    modal True
    imagebutton idle "images/inventary/Inventory_close.png"  action Hide("mainInventory")
    imagebutton idle Transform("images/inventary/inv_bg.png", zoom =0.8) xalign 0.5 yalign 0.5 action NullAction()
    $ycord=100
    for i in p_inventory:
        $item = i[0].fname
        $qty = i[1]
        $idle = i[0].img
        hbox:
            xpos 200
            ypos ycord
            add Transform (idle, zoom =0.1)
            spacing 50
            text "{color=#000000} [item]: [qty]{/color}"
        $ycord+=100

screen m1_inventory():
    modal True
    imagebutton idle "images/inventary/Inventory_close.png"  action Hide("m1_inventory")
    imagebutton idle Transform("images/inventary/inv_bg.png", zoom =0.5) xalign 0.5 yalign 0.5 action NullAction()
    $ycord=100
    for i in m1_inventory:
        $item = i[0].fname
        $qty = i[1]
        $idle = i[0].img
        hbox:
            xpos 200
            ypos ycord
            add Transform (idle, zoom =0.1)
            spacing 50
            text "{color=#000000} [item]: [qty]{/color}"
        $ycord+=100
