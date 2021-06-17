@namespace
class SpriteKind:
    Powerup1 = SpriteKind.create()
    Ammo = SpriteKind.create()
    Boss = SpriteKind.create()
    Bossprojectile = SpriteKind.create()
@namespace
class StatusBarKind:
    Ammo2 = StatusBarKind.create()

def on_combos_attach_combo():
    global Skudd_rettning
    Skudd_rettning = 180
    animation.stop_animation(animation.AnimationTypes.ALL, Player1)
    animation.run_image_animation(Player1,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . . f e 4 d d d d 4 e f e . . 
                        . . f e f 2 2 2 2 e d d 4 e . . 
                        . . e 4 f 2 2 2 2 e d d e . . . 
                        . . . . f 4 4 5 5 f e e . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 2 2 2 2 2 2 e f f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 2 2 2 2 f e f . . 
                        . . . e d d e 2 2 2 2 f 4 e . . 
                        . . . . e e f 5 5 4 4 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        200,
        True)
controller.combos.attach_combo(controller.combos.id_to_string(controller.combos.ID.DOWN),
    on_combos_attach_combo)

def on_combos_attach_combo2():
    global Ammo1
    Ammo1 += -10
controller.combos.attach_combo("a", on_combos_attach_combo2)

def on_a_pressed():
    global projectile
    if Ammo1 > 1:
        music.pew_pew.play()
        if Skudd_rettning == 0:
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . 4 4 4 5 5 4 4 4 . . . . 
                                    . . . 3 3 3 3 4 4 4 4 4 4 . . . 
                                    . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
                                    . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
                                    . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
                                    . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
                                    . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
                                    . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
                                    . . . 4 2 2 2 2 2 2 2 2 4 . . . 
                                    . . . . 4 4 2 2 2 2 4 4 . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                Player1,
                0,
                -120)
        elif Skudd_rettning == 90:
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . 4 4 4 5 5 4 4 4 . . . . 
                                    . . . 3 3 3 3 4 4 4 4 4 4 . . . 
                                    . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
                                    . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
                                    . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
                                    . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
                                    . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
                                    . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
                                    . . . 4 2 2 2 2 2 2 2 2 4 . . . 
                                    . . . . 4 4 2 2 2 2 4 4 . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                Player1,
                120,
                0)
        elif Skudd_rettning == 180:
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . 4 4 4 5 5 4 4 4 . . . . 
                                    . . . 3 3 3 3 4 4 4 4 4 4 . . . 
                                    . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
                                    . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
                                    . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
                                    . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
                                    . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
                                    . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
                                    . . . 4 2 2 2 2 2 2 2 2 4 . . . 
                                    . . . . 4 4 2 2 2 2 4 4 . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                Player1,
                0,
                120)
        elif Skudd_rettning == 270:
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . 4 4 4 5 5 4 4 4 . . . . 
                                    . . . 3 3 3 3 4 4 4 4 4 4 . . . 
                                    . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
                                    . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
                                    . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
                                    . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
                                    . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
                                    . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
                                    . . . 4 2 2 2 2 2 2 2 2 4 . . . 
                                    . . . . 4 4 2 2 2 2 4 4 . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                Player1,
                -120,
                0)
    else:
        game.set_dialog_text_color(15)
        game.show_long_text("Tom for ammo", DialogLayout.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    info.change_life_by(-1)
    music.small_crash.play()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def on_on_overlap(sprite, otherSprite):
    global NextLevel_2
    Boss_statusbar.value += -4
    sprite.destroy()
    pause(100)
    if Boss_statusbar.value < 10:
        Boss2.destroy()
        NextLevel_2 = 3
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Boss, on_on_overlap)

def on_overlap_tile2(sprite, location):
    sprite.destroy()
scene.on_overlap_tile(SpriteKind.projectile,
    sprites.dungeon.floor_light0,
    on_overlap_tile2)

