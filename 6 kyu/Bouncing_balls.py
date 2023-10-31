def bouncing_ball(h, bounce, window):
    times = 1
    if h > 0 and 0 < bounce < 1 and window < h:
        run = True
    else:
        return -1
    while run:
        h *= bounce
        if window < h:
            times += 2
        else:
            run = False
    return times