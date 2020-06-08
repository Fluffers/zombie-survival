import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 800   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 600  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN


TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'survivor.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 45, 45)
BARREL_OFFSET = vec(30, 15)

# Weapon settings
BULLET_IMG = 'bullet_s.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 800, 'bullet_lifetime': 600, 'rate': 400, 'kickback': 50, 'spread': 8, 'damage': 40, 'bullet_size': 'large', 'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 600, 'bullet_lifetime': 300, 'rate': 800, 'kickback': 150, 'spread': 20, 'damage': 8, 'bullet_size': 'small', 'bullet_count': 12}

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS = [90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 4000

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png', 'whitePuff18.png', ]
FLASH_DURATION = 40
SPLAT = 'splat red.png'
DAMAGE_ALPHA = [i for i in range(0, 255, 50)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = 'light_350_med.png'

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
BULLET_LAYER = 3
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'
               }
HEALTH_PACK_AMOUNT = 50
BOB_RANGE = 10
BOB_SPEED = 0.4


# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav','zombie-roar-3.wav',
                      'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav']
                }
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'weapon_pickup': 'gun_pickup.wav'
                  }



# 2. DODAĆ 8 LOSOWYCH MIEJSC DO DROPU RZECZY CO FALĘ
# 3. ZMIENIĆ MODEL ZOMBIE NA RAPTORA i wszystkie funkcje z nazwą zombie związane
# 4. POPRAWIĆ HITBOXY W TILED



# ZAPIS GRY PO PRZEGRANEJ - DO PLIKU NAZWA GRACZA - https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame + shelve

# PAUZOWANIE MUZYKI W CZASIE PAUZY
# DODAĆ RIFLE JAKO BROŃ
# ROZWAŻYĆ OPCJĘ DODANIA 2 INNYCH PRZECIWNIKÓW


# PRZYGOTOWAĆ ROZPISKĘ RZECZY KTÓRE MUSIAŁEM ZROBIĆ I CZEGO SIĘ NAUCZYŁEM

# WYRÓWNAĆ NAZWĘ BRONI
# OPCJE - TRYB NOCNY, GŁOŚNOŚĆ POSZCZEGÓLNYCH RZECZY - check!
# 8. ZROBIĆ EKRAN SETTINGS  check!
# 7. ZROBIĆ EKRAN HELP - check
# 5. ZROBIĆ ŁADNE MENU [NAZWA GRY, START, OPCJE, STEROWANIE, WYJŚCIE] - check!
# 6. DODAĆ MOŻLIWOŚĆ ZMIANY BRONI + HUD - check
# 1. DODAĆ FALE - check!
