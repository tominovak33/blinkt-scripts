no_blinkt = False
try:
    from blinkt import set_pixel, show
except ImportError:
    no_blinkt = True
    pass


def set_led(led_number, r, g, b, brightness=1):
    if no_blinkt:
        return

    set_pixel(int(led_number), r, g, b, brightness)


def apply_changes():
    if no_blinkt:
        return
    show()
    show()
