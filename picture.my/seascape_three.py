import graphics as gr

window = gr.GraphWin("First seascape", 500, 500)


def dr_sky():
    sky = gr.Line(gr.Point(0, 100), gr.Point(500, 100))
    sky.setWidth(300)
    sky.setOutline('grey')
    sky.draw(window)


def dr_sea():
    sea = gr.Line(gr.Point(0, 500), gr.Point(500, 500))
    sea.setWidth(500)
    sea.setOutline('blue')
    sea.draw(window)


def dr_wave():
    for coord in ((50, 400), (300, 400)),\
                 ((100, 450), (150, 450)), \
                 ((300, 300), (400, 300)), \
                 ((10, 350), (210, 350)), \
                 ((10, 300), (110, 300)), \
                 ((200, 450), (400, 450)), \
                 ((300, 425), (425, 425)), \
                 ((200, 375), (450, 375)):

        x = coord[0]
        y = coord[1]
        wave = gr.Line(gr.Point(x[0], x[1]), gr.Point(y[0], y[1]))
        wave.setOutline('white')
        wave.draw(window)


def dr_ship():
    for coord in((230, 400), (375, 400)), \
                ((240, 418), (365, 418)), \
                ((250, 436), (355, 436)):
        x = coord[0]
        y = coord[1]
        ship_brown_line = gr.Line(gr.Point(x[0], x[1]), gr.Point(y[0], y[1]))
        ship_brown_line.setWidth(18)
        ship_brown_line.setOutline('brown')
        ship_brown_line.draw(window)

    for coord in ((240, 409), (365, 409)), \
                 ((240, 427), (365, 427)):
        x = coord[0]
        y = coord[1]
        ship_black_line = gr.Line(gr.Point(x[0], x[1]), gr.Point(y[0], y[1]))
        ship_black_line.setOutline('black')
        ship_black_line.draw(window)

    mast = gr.Line(gr.Point(300, 400), gr.Point(300, 300))
    mast.setWidth(5)
    mast.setOutline('brown')
    mast.draw(window)


def dr_sail():
    for coord in ((302, 385), (302, 300), (370, 385)), \
                 ((298, 385), (298, 300), (250, 385)):
        x = coord[0]
        y = coord[1]
        z = coord[2]

        sail = gr.Polygon(gr.Point(x[0], x[1]), gr.Point(y[0], y[1]), gr.Point(z[0], z[1]))
        sail.setFill('white')
        sail.draw(window)


def dr_cloud():
    for coord in ((0, 20), 40), \
                 ((70, 20), 46), \
                 ((10, 60), 22), \
                 ((40, 50), 30), \
                 ((500, 50), 60), \
                 ((450, 20), 30):

        x = coord[0]
        cloud = gr.Circle(gr.Point(x[0], x[1]), coord[1])
        cloud.setFill('white')
        cloud.setOutline('white')
        cloud.draw(window)


dr_sky()
dr_sea()
dr_wave()
dr_ship()
dr_cloud()
dr_sail()


window.getMouse()
