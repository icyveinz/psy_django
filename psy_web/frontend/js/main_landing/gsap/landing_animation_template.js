function move_from_the_top() {
    return {
        opacity: 0,
        yPercent: -50,
        transform: 'scale(0)'
    }
}

function move_from_the_left() {
    return {
        opacity: 0,
        xPercent: -50,
        transform: 'scale(0)'
    }
}

export {move_from_the_top, move_from_the_left}