def next_level():
    global NextLevel, Ammo1, Enemey1, Powerup12, Ammokasse, Boss2, Boss_statusbar
    for value in sprites.all_of_kind(SpriteKind.enemy):
        value.destroy()
    for value2 in sprites.all_of_kind(SpriteKind.Ammo):
        value2.destroy()
    for value3 in sprites.all_of_kind(SpriteKind.Powerup1):
        value3.destroy()
    for value4 in sprites.all_of_kind(SpriteKind.Bossprojectile):
        value4.destroy()
    NextLevel += 1
    music.beam_up.play()
    Ammo1 = 100
    if NextLevel == 1:
        game.splash("Level 1")
        tiles.set_tilemap(tilemap("""
            level1
        """))
        for index in range(1):
            Enemey1 = sprites.create(img("""
                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ..........ffff..........
                                    ........ff1111ff........
                                    .......fb111111bf.......
                                    .......f11111111f.......
                                    ......fd11111111df......
                                    ......fd11111111df......
                                    ......fddd1111dddf......
                                    ......fbdbfddfbdbf......
                                    ......fcdcf11fcdcf......
                                    .......fb111111bf.......
                                    ......fffcdb1bdffff.....
                                    ....fc111cbfbfc111cf....
                                    ....f1b1b1ffff1b1b1f....
                                    ....fbfbffffffbfbfbf....
                                    .........ffffff.........
                                    ...........fff..........
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                """),
                SpriteKind.enemy)
            tiles.place_on_random_tile(Enemey1, sprites.dungeon.floor_dark5)
            Enemey1.follow(Player1, 50)
    elif NextLevel == 2:
        game.splash("Level 2")
        if randint(1, 2) == 1:
            tiles.set_tilemap(tilemap("""
                level2
            """))
        else:
            tiles.set_tilemap(tilemap("""
                level16
            """))
        for index2 in range(3):
            Enemey1 = sprites.create(img("""
                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ..........ffff..........
                                    ........ff1111ff........
                                    .......fb111111bf.......
                                    .......f11111111f.......
                                    ......fd11111111df......
                                    ......fd11111111df......
                                    ......fddd1111dddf......
                                    ......fbdbfddfbdbf......
                                    ......fcdcf11fcdcf......
                                    .......fb111111bf.......
                                    ......fffcdb1bdffff.....
                                    ....fc111cbfbfc111cf....
                                    ....f1b1b1ffff1b1b1f....
                                    ....fbfbffffffbfbfbf....
                                    .........ffffff.........
                                    ...........fff..........
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                """),
                SpriteKind.enemy)
            tiles.place_on_random_tile(Enemey1, sprites.dungeon.floor_dark5)
            Enemey1.follow(Player1, 50)
        for index3 in range(2):
            Powerup12 = sprites.create(img("""
                    . . . . . . b b b b . . . . . . 
                                    . . . . . . b 4 4 4 b . . . . . 
                                    . . . . . . b b 4 4 4 b . . . . 
                                    . . . . . b 4 b b b 4 4 b . . . 
                                    . . . . b d 5 5 5 4 b 4 4 b . . 
                                    . . . . b 3 2 3 5 5 4 e 4 4 b . 
                                    . . . b d 2 2 2 5 7 5 4 e 4 4 e 
                                    . . . b 5 3 2 3 5 5 5 5 e e e e 
                                    . . b d 7 5 5 5 3 2 3 5 5 e e e 
                                    . . b 5 5 5 5 5 2 2 2 5 5 d e e 
                                    . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
                                    . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
                                    b d 3 2 d 5 5 5 d d d 4 4 . . . 
                                    b 5 5 5 5 d d 4 4 4 4 . . . . . 
                                    4 d d d 4 4 4 . . . . . . . . . 
                                    4 4 4 4 . . . . . . . . . . . .
                """),
                SpriteKind.Powerup1)
            tiles.place_on_random_tile(Powerup12, sprites.dungeon.dark_ground_center)
        for index4 in range(1):
            Ammokasse = sprites.create(img("""
                    . . b b b b b b b b b b b b . . 
                                    . b e 4 4 4 4 4 4 4 4 4 4 e b . 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b b b b b b b d d b b b b b b b 
                                    c b b b b b b c c b b b b b b c 
                                    c c c c c c b c c b c c c c c c 
                                    b e e e e e c b b c e e e e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b c e e e e e e e e e e e e c b 
                                    b b b b b b b b b b b b b b b b 
                                    . b b . . . . . . . . . . b b .
                """),
                SpriteKind.Ammo)
            tiles.place_on_random_tile(Ammokasse, sprites.dungeon.dark_ground_center)
    elif NextLevel == 3:
        game.splash("Level 3")
        if randint(1, 2) == 1:
            tiles.set_tilemap(tilemap("""
                level3
            """))
        else:
            tiles.set_tilemap(tilemap("""
                level14
            """))
        for index5 in range(6):
            Enemey1 = sprites.create(img("""
                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ..........ffff..........
                                    ........ff1111ff........
                                    .......fb111111bf.......
                                    .......f11111111f.......
                                    ......fd11111111df......
                                    ......fd11111111df......
                                    ......fddd1111dddf......
                                    ......fbdbfddfbdbf......
                                    ......fcdcf11fcdcf......
                                    .......fb111111bf.......
                                    ......fffcdb1bdffff.....
                                    ....fc111cbfbfc111cf....
                                    ....f1b1b1ffff1b1b1f....
                                    ....fbfbffffffbfbfbf....
                                    .........ffffff.........
                                    ...........fff..........
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                """),
                SpriteKind.enemy)
            tiles.place_on_random_tile(Enemey1, sprites.dungeon.floor_dark5)
            Enemey1.follow(Player1, 50)
        for index6 in range(2):
            Powerup12 = sprites.create(img("""
                    . . . . . . b b b b . . . . . . 
                                    . . . . . . b 4 4 4 b . . . . . 
                                    . . . . . . b b 4 4 4 b . . . . 
                                    . . . . . b 4 b b b 4 4 b . . . 
                                    . . . . b d 5 5 5 4 b 4 4 b . . 
                                    . . . . b 3 2 3 5 5 4 e 4 4 b . 
                                    . . . b d 2 2 2 5 7 5 4 e 4 4 e 
                                    . . . b 5 3 2 3 5 5 5 5 e e e e 
                                    . . b d 7 5 5 5 3 2 3 5 5 e e e 
                                    . . b 5 5 5 5 5 2 2 2 5 5 d e e 
                                    . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
                                    . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
                                    b d 3 2 d 5 5 5 d d d 4 4 . . . 
                                    b 5 5 5 5 d d 4 4 4 4 . . . . . 
                                    4 d d d 4 4 4 . . . . . . . . . 
                                    4 4 4 4 . . . . . . . . . . . .
                """),
                SpriteKind.Powerup1)
            tiles.place_on_random_tile(Powerup12, sprites.dungeon.dark_ground_center)
        for index7 in range(2):
            Ammokasse = sprites.create(img("""
                    . . b b b b b b b b b b b b . . 
                                    . b e 4 4 4 4 4 4 4 4 4 4 e b . 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b b b b b b b d d b b b b b b b 
                                    c b b b b b b c c b b b b b b c 
                                    c c c c c c b c c b c c c c c c 
                                    b e e e e e c b b c e e e e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b c e e e e e e e e e e e e c b 
                                    b b b b b b b b b b b b b b b b 
                                    . b b . . . . . . . . . . b b .
                """),
                SpriteKind.Ammo)
            tiles.place_on_random_tile(Ammokasse, sprites.dungeon.dark_ground_center)
    elif NextLevel == 4:
        game.splash("Level 4")
        tiles.set_tilemap(tilemap("""
            level0
        """))
        for index8 in range(2):
            Powerup12 = sprites.create(img("""
                    . . . . . . b b b b . . . . . . 
                                    . . . . . . b 4 4 4 b . . . . . 
                                    . . . . . . b b 4 4 4 b . . . . 
                                    . . . . . b 4 b b b 4 4 b . . . 
                                    . . . . b d 5 5 5 4 b 4 4 b . . 
                                    . . . . b 3 2 3 5 5 4 e 4 4 b . 
                                    . . . b d 2 2 2 5 7 5 4 e 4 4 e 
                                    . . . b 5 3 2 3 5 5 5 5 e e e e 
                                    . . b d 7 5 5 5 3 2 3 5 5 e e e 
                                    . . b 5 5 5 5 5 2 2 2 5 5 d e e 
                                    . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
                                    . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
                                    b d 3 2 d 5 5 5 d d d 4 4 . . . 
                                    b 5 5 5 5 d d 4 4 4 4 . . . . . 
                                    4 d d d 4 4 4 . . . . . . . . . 
                                    4 4 4 4 . . . . . . . . . . . .
                """),
                SpriteKind.Powerup1)
            tiles.place_on_random_tile(Powerup12, sprites.dungeon.dark_ground_center)
        for index9 in range(6):
            Enemey1 = sprites.create(img("""
                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ..........ffff..........
                                    ........ff1111ff........
                                    .......fb111111bf.......
                                    .......f11111111f.......
                                    ......fd11111111df......
                                    ......fd11111111df......
                                    ......fddd1111dddf......
                                    ......fbdbfddfbdbf......
                                    ......fcdcf11fcdcf......
                                    .......fb111111bf.......
                                    ......fffcdb1bdffff.....
                                    ....fc111cbfbfc111cf....
                                    ....f1b1b1ffff1b1b1f....
                                    ....fbfbffffffbfbfbf....
                                    .........ffffff.........
                                    ...........fff..........
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                """),
                SpriteKind.enemy)
            tiles.place_on_random_tile(Enemey1, sprites.dungeon.floor_dark5)
            Enemey1.follow(Player1, 50)
        for index10 in range(4):
            Ammokasse = sprites.create(img("""
                    . . b b b b b b b b b b b b . . 
                                    . b e 4 4 4 4 4 4 4 4 4 4 e b . 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b b b b b b b d d b b b b b b b 
                                    c b b b b b b c c b b b b b b c 
                                    c c c c c c b c c b c c c c c c 
                                    b e e e e e c b b c e e e e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b c e e e e e e e e e e e e c b 
                                    b b b b b b b b b b b b b b b b 
                                    . b b . . . . . . . . . . b b .
                """),
                SpriteKind.Ammo)
            tiles.place_on_random_tile(Ammokasse, sprites.dungeon.dark_ground_center)
    elif NextLevel == 5:
        game.splash("Level 5")
        if randint(1, 3) == 1:
            tiles.set_tilemap(tilemap("""
                level7
            """))
            info.change_score_by(1)
        elif randint(1, 3) == 2:
            tiles.set_tilemap(tilemap("""
                level12
            """))
            info.change_score_by(2)
        elif randint(1, 3) == 3:
            tiles.set_tilemap(tilemap("""
                level13
            """))
            info.change_score_by(3)
    elif NextLevel == 6:
        game.splash("Bosslevel")
        tiles.set_tilemap(tilemap("""
            Boss level
        """))
        for index11 in range(7):
            Ammokasse = sprites.create(img("""
                    . . b b b b b b b b b b b b . . 
                                    . b e 4 4 4 4 4 4 4 4 4 4 e b . 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                                    b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b b b b b b b d d b b b b b b b 
                                    c b b b b b b c c b b b b b b c 
                                    c c c c c c b c c b c c c c c c 
                                    b e e e e e c b b c e e e e e b 
                                    b e e e e e e e e e e e e e e b 
                                    b c e e e e e e e e e e e e c b 
                                    b b b b b b b b b b b b b b b b 
                                    . b b . . . . . . . . . . b b .
                """),
                SpriteKind.Ammo)
            tiles.place_on_random_tile(Ammokasse, sprites.dungeon.dark_ground_center)
        Boss2 = sprites.create(img("""
                . . . . . f f f f f . . . . . . 
                            . . . . f e e e e e f . . . . . 
                            . . . f d d d d d d e f . . . . 
                            . . f d f f d d f f d f f . . . 
                            . c d d d e e d d d d e d f . . 
                            . c d c d d d d c d d e f f . . 
                            . c d d c c c c d d d e f f f f 
                            . . c d d d d d d d e f f b d f 
                            . . . c d d d d e e f f f d d f 
                            . . . . f f f e e f e e e f f f 
                            . . . . f e e e e e e e f f f . 
                            . . . f e e e e e e f f f e f . 
                            . . f f e e e e f f f f f e f . 
                            . f b d f e e f b b f f f e f . 
                            . f d d f f f f d d b f f f f . 
                            . f f f f f f f f f f f f f . .
            """),
            SpriteKind.Boss)
        Boss2.follow(Player1, 30)
        Boss_statusbar = statusbars.create(25, 4, StatusBarKind.enemy_health)
        Boss_statusbar.attach_to_sprite(Boss2, -25, 0)
        Boss_statusbar.value = 100
        Boss_statusbar.set_color(5, 2)
    elif NextLevel == 7 and NextLevel_2 == 3:
        tiles.set_tilemap(tilemap("""
            level10
        """))
        tiles.place_on_random_tile(Player1, sprites.dungeon.floor_dark_diamond)
        for index12 in range(10):
            Powerup12 = sprites.create(img("""
                    . . . . . . b b b b . . . . . . 
                                    . . . . . . b 4 4 4 b . . . . . 
                                    . . . . . . b b 4 4 4 b . . . . 
                                    . . . . . b 4 b b b 4 4 b . . . 
                                    . . . . b d 5 5 5 4 b 4 4 b . . 
                                    . . . . b 3 2 3 5 5 4 e 4 4 b . 
                                    . . . b d 2 2 2 5 7 5 4 e 4 4 e 
                                    . . . b 5 3 2 3 5 5 5 5 e e e e 
                                    . . b d 7 5 5 5 3 2 3 5 5 e e e 
                                    . . b 5 5 5 5 5 2 2 2 5 5 d e e 
                                    . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
                                    . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
                                    b d 3 2 d 5 5 5 d d d 4 4 . . . 
                                    b 5 5 5 5 d d 4 4 4 4 . . . . . 
                                    4 d d d 4 4 4 . . . . . . . . . 
                                    4 4 4 4 . . . . . . . . . . . .
                """),
                SpriteKind.Powerup1)
            tiles.place_on_random_tile(Powerup12, sprites.dungeon.floor_dark2)
    tiles.place_on_random_tile(Player1, sprites.dungeon.floor_dark_diamond)

