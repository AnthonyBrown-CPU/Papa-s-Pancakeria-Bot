class GUISum:
    flipline_logo = 34737,
    continue1 = 25562,
    menu_btn = 12564,
    play_button = 20262,
    
    sound_active = 6021,
    sound_muted = 3414,
    
    load_loading = 140,
    load_continue = 5243,
    
    empty_slot = 7790,
    closed_sign = 4322,
    pancake_tray = 1514,

    dayStart_tutorial = 26008,
    drinks_tutorial = 3627,   
    
    order_floor = 1444,
    store_floor = 3928

class Coor:
    # Set to the top left pixel of the game window. 
    # Firefox browser with bookmark tab, scrolled to the top.
    
    # Kongregate
    #X_PAD = 20
    #Y_PAD = 347
    
    # Flipline
    X_PAD = 28
    Y_PAD = 353
    
    X_LIMIT = X_PAD + 640
    Y_LIMIT = Y_PAD + 480
    
    preload_continue = (565, 458)
    
    mm_play = (347, 351)
    mm_sound = (621, 362)
    
    mm_slot = {
        '1' : (129, 334),
        '2' : (319, 334),
        '3' : (513, 334)
    }
    
    mm_delete_slot = {
        '1' : (202, 76),
        '2' : (394, 76),
        '3' : (585, 76)
    }
    
    mm_erasegmcnfm = {
        '1' : (130, 250),
        '2' : (320, 250),
        '3' : (510, 250)
    }
    
    mm_resume_save = (305, 435)
    
    char_male = (215, 330)
    char_female = (414, 330)
    char_nameField = (313, 269)
    char_continue = (400, 315)
    
    intro_skip = (570, 445)
    
    s_order = (160, 455)
    s_grill = (265, 455)
    s_build = (380, 455)
    s_drink = (480, 450)
    
    take_order = (150, 145)
    
    line_active = (560, 20)
    line_first_slot = (20, 10)
    line_spacing = 37

    #Grill Station controls
    gril_cancel = (60, 385)
    gril_confirm = (565, 390)
    
    #Grill Station grills
    grill = {
        0:(65, 205),
        1:(185, 205),
        2:(305, 205),
        3:(425, 205),
        4:(65, 290),
        5:(185, 290),
        6:(305, 290),
        7:(425, 290)
    }
        
    iron = {
        0:(65, 115),
        1:(185, 115),
        2:(305, 115),
        3:(430, 115)
    }
    
    drink_rack = [
        (70, 140),
        (140, 140),
        (210, 140),
        (280, 140),
        (350, 140),
        (420, 140)
    ]
    
    d_pour_btn = (240, 130)
    d_my_drinks = (565, 355)
    
    d_flav = {
        'tea': (40, 130),
        'orange': (85, 130),
        'coffee': (135, 130),
        'decaf': (345, 130),
        'cranberry': (395, 130),
        'milk': (440, 130)
    }
    
    d_size = {
        'small': (120, 330),
        'large': (370, 330)
    }
    
    d_add = {
        'ice': (55, 180),
        'sugar': (120, 180),
        'milk': (355, 180),
        'cocoa': (425, 180)
    }

    #Build station controls
    build_base = (74, 345)
    build_center = (310, 225)   
    build_tray = (170, 335)
    build_finish = (595, 395)
    
    #Day complete
    daycom_continue1 = (310, 445)
    daycom_skipslots = (254, 364)
    daycom_continue2 = (313, 450)
    daycom_continue3 = (570, 460)
    
