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
    line_coords_list = [gr.Point(50, 400), gr.Point(300, 400),
                        gr.Point(100, 450), gr.Point(150, 450),
                        gr.Point(300, 300), gr.Point(400, 300),
                        gr.Point(10, 350), gr.Point(210, 350),
                        gr.Point(10, 300), gr.Point(110, 300),
                        gr.Point(200, 450), gr.Point(400, 450),
                        gr.Point(300, 425), gr.Point(425, 425),
                        gr.Point(200, 375), gr.Point(450, 375)]

    while len(line_coords_list) != 0:

        wave = gr.Line(line_coords_list.pop(0), line_coords_list.pop(0))
        wave.setOutline('white')
        wave.draw(window)


def dr_ship():
    list_brown_boards_coords = [gr.Point(230, 400), gr.Point(375, 400),
                                gr.Point(240, 418), gr.Point(365, 418),
                                gr.Point(250, 436), gr.Point(355, 436)]
    list_black_lines_coords = [gr.Point(240, 409), gr.Point(365, 409),
                               gr.Point(240, 427), gr.Point(365, 427)]
    while len(list_brown_boards_coords) != 0:
        ship_brown_line = gr.Line(list_brown_boards_coords.pop(0), list_brown_boards_coords.pop(0))
        ship_brown_line.setWidth(18)
        ship_brown_line.setOutline('brown')
        ship_brown_line.draw(window)

    while len(list_black_lines_coords) != 0:
        ship_black_line = gr.Line(list_black_lines_coords.pop(0), list_black_lines_coords.pop(0))
        ship_black_line.setOutline('black')
        ship_black_line.draw(window)

    mast = gr.Line(gr.Point(300, 400), gr.Point(300, 300))
    mast.setWidth(5)
    mast.setOutline('brown')
    mast.draw(window)

    sail = gr.Oval(gr.Point(290, 385), gr.Point(320, 310))
    sail.setFill('white')
    sail.draw(window)


def dr_cloud1():
    list_cloud_coords = [gr.Point(0, 20), 40,
                         gr.Point(70, 20), 46,
                         gr.Point(10, 60), 22,
                         gr.Point(40, 50), 30,
                         gr.Point(500, 50), 60,
                         gr.Point(450, 20), 30]
    while len(list_cloud_coords) != 0:
        cloud = gr.Circle(list_cloud_coords.pop(0), list_cloud_coords.pop(0))
        cloud.setFill('white')
        cloud.draw(window)


dr_sky()
dr_sea()
dr_wave()
dr_ship()
dr_cloud()


window.getMouse()