def on_combos_attach_combo3():
    global Skudd_rettning
    Skudd_rettning = 0
    animation.stop_animation(animation.AnimationTypes.ALL, Player1)
    animation.run_image_animation(Player1,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f f 2 f e f . . 
                        . . f f f 2 f e e 2 2 f f f . . 
                        . . f e 2 f f e e 2 f e e f . . 
                        . f f e f f e e e f e e e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . . e f f f f f f f f 4 e . . 
                        . . . 4 f 2 2 2 2 2 e d d 4 . . 
                        . . . e f f f f f f e e 4 . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e f 2 f f f 2 f 2 e f . . 
                        . . f f f 2 2 e e f 2 f f f . . 
                        . . f e e f 2 e e f f 2 e f . . 
                        . f f e e e f e e e f f e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f e . . . 
                        . . 4 d d e 2 2 2 2 2 f 4 . . . 
                        . . . 4 e e f f f f f f e . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        200,
        True)
controller.combos.attach_combo(controller.combos.id_to_string(controller.combos.ID.UP),
    on_combos_attach_combo3)

def on_overlap_tile3(sprite, location):
    global NextLevel
    music.big_crash.play()
    game.splash("-1 level")
    NextLevel += -2
    next_level()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles10,
    on_overlap_tile3)

def on_on_overlap2(sprite, otherSprite):
    global Ammo1
    music.power_up.play()
    otherSprite.destroy()
    Ammo1 += 40
