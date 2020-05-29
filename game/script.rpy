
define e = Character("Eileen")


label start:
    $p_inventory =[] #player inventory
    $m1_inventory =[] #mesa1

    $p_inventory=[[apple,2], [egg, 1]]
    $add_inventory(p_inventory, fish, 3)

    call screen inicial

    return


screen inicial():
    add "images/main_scene.png"
    textbutton "inventory" action Show("mainInventory")
    textbutton "mesa 1" xpos 200 action Show("m1_inventory")
    textbutton "Remove from main inv" ypos 200 action Function(remove_inventory, p_inventory, apple, 1)
    textbutton "swap" ypos 400 action Function(swap_inventory, p_inventory, m1_inventory, apple, 1)
