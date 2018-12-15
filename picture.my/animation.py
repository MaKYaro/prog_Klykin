import graphics as gr
from time import sleep

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


def dr_ship(x_coord, y_coord):
        ship = []
        for coord in((x_coord, y_coord), (x_coord + 145, y_coord)), \
                    ((x_coord + 10, y_coord + 18), (x_coord + 135, y_coord + 18)), \
                    ((x_coord + 20, y_coord + 36), (x_coord + 125, y_coord + 36)):
            x = coord[0]
            y = coord[1]
            ship_brown_line = gr.Line(gr.Point(x[0], x[1]), gr.Point(y[0], y[1]))
            ship_brown_line.setWidth(18)
            ship_brown_line.setOutline('brown')
            ship_brown_line.draw(window)
            ship.append(ship_brown_line)

        for coord in ((x_coord + 10, y_coord + 9), (x_coord + 135, y_coord + 9)), \
                     ((x_coord + 10, y_coord + 27), (x_coord + 135, y_coord + 27)):
            x = coord[0]
            y = coord[1]
            ship_black_line = gr.Line(gr.Point(x[0], x[1]), gr.Point(y[0], y[1]))
            ship_black_line.setOutline('black')
            ship_black_line.draw(window)
            ship.append(ship_black_line)

        mast = gr.Line(gr.Point(x_coord + 70, y_coord), gr.Point(x_coord + 70, y_coord - 100))
        mast.setWidth(5)
        mast.setOutline('brown')
        mast.draw(window)
        ship.append(mast)

        for coord in ((x_coord + 72, y_coord - 15), (x_coord + 72, y_coord - 100), (x_coord + 140, y_coord - 15)), \
                     ((x_coord + 68, y_coord - 15), (x_coord + 68, y_coord - 100), (x_coord + 20, y_coord - 15)):
            x = coord[0]
            y = coord[1]
            z = coord[2]

            sail = gr.Polygon(gr.Point(x[0], x[1]), gr.Point(y[0], y[1]), gr.Point(z[0], z[1]))
            sail.setFill('white')
            sail.draw(window)
            ship.append(sail)
        return ship


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


def main():
    dr_sky()
    dr_sea()
    dr_wave()
    dr_cloud()
    a = dr_ship(200, 400)
    for step in range(0, 100, 1):
        for i in a:
            i.move(5, 0)
        sleep(0.1)
    window.getMouse()


main()

