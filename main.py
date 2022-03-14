start = 0
elapsed = 0
check = 0
def on_button_pressed_a():
    global start
    start = input.running_time()
    while check == 0:
        basic.show_number(Math.idiv(elapsed, 1000))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global elapsed
    global check
    check = 1
    elapsed = input.running_time() - start
    basic.show_number(Math.idiv(elapsed, 1000))
input.on_button_pressed(Button.B, on_button_pressed_b)
