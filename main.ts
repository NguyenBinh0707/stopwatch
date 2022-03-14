let start = 0
let check = 0
let elapsed = 0
input.onButtonPressed(Button.A, function () {
    start = input.runningTime()
    while (check == 0) {
        elapsed = input.runningTime() - start
        basic.showNumber(Math.idiv(elapsed, 1000))
    }
})
input.onButtonPressed(Button.B, function () {
    check = 1
    basic.showNumber(Math.idiv(elapsed, 1000))
    start = 0
    elapsed = 0
    check = 0
})