sprites.on_overlap(SpriteKind.player, SpriteKind.Ammo, on_on_overlap2)

def on_overlap_tile4(sprite, location):
    info.change_life_by(-1)
    music.small_crash.play()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile4)

def on_on_overlap3(sprite, otherSprite):
    music.jump_down.play()
    sprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap3)

def on_combos_attach_combo4():
    global Skudd_rettning
    Skudd_rettning = 90
    animation.stop_animation(animation.AnimationTypes.ALL, Player1)
    animation.run_image_animation(Player1,
        [img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e e e d d d f . . . 
                        . . . . . f 4 d d e 4 e f . . . 
                        . . . . . f e d d e 2 2 f . . . 
                        . . . . f f f e e f 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . 4 d d e 4 4 4 e f . . . 
                        . . . . e d d e 2 2 2 2 f . . . 
                        . . . . f e e f 4 4 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """)],
        200,
        True)
controller.combos.attach_combo(controller.combos.id_to_string(controller.combos.ID.RIGHT),
    on_combos_attach_combo4)

def on_on_overlap4(sprite, otherSprite):
    info.change_life_by(-1)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Bossprojectile, on_on_overlap4)

def on_on_overlap5(sprite, otherSprite):
    otherSprite.destroy()
    music.ba_ding.play()
    info.change_life_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Powerup1, on_on_overlap5)

def on_overlap_tile5(sprite, location):
    next_level()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_large,
    on_overlap_tile5)

def on_combos_attach_combo5():
    global Skudd_rettning
    Skudd_rettning = 270
    animation.stop_animation(animation.AnimationTypes.ALL, Player1)
    animation.run_image_animation(Player1,
        [img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 2 2 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """),
            img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e d d 4 . . . . 
                        . . . f 2 2 2 2 e d d e . . . . 
                        . . f f 5 5 4 4 f e e f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """)],
        200,
        True)
controller.combos.attach_combo(controller.combos.id_to_string(controller.combos.ID.LEFT),
    on_combos_attach_combo5)

def on_on_overlap6(sprite, otherSprite):
    global Ammo1, Speed1
    music.knock.play()
    info.change_score_by(1)
    sprite.destroy()
    otherSprite.destroy()
    if randint(1, 5) == 3:
        music.ba_ding.play()
        game.set_dialog_text_color(2)
        game.show_long_text("Ekstra liv", DialogLayout.BOTTOM)
        info.change_life_by(1)
        Ammo1 += 10
    elif randint(1, 5) == 3:
        music.magic_wand.play()
        Speed1 += 20
        game.set_dialog_text_color(6)
        game.show_long_text("Ekstra fart", DialogLayout.TOP)
        Ammo1 += 10
    elif randint(1, 5) == 3:
        game.set_dialog_text_color(6)
        game.show_long_text("Ekstra ammo", DialogLayout.CENTER)
        Ammo1 += 40
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap6)

def on_overlap_tile6(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile6)

def on_on_overlap7(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.Bossprojectile,
    on_on_overlap7)

def on_on_overlap8(sprite, otherSprite):
    info.change_life_by(-1)
    pause(200)
sprites.on_overlap(SpriteKind.player, SpriteKind.Boss, on_on_overlap8)

Life = 0
BossProjectile: Sprite = None
Boss_skudd = 0
Ammokasse: Sprite = None
Powerup12: Sprite = None
Enemey1: Sprite = None
NextLevel_2 = 0
Boss2: Sprite = None
Boss_statusbar: StatusBarSprite = None
projectile: Sprite = None
Skudd_rettning = 0
Ammo1 = 0
Player1: Sprite = None
NextLevel = 0
NextLevel = 0
Speed1 = 100
Player1 = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Player1, Speed1, Speed1)
scene.camera_follow_sprite(Player1)
next_level()
info.set_life(3)
info.set_score(0)
Ammo1 = 100
statusbar = statusbars.create(20, 4, StatusBarKind.Ammo2)
statusbar.max = 100
statusbar.set_position(113, 5)
statusbar.set_color(7, 2)
statusbar.set_label("Ammo")

def on_forever():
    if NextLevel == 1:
        music.play_melody("E B C5 A B G A F ", 120)
    elif NextLevel == 2:
        music.play_melody("D A B G A F G E ", 120)
    elif NextLevel == 3:
        music.play_melody("C G A F G E F D ", 120)
    elif NextLevel == 4:
        music.play_melody("D A B F A E G D ", 120)
    elif NextLevel == 5:
        music.play_melody("F A A B A G B G ", 120)
    elif NextLevel == 6:
        music.play_melody("E C D C E C C D ", 120)
    elif NextLevel == 7:
        music.play_melody("F G A F G A F G ", 120)
forever(on_forever)

def on_forever2():
    global Ammo1
    if Ammo1 > 100:
        Ammo1 = 100
forever(on_forever2)

def on_forever3():
    statusbar.value = Ammo1
forever(on_forever3)

def on_forever4():
    Enemey1.follow(Player1, 50)
forever(on_forever4)

def on_forever5():
    tiles.create_sprites_on_tiles(sprites.dungeon.floor_dark5, SpriteKind.enemy)
    tiles.replace_all_tiles(sprites.dungeon.floor_dark5,
        sprites.dungeon.dark_ground_center)
forever(on_forever5)

def on_forever6():
    global BossProjectile
    if Boss_skudd == 1:
        BossProjectile = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . c c . . . . . . . . 
                            . . . . c a f b c . . . . . . . 
                            . . . . b f f b c c . . . . . . 
                            . . . a a f b a b a c . . . . . 
                            . . . c a c b b f f b . . . . . 
                            . . . . b f f b f a b . . . . . 
                            . . . . a f f b b b a . . . . . 
                            . . . . . a b b c c . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Bossprojectile)
        BossProjectile.follow(Player1, 50)
forever(on_forever6)

def on_forever7():
    if NextLevel == 6:
        Enemey1.destroy()
forever(on_forever7)

def on_forever8():
    global Life
    Life = info.life()
forever(on_forever8)

def on_forever9():
    global Boss_skudd
    if NextLevel == 6:
        pause(5000)
        Boss_skudd += 1
        pause(20)
        Boss_skudd = 0
forever(on_forever9)
