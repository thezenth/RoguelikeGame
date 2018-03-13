import libtcodpy as libtcod

# basic screen parameters
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

# initialize font
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

# ===== Start the Game Console! =====
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/RoguelikeGame', False)
# limit FPS since ours will be realtime
libtcod.sys_set_fps(LIMIT_FPS)

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)
    libtcod.console_flush()
