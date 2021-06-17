namespace SpriteKind {
    export const Powerup1 = SpriteKind.create()
    export const Ammo = SpriteKind.create()
    export const Boss = SpriteKind.create()
    export const Bossprojectile = SpriteKind.create()
}
namespace StatusBarKind {
    export const Ammo2 = StatusBarKind.create()
}
controller.combos.attachCombo(controller.combos.idToString(controller.combos.ID.down), function () {
    Skudd_rettning = 180
    animation.stopAnimation(animation.AnimationTypes.All, Player1)
    animation.runImageAnimation(
    Player1,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
controller.combos.attachCombo("a", function () {
    Ammo1 += -10
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Ammo1 > 1) {
        music.pewPew.play()
        if (Skudd_rettning == 0) {
            projectile = sprites.createProjectileFromSprite(img`
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
                `, Player1, 0, -120)
        } else if (Skudd_rettning == 90) {
            projectile = sprites.createProjectileFromSprite(img`
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
                `, Player1, 120, 0)
        } else if (Skudd_rettning == 180) {
            projectile = sprites.createProjectileFromSprite(img`
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
                `, Player1, 0, 120)
        } else if (Skudd_rettning == 270) {
            projectile = sprites.createProjectileFromSprite(img`
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
                `, Player1, -120, 0)
        }
    } else {
        game.setDialogTextColor(15)
        game.showLongText("Tom for ammo", DialogLayout.Bottom)
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite, location) {
    info.changeLifeBy(-1)
    music.smallCrash.play()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Boss, function (sprite, otherSprite) {
    Boss_statusbar.value += -4
    sprite.destroy()
    pause(100)
    if (Boss_statusbar.value < 10) {
        Boss2.destroy(effects.spray, 500)
        NextLevel_2 = 3
    }
})
scene.onOverlapTile(SpriteKind.Projectile, sprites.dungeon.floorLight0, function (sprite, location) {
    sprite.destroy()
})
function next_level () {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        value.destroy()
    }
    for (let value2 of sprites.allOfKind(SpriteKind.Ammo)) {
        value2.destroy()
    }
    for (let value3 of sprites.allOfKind(SpriteKind.Powerup1)) {
        value3.destroy()
    }
    for (let value4 of sprites.allOfKind(SpriteKind.Bossprojectile)) {
        value4.destroy()
    }
    NextLevel += 1
    music.beamUp.play()
    Ammo1 = 100
    if (NextLevel == 1) {
        game.splash("Level 1")
        tiles.setTilemap(tilemap`level1`)
        for (let index = 0; index < 1; index++) {
            Enemey1 = sprites.create(img`
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
                `, SpriteKind.Enemy)
            tiles.placeOnRandomTile(Enemey1, sprites.dungeon.floorDark5)
            Enemey1.follow(Player1, 50)
        }
    } else if (NextLevel == 2) {
        game.splash("Level 2")
        if (randint(1, 2) == 1) {
            tiles.setTilemap(tilemap`level2`)
        } else {
            tiles.setTilemap(tilemap`level16`)
        }
        for (let index = 0; index < 3; index++) {
            Enemey1 = sprites.create(img`
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
                `, SpriteKind.Enemy)
            tiles.placeOnRandomTile(Enemey1, sprites.dungeon.floorDark5)
            Enemey1.follow(Player1, 50)
        }
        for (let index = 0; index < 2; index++) {
            Powerup12 = sprites.create(img`
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
                `, SpriteKind.Powerup1)
            tiles.placeOnRandomTile(Powerup12, sprites.dungeon.darkGroundCenter)
        }
        for (let index = 0; index < 1; index++) {
            Ammokasse = sprites.create(img`
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
                `, SpriteKind.Ammo)
            tiles.placeOnRandomTile(Ammokasse, sprites.dungeon.darkGroundCenter)
        }
    } else if (NextLevel == 3) {
        game.splash("Level 3")
        if (randint(1, 2) == 1) {
            tiles.setTilemap(tilemap`level3`)
        } else {
            tiles.setTilemap(tilemap`level14`)
        }
        for (let index = 0; index < 6; index++) {
            Enemey1 = sprites.create(img`
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
                `, SpriteKind.Enemy)
            tiles.placeOnRandomTile(Enemey1, sprites.dungeon.floorDark5)
            Enemey1.follow(Player1, 50)
        }
        for (let index = 0; index < 2; index++) {
            Powerup12 = sprites.create(img`
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
                `, SpriteKind.Powerup1)
            tiles.placeOnRandomTile(Powerup12, sprites.dungeon.darkGroundCenter)
        }
        for (let index = 0; index < 2; index++) {
            Ammokasse = sprites.create(img`
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
                `, SpriteKind.Ammo)
            tiles.placeOnRandomTile(Ammokasse, sprites.dungeon.darkGroundCenter)
        }
    } else if (NextLevel == 4) {
        game.splash("Level 4")
        tiles.setTilemap(tilemap`level0`)
        for (let index = 0; index < 2; index++) {
            Powerup12 = sprites.create(img`
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
                `, SpriteKind.Powerup1)
            tiles.placeOnRandomTile(Powerup12, sprites.dungeon.darkGroundCenter)
        }
        for (let index = 0; index < 6; index++) {
            Enemey1 = sprites.create(img`
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
                `, SpriteKind.Enemy)
            tiles.placeOnRandomTile(Enemey1, sprites.dungeon.floorDark5)
            Enemey1.follow(Player1, 50)
        }
        for (let index = 0; index < 4; index++) {
            Ammokasse = sprites.create(img`
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
                `, SpriteKind.Ammo)
            tiles.placeOnRandomTile(Ammokasse, sprites.dungeon.darkGroundCenter)
        }
    } else if (NextLevel == 5) {
        game.splash("Level 5")
        if (randint(1, 3) == 1) {
            tiles.setTilemap(tilemap`level7`)
            info.changeScoreBy(1)
        } else if (randint(1, 3) == 2) {
            tiles.setTilemap(tilemap`level12`)
            info.changeScoreBy(2)
        } else if (randint(1, 3) == 3) {
            tiles.setTilemap(tilemap`level13`)
            info.changeScoreBy(3)
        }
    } else if (NextLevel == 6) {
        game.splash("Bosslevel")
        tiles.setTilemap(tilemap`Boss level`)
        for (let index = 0; index < 7; index++) {
            Ammokasse = sprites.create(img`
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
                `, SpriteKind.Ammo)
            tiles.placeOnRandomTile(Ammokasse, sprites.dungeon.darkGroundCenter)
        }
        Boss2 = sprites.create(img`
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
            `, SpriteKind.Boss)
        Boss2.follow(Player1, 30)
        Boss_statusbar = statusbars.create(25, 4, StatusBarKind.EnemyHealth)
        Boss_statusbar.attachToSprite(Boss2, -25, 0)
        Boss_statusbar.value = 100
        Boss_statusbar.setColor(5, 2)
    } else if (NextLevel == 7 && NextLevel_2 == 3) {
        tiles.setTilemap(tilemap`level10`)
        tiles.placeOnRandomTile(Player1, sprites.dungeon.floorDarkDiamond)
        for (let index = 0; index < 10; index++) {
            Powerup12 = sprites.create(img`
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
                `, SpriteKind.Powerup1)
            tiles.placeOnRandomTile(Powerup12, sprites.dungeon.floorDark2)
        }
    }
    tiles.placeOnRandomTile(Player1, sprites.dungeon.floorDarkDiamond)
}
controller.combos.attachCombo(controller.combos.idToString(controller.combos.ID.up), function () {
    Skudd_rettning = 0
    animation.stopAnimation(animation.AnimationTypes.All, Player1)
    animation.runImageAnimation(
    Player1,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles10, function (sprite, location) {
    music.bigCrash.play()
    game.splash("-1 level")
    NextLevel += -2
    next_level()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Ammo, function (sprite, otherSprite) {
    music.powerUp.play()
    otherSprite.destroy()
    Ammo1 += 40
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava1, function (sprite, location) {
    info.changeLifeBy(-1)
    music.smallCrash.play()
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    music.jumpDown.play()
    sprite.destroy()
    info.changeLifeBy(-1)
})
controller.combos.attachCombo(controller.combos.idToString(controller.combos.ID.right), function () {
    Skudd_rettning = 90
    animation.stopAnimation(animation.AnimationTypes.All, Player1)
    animation.runImageAnimation(
    Player1,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Bossprojectile, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Powerup1, function (sprite, otherSprite) {
    otherSprite.destroy()
    music.baDing.play()
    info.changeLifeBy(1)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairLarge, function (sprite, location) {
    next_level()
})
controller.combos.attachCombo(controller.combos.idToString(controller.combos.ID.left), function () {
    Skudd_rettning = 270
    animation.stopAnimation(animation.AnimationTypes.All, Player1)
    animation.runImageAnimation(
    Player1,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    music.knock.play()
    info.changeScoreBy(1)
    sprite.destroy()
    otherSprite.destroy()
    if (randint(1, 5) == 3) {
        music.baDing.play()
        game.setDialogTextColor(2)
        game.showLongText("Ekstra liv", DialogLayout.Bottom)
        info.changeLifeBy(1)
        Ammo1 += 10
    } else if (randint(1, 5) == 3) {
        music.magicWand.play()
        Speed1 += 20
        game.setDialogTextColor(6)
        game.showLongText("Ekstra fart", DialogLayout.Top)
        Ammo1 += 10
    } else if (randint(1, 5) == 3) {
        game.setDialogTextColor(6)
        game.showLongText("Ekstra ammo", DialogLayout.Center)
        Ammo1 += 40
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite, location) {
    game.over(true)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Bossprojectile, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Boss, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    pause(200)
})
let Life = 0
let BossProjectile: Sprite = null
let Boss_skudd = 0
let Ammokasse: Sprite = null
let Powerup12: Sprite = null
let Enemey1: Sprite = null
let NextLevel_2 = 0
let Boss2: Sprite = null
let Boss_statusbar: StatusBarSprite = null
let projectile: Sprite = null
let Skudd_rettning = 0
let Ammo1 = 0
let Player1: Sprite = null
let NextLevel = 0
NextLevel = 0
let Speed1 = 100
Player1 = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Player1, Speed1, Speed1)
scene.cameraFollowSprite(Player1)
next_level()
info.setLife(3)
info.setScore(0)
Ammo1 = 100
let statusbar = statusbars.create(20, 4, StatusBarKind.Ammo2)
statusbar.max = 100
statusbar.setPosition(113, 5)
statusbar.setColor(7, 2)
statusbar.setLabel("Ammo")
forever(function () {
    if (NextLevel == 1) {
        music.playMelody("E B C5 A B G A F ", 120)
    } else if (NextLevel == 2) {
        music.playMelody("D A B G A F G E ", 120)
    } else if (NextLevel == 3) {
        music.playMelody("C G A F G E F D ", 120)
    } else if (NextLevel == 4) {
        music.playMelody("D A B F A E G D ", 120)
    } else if (NextLevel == 5) {
        music.playMelody("F A A B A G B G ", 120)
    } else if (NextLevel == 6) {
        music.playMelody("E C D C E C C D ", 120)
    } else if (NextLevel == 7) {
        music.playMelody("F G A F G A F G ", 120)
    }
})
forever(function () {
    if (Ammo1 > 100) {
        Ammo1 = 100
    }
})
forever(function () {
    statusbar.value = Ammo1
})
forever(function () {
    Enemey1.follow(Player1, 50)
})
forever(function () {
    tiles.createSpritesOnTiles(sprites.dungeon.floorDark5, SpriteKind.Enemy)
    tiles.replaceAllTiles(sprites.dungeon.floorDark5, sprites.dungeon.darkGroundCenter)
})
forever(function () {
    if (Boss_skudd == 1) {
        BossProjectile = sprites.create(img`
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
            `, SpriteKind.Bossprojectile)
        BossProjectile.follow(Player1, 50)
    }
})
forever(function () {
    if (NextLevel == 6) {
        Enemey1.destroy()
    }
})
forever(function () {
    Life = info.life()
})
forever(function () {
    if (NextLevel == 6) {
        pause(5000)
        Boss_skudd += 1
        pause(20)
        Boss_skudd = 0
    }
})
