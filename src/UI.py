import lvgl as lv
import utime
import usys
from usr import lcd

year, month, day, hour, minute, second = utime.localtime()[0:6]

def anim_x_cb(obj, v):
    obj.set_x(v)

def anim_y_cb(obj, v):
    obj.set_y(v)

def anim_width_cb(obj, v):
    obj.set_width(v)

def anim_height_cb(obj, v):
    obj.set_height(v)

def anim_img_zoom_cb(obj, v):
    obj.set_zoom(v)

def anim_img_rotate_cb(obj, v):
    obj.set_angle(v)

global_font_cache = {}
def test_font(font_family, font_size):
    global global_font_cache
    if font_family + str(font_size) in global_font_cache:
        return global_font_cache[font_family + str(font_size)]
    if font_size % 2:
        candidates = [
            (font_family, font_size),
            (font_family, font_size-font_size%2),
            (font_family, font_size+font_size%2),
            ("montserrat", font_size-font_size%2),
            ("montserrat", font_size+font_size%2),
            ("montserrat", 16)
        ]
    else:
        candidates = [
            (font_family, font_size),
            ("montserrat", font_size),
            ("montserrat", 16)
        ]
    for (family, size) in candidates:
        try:
            if eval('lv.font_{}_{}'.format(family, size)):
                global_font_cache[font_family + str(font_size)] = eval('lv.font_{}_{}'.format(family, size))
                if family != font_family or size != font_size:
                    print('WARNING: lv.font_{}_{} is used!'.format(family,size))
                return eval('lv.font_{}_{}'.format(family,size))
        except AttributeError:
            try:
                load_font = lv.font_load("U:/media/lv_font_{}_{}.fnt".format(family, size))
                global_font_cache[font_family + str(font_size)] = load_font
                return load_font
            except:
                if family == font_family and size == font_size:
                    print('WARNING: lv.font_{}_{} is NOT supported!'.format(family, size))


# Create screen
screen = lv.obj()
screen.set_size(240, 320)
screen.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen.set_style_bg_grad_dir(lv.GRAD_DIR.NONE, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_top_date
screen_top_date = lv.label(screen)
screen_top_date.set_text("{}/{}/{}".format(year, month, day))
screen_top_date.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
screen_top_date.add_flag(lv.obj.FLAG.CLICKABLE)
screen_top_date_calendar = None
screen_top_date.set_pos(45, 21)
screen_top_date.set_size(157, 31)
# Set style for screen_top_date, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_top_date.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_text_font(test_font("Alatsi_Regular", 22), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_text_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_bg_grad_dir(lv.GRAD_DIR.NONE, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_pad_top(7, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_shadow_width(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_shadow_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_shadow_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_shadow_spread(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_shadow_ofs_x(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_top_date.set_style_shadow_ofs_y(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# # Create tired_happy
# screen_tired = lv.img(screen)
# screen_tired.set_pos(44, 100)
# screen_tired.set_size(152, 152)
# screen_tired.set_src("U:/media/tired.png")

# Create screen_happy
screen_gif = lv.gif(screen)
screen_gif.set_src("U:/media/happy_min.gif")
screen_gif.set_pos(44, 100)
screen_gif.set_size(152, 152)

# Update the emoji
def update_emoji(emoji_name):

    if emoji_name == "happy":
        screen_gif.set_src("U:/media/happy_min.gif")
    if emoji_name == "cool":
        screen_gif.set_src("U:/media/cool_min.gif")
    if emoji_name == "think":
        screen_gif.set_src("U:/media/think_min.gif")
    if emoji_name == "angry":
        screen_gif.set_src("U:/media/angry_min.gif")

    #screen_gif.refr_size()

# Load the default screen
lv.scr_load(screen)

