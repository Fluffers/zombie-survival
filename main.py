import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
from modules import pygame_textinput



class Game:
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 1, 2048)
        # menu option variables
        self.music_volume = 1
        self.night = False

        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    # HUD functions:
    def draw_player_health(self, surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 20
        fill = pct * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        if pct > 0.6:
            col = GREEN
        elif pct > 0.3:
            col = YELLOW
        else:
            col = RED
        pg.draw.rect(surf, col, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 2)

    def draw_text(self, text, font_name, size, color, x, y, align="top-left"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "top-left":
            text_rect.topleft = (x, y)
        if align == "top-right":
            text_rect.topright = (x, y)
        if align == "bottom-left":
            text_rect.bottomleft = (x, y)
        if align == "bottom-right":
            text_rect.bottomright = (x, y)
        if align == "top":
            text_rect.midtop = (x, y)
        if align == "bottom":
            text_rect.midbottom = (x, y)
        if align == "right":
            text_rect.midright = (x, y)
        if align == "left":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_button(self, x, y, width, height, color, thickness=0):
        button = pg.Rect(x - width / 2, y - height / 2, width, height)
        pg.draw.rect(self.screen, color, button, thickness)
        return button

    def show_menu_screen(self):

        self.inMenu = True
        while self.inMenu:
            # catch mouse
            click = False
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = True

            # draw menu
            self.screen.fill(BLACK)
            self.draw_text("DINOSAURVIVAL", self.title_font, 100, WHITE, WIDTH / 2, HEIGHT * 1 / 5,
                           align="center")
            # start
            bt_start = self.draw_button(WIDTH / 2, HEIGHT * 5 / 10, 200, 50, WHITE, 3)
            self.draw_text("Start", self.title_font, 40, WHITE, WIDTH / 2, HEIGHT * 5 / 10,
                           align="center")
            # settings
            bt_settings = self.draw_button(WIDTH / 2, HEIGHT * 6 / 10, 200, 50, WHITE, 3)
            self.draw_text("Settings", self.title_font, 40, WHITE, WIDTH / 2, HEIGHT * 6 / 10,
                           align="center")
            # help
            bt_help = self.draw_button(WIDTH / 2, HEIGHT * 7 / 10, 200, 50, WHITE, 3)
            self.draw_text("Help", self.title_font, 40, WHITE, WIDTH / 2, HEIGHT * 7 / 10,
                           align="center")
            # quit
            bt_quit = self.draw_button(WIDTH / 2, HEIGHT * 8 / 10, 200, 50, WHITE, 3)
            self.draw_text("Quit", self.title_font, 40, WHITE, WIDTH / 2, HEIGHT * 8 / 10,
                           align="center")
            self.draw_text("Jakub Juszczak, 06.2020", self.title_font, 16, WHITE, WIDTH / 2, HEIGHT - 20,
                           align="top")

            # menu interaction
            if bt_start.collidepoint(mouse_pos):
                self.draw_button(WIDTH / 2, HEIGHT * 5 / 10, 200, 50, RED, 3)
                if click:
                    self.inMenu = False
                    self.new()
            elif bt_settings.collidepoint(mouse_pos):
                self.draw_button(WIDTH / 2, HEIGHT * 6 / 10, 200, 50, RED, 3)
                if click:
                    self.show_settings_screen()
            elif bt_help.collidepoint(mouse_pos):
                self.draw_button(WIDTH / 2, HEIGHT * 7 / 10, 200, 50, RED, 3)
                if click:
                    self.show_help_screen()
            elif bt_quit.collidepoint(mouse_pos):
                self.draw_button(WIDTH / 2, HEIGHT * 8 / 10, 200, 50, RED, 3)
                if click:
                    self.quit()

            pg.display.flip()

    def show_end_screen(self):
        # self.screen.fill(BLACK)
        self.draw_text("GAME OVER", self.title_font, 100, WHITE, WIDTH / 2, HEIGHT * 1 / 3, align="center")
        self.draw_text("Press SPACE to start again ", self.title_font, 40, WHITE, WIDTH / 2, HEIGHT * 2 / 3, align="center")
        pg.display.flip()
        self.wait_for_key()
        self.show_menu_screen()

    def show_help_screen(self):
        while True:
            self.screen.fill(BLACK)

            # catch mouse
            click = False
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = True

            # content
            text0 = "Dinosaurvival is a dino survival game."
            self.draw_text(text0, self.hud_font, 40, WHITE, WIDTH / 2, HEIGHT * 10 / 100,
                           align="center")
            text1 = "Your goal is to survive as many waves as possible."
            self.draw_text(text1, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 18 / 100,
                           align="center")
            text2 = "Who would have thought, huh?"
            self.draw_text(text2, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 24 / 100,
                           align="center")
            text3 = "CONTROLS:"
            self.draw_text(text3, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 35 / 100,
                           align="center")
            text4 = "W, S, A, D - movement"
            self.draw_text(text4, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 40 / 100,
                           align="center")
            text5 = "Q - Weapon change"
            self.draw_text(text5, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 45 / 100,
                           align="center")
            text6 = "P - Pause"
            self.draw_text(text6, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 50 / 100,
                           align="center")
            text7 = "MOUSE - Aiming"
            self.draw_text(text7, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 55 / 100,
                           align="center")
            text8 = "LMB - Shooting"
            self.draw_text(text8, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 60 / 100,
                           align="center")
            text9 = "There are healthpacks and stuff, but you'll figure it on the go."
            self.draw_text(text9, self.hud_font, 20, WHITE, WIDTH / 2, HEIGHT * 75 / 100,
                           align="center")


            # quit
            bt_return = self.draw_button(WIDTH / 2, HEIGHT * 9 / 10, 200, 50, WHITE, 3)
            self.draw_text("Return", self.title_font, 40, WHITE, WIDTH / 2, HEIGHT * 9 / 10,
                           align="center")

            # menu interaction
            if bt_return.collidepoint(mouse_pos):
                self.draw_button(WIDTH / 2, HEIGHT * 9 / 10, 200, 50, RED, 3)
                if click:
                    self.show_menu_screen()

            pg.display.flip()

    def show_settings_screen(self):
        color = WHITE

        music_input_box = pg.Rect(WIDTH / 2 - 100, 200, 50, 40)
        night_box = pg.Rect(WIDTH / 2 - 100, 250, 40, 40)

        music_box_active = False
        text = str(int(self.music_volume * 100))
        # volume = int(text)
        while True:
            self.screen.fill(BLACK)
            # catch mouse
            click = False
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = True
                if event.type == pg.KEYDOWN:
                    if music_box_active:
                        if event.key == pg.K_RETURN:
                            music_box_active = False
                            if len(text) == 0:
                                text = '0'
                            volume = int(text)
                            if volume > 100:
                                text = '100'
                                volume = 100
                            self.music_volume = volume / 100
                            # for snd in self.effects_sounds:
                            #     self.effects_sounds[snd].set_volume(0.3 * self.music_volume)
                            # for weapon in self.weapon_sounds:
                            #     for snd in self.weapon_sounds[weapon]:
                            #         snd.set_volume(0.15 * self.music_volume)
                            # for snd in self.zombie_moan_sounds:
                            #     snd.set_volume(0.15 * self.music_volume)
                            # for snd in self.player_hit_sounds:
                            #     snd.set_volume(0.15 * self.music_volume)
                            # for snd in self.zombie_hit_sounds:
                            #     snd.set_volume(0.15 * self.music_volume)
                            # pg.mixer.music.set_volume(self.music_volume)
                            color = RED if music_box_active else WHITE
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        elif len(text) < 3:
                            if event.key in (pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9):
                                text += event.unicode

            # Music volume text
            self.draw_text("Music Volume", self.title_font, 30, WHITE, WIDTH / 2 - 300, 205,
                           align="top-left")
            # Night mode text
            self.draw_text("Night Mode", self.title_font, 30, WHITE, WIDTH / 2 - 300, 255,
                           align="top-left")

            # quit
            bt_return = self.draw_button(WIDTH / 2, HEIGHT * 9 / 10, 200, 50, WHITE, 3)
            self.draw_text("Return", self.title_font, 40, WHITE, WIDTH / 2, HEIGHT * 9 / 10,
                           align="center")

            # menu interaction
            if click:
                if night_box.collidepoint(mouse_pos):
                    if click:
                        self.night = not self.night

                if music_input_box.collidepoint(mouse_pos):
                    music_box_active = True
                    pass
                else:
                    music_box_active = False
                    if len(text) == 0:
                        text = '0'
                    volume = int(text)
                    if volume > 100:
                        text = '100'
                        volume = 100
                    self.music_volume = volume/100
                    # for snd in self.effects_sounds:
                    #     self.effects_sounds[snd].set_volume(0.3 * self.music_volume)
                    # for weapon in self.weapon_sounds:
                    #     for snd in self.weapon_sounds[weapon]:
                    #         snd.set_volume(0.15 * self.music_volume)
                    # for snd in self.zombie_moan_sounds:
                    #     snd.set_volume(0.15 * self.music_volume)
                    # for snd in self.player_hit_sounds:
                    #     snd.set_volume(0.15 * self.music_volume)
                    # for snd in self.zombie_hit_sounds:
                    #     snd.set_volume(0.15 * self.music_volume)
                    pg.mixer.music.set_volume(self.music_volume)
                color = RED if music_box_active else WHITE

            if bt_return.collidepoint(mouse_pos):
                self.draw_button(WIDTH / 2, HEIGHT * 9 / 10, 200, 50, RED, 3)
                if click:
                    self.show_menu_screen()
            # Music volume input
            txt_surface = pg.font.Font(self.hud_font, 25).render(text, True, color)
            self.screen.blit(txt_surface, (music_input_box.x + 5, music_input_box.y + 2))
            pg.draw.rect(self.screen, color, music_input_box, 2)
            # Night mode input
            if self.night:
                txt_surface = pg.font.Font(self.hud_font, 25).render("X", True, WHITE)
                self.screen.blit(txt_surface, (night_box.x + 15, night_box.y + 2))
            pg.draw.rect(self.screen, WHITE, night_box, 2)

            pg.display.flip()

    # Game functions
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        snd_folder = path.join(game_folder, 'snd')
        music_folder = path.join(game_folder, 'music')
        self.map_folder = path.join(game_folder, 'maps')
        self.title_font = path.join(img_folder, 'MachineGunk.ttf')
        self.hud_font = path.join(img_folder, 'Impacted2.0.ttf')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0,0,0,150))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.bullet_images = {}
        self.bullet_images['large'] = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.bullet_images['small'] = pg.transform.scale(self.bullet_images['large'], (10, 10))
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.splat = pg.image.load(path.join(img_folder, SPLAT)).convert_alpha()
        self.splat = pg.transform.scale(self.splat, (64,64))
        self.gun_flashes = []
        for img in MUZZLE_FLASHES:
            self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()
        # lighting effect
        self.fog = pg.Surface((WIDTH, HEIGHT))
        self.fog.fill(NIGHT_COLOR)
        self.light_mask = pg.image.load(path.join(img_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pg.transform.scale(self.light_mask, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()
        # Sound loading
        pg.mixer.music.load(path.join(music_folder, BG_MUSIC))
        self.effects_sounds = {}
        for type in EFFECTS_SOUNDS:
            s = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))
            s.set_volume(0.3 * self.music_volume)
            self.effects_sounds[type] = s
        self.weapon_sounds = {}
        for weapon in WEAPON_SOUNDS:
            self.weapon_sounds[weapon] = []
            for snd in WEAPON_SOUNDS[weapon]:
                s = pg.mixer.Sound(path.join(snd_folder, snd))
                s.set_volume(0.15 * self.music_volume)
                self.weapon_sounds[weapon].append(s)
        self.zombie_moan_sounds = []
        for snd in ZOMBIE_MOAN_SOUNDS:
            s = pg.mixer.Sound(path.join(snd_folder, snd))
            s.set_volume(0.15 * self.music_volume)
            self.zombie_moan_sounds.append(s)
        self.player_hit_sounds = []
        for snd in PLAYER_HIT_SOUNDS:
            s = pg.mixer.Sound(path.join(snd_folder, snd))
            s.set_volume(0.15 * self.music_volume)
            self.player_hit_sounds.append(s)
        self.zombie_hit_sounds = []
        for snd in ZOMBIE_HIT_SOUNDS:
            s = pg.mixer.Sound(path.join(snd_folder, snd))
            s.set_volume(0.15 * self.music_volume)
            self.zombie_hit_sounds.append(s)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, 'level1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            # if tile_object.name == 'mob':
            #     Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                self.player = Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name in ['health', 'shotgun']:
                Item(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
        self.paused = False
        self.wave = 0
        self.effects_sounds['level_start'].play()
        self.run()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x
            self.events()
            if not self.paused:
                self.update()
            self.draw()
        g.show_end_screen()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        # game over condition
        if len(self.mobs) == 0:
            self.wave += 1
            self.next_wave(self.wave)
        # player hits items
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'health' and self.player. health < PLAYER_HEALTH:
                hit.kill()
                self.effects_sounds['health_up'].play()
                self.player.add_health(HEALTH_PACK_AMOUNT)
            if hit.type == 'shotgun':
                hit.kill()
                self.effects_sounds['weapon_pickup'].play()
                self.player.weapons.append('shotgun')
                self.player.weapon = 'shotgun'
        # mobs hit player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            if random() < 0.5:
                choice(self.player_hit_sounds).play()
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.hit()
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # bullets hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for mob in hits:
            #hit.health -= WEAPONS[self.player.weapon]['damage'] * len(hits[hit])
            for bullet in hits[mob]:
                mob.health -= bullet.damage
            mob.vel = vec(0, 0)

    def render_fog(self):
        # draw the light mask onto fog
        self.fog.fill(NIGHT_COLOR)
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.fog, (0, 0), special_flags=pg.BLEND_MULT)

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                if isinstance(sprite, Mob) or isinstance(sprite, Player):
                    pg.draw.rect(self.screen, RED, self.camera.apply_rect(sprite.hit_rect), 1)
        if  self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, RED, self.camera.apply_rect(wall.rect), 1)
            for mob in self.mobs:
                pg.draw.line(self.screen, BLUE, self.player.pos_rel, mob.pos-self.player.pos+(WIDTH/2, HEIGHT/2))
        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        if self.night:
            self.render_fog()
        # HUD functions
        if self.playing:
            self.draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
            self.draw_text('Enemies left: {}'.format(len(self.mobs)), self.hud_font, 16, WHITE, WIDTH - 10, 8,
                           align="top-right")
            self.draw_text('WAVE: {}'.format(self.wave), self.hud_font, 16, WHITE, WIDTH / 2, 8,
                           align="top")
            self.draw_text('WEAPON: {}'.format(self.player.weapon), self.hud_font, 16, WHITE, 10, 32,
                           align="top-left")

            if self.paused:
                self.screen.blit(self.dim_screen, (0, 0))
                self.draw_text("Paused", self.title_font, 105, WHITE, WIDTH / 2, HEIGHT / 2, align="center")

        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pg.K_p:
                    self.paused = not self.paused
                if event.key == pg.K_n:
                    self.night = not self.night
                # player settings for keydown
                if event.key == pg.K_q:
                    current = self.player.weapons.index(self.player.weapon) + 1
                    if current == len(self.player.weapons):
                        current = 0
                    self.player.weapon = self.player.weapons[current]

    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                elif event.type == pg.KEYUP and event.key == pg.K_SPACE:
                    waiting = False

    def next_wave(self, number):
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height / 2)
            if tile_object.name == 'mob':
                for i in range(0, number):
                    Mob(self, obj_center.x+number-1, obj_center.y+number-1)


# create the game object
g = Game()
pg.mixer.music.play(loops=-1)
g.show_menu_screen()