class Area:
    #Places which need Screengrab for the bot to see
    mm_sound = (620, 358, 9, 9)
    mm_play = (278, 338, 56, 28)
    
    #Save Slot delete button
    mm_delete_slot = {
        '1':(184, 61, 29, 21),
        '2':(376, 61, 29, 21),
        '3':(568, 61, 29, 21)
    }
    
    #Menu button in lower left when main game is running. Used as confirmation that a cut-scene has finished
    menu_btn = (17, 451, 41, 12)
    
    #Area of floor where new customers feet will be. Used to detect customers waiting for you to take their order
    order_floor = (120, 365, 20, 30) 
    
    # Used to detect approaching customers
    store_floor = (111, 343, 528, 4)
    
    #Used to detect when customers have finished reviewing their pancake.
    pancake_tray = (300, 350, 20, 20)
    
    #Used to detect the end of the day
    flipline_logo = (14, 434, 78, 34)
    
    #Used to detect when day summary has finished
    continue1 = (245, 434, 121, 28)
    
    #Day Number, visible during store opening
    day_number = (300, 445, 37, 23)
    
    #Day Title, accompanies day number, used to check when day number is fully visible
    day_title = (284, 418, 66, 4)
    
    # Used to detect when a customer has finished ordering
    order_wait = (540, 360, 60, 30)
    
    # User to detect if the store is closed.
    store_sign = (527, 355, 18, 41)
    
    #Continue Area on game load, used to detect when the game is finished loading
    load_continue = (550, 440, 4, 35)
    load_screen = (480, 440, 4, 35)
    
    # Order ticket box, and spacing between them
    ticket_section = (513, 267, 45, 10)
    ticket_toppingNum = (562, 267, 45, 10)
    ticket_spacing = 30
    
    t_d_flavour = (508, 42, 32, 30)
    t_d_size = (549, 53, 18, 13)
    t_d_additional = (580, 43, 32, 30) 
    
    # On the first day drinks are introduced, the games forces you
    # to press the 'MY DRINKS' button, disabling every other button
    # A check for the tutorial speechbubble solves this.
    drink_check = (185, 230, 72, 20)
    
IngredientTypes = {
    # Itemname : ItemType, (CoorX, CoorY), TimeToApply
    #Time it takes to apply = more points on circle

    'pancake':              ['bread', (256, 384)],
    'french':               ['bread', (357, 376)],
    'waffle':               ['waffle', (256, 384)],
    
    #Bacon. What? Who puts bacon in their pancakes?
    'bacon_pancake':        ['combo','pancake','bacon_mix'],
    'bacon_french':         ['combo','french','bacon_mix'],
    'bacon_waffle':         ['combo','waffle','bacon_mix'],
    
    'blueberry_mix':        ['mix', (435, 395)],
    'chocolate_mix':        ['mix', (180, 398)],
    'pecan_mix':            ['mix', (462, 355)],
    'bacon_mix':            ['mix', (149, 355)],
    
    'butterpad':            ['piece', (445, 235)],
    'banana':               ['piece', (445, 315)],
    'strawberry':           ['piece', (445, 275)],
    
    'blueberry':            ['sprinkle', (175, 235), 2],
    'choc_chip':            ['sprinkle', (172, 283), 6],
    'raspberry':            ['sprinkle', (177, 326), 2.2],
    'cinnamon':             ['sprinkle', (441, 192), 4.5],
    'sugar':                ['sprinkle', (175, 198), 4.5],
    
    'blueberry_sauce':      ['sauce', (155, 140), 4],
    'hot_sauce':            ['sauce', (420, 140), 4],
    'whipped_cream':        ['sauce', (195, 133), 3.5],
    'honey':                ['sauce', (467, 133), 4],
    
    # Bread COMBOS
    # combo_name : ItemType, Bread, Mixin
    
    'blueberry_pancake':['combo', 'pancake', 'blueberry_mix'],
    'blueberry_french': ['combo', 'french', 'blueberry_mix'],
    'blueberry_waffle': ['combo', 'waffle', 'blueberry_mix'],
        
    'chocolate_pancake':['combo', 'pancake', 'chocolate_mix'],
    'chocolate_french': ['combo', 'french', 'chocolate_mix'],
    'chocolate_waffle': ['combo', 'waffle', 'chocolate_mix'],
    
    'pecan_pancake':    ['combo','pancake','pecan_mix'],
    'pecan_french':     ['combo','french','pecan_mix'],
    'pecan_waffle':     ['combo','waffle','pecan_mix']
    
}

