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
    wave1 = gr.Line(gr.Point(50, 400), gr.Point(300, 400))
    wave1.setOutline('white')
    wave1.draw(window)

    wave2 = gr.Line(gr.Point(100, 450), gr.Point(150, 450))
    wave2.setOutline('white')
    wave2.draw(window)

    wave3 = gr.Line(gr.Point(300, 300), gr.Point(400, 300))
    wave3.setOutline('white')
    wave3.draw(window)

    wave4 = gr.Line(gr.Point(10, 350), gr.Point(210, 350))
    wave4.setOutline('white')
    wave4.draw(window)

    wave5 = gr.Line(gr.Point(10, 300), gr.Point(110, 300))
    wave5.setOutline('white')
    wave5.draw(window)

    wave6 = gr.Line(gr.Point(200, 450), gr.Point(400, 450))
    wave6.setOutline('white')
    wave6.draw(window)

    wave7 = gr.Line(gr.Point(300, 425), gr.Point(425, 425))
    wave7.setOutline('white')
    wave7.draw(window)

    wave8 = gr.Line(gr.Point(200, 375), gr.Point(450, 375))
    wave8.setOutline('white')
    wave8.draw(window)
def dr_ship_one():
    ship1 = gr.Line(gr.Point(230, 400), gr.Point(375, 400))
    ship1.setWidth(18)
    ship1.setOutline('brown')
    ship1.draw(window)

    ship2 = gr.Line(gr.Point(240, 418), gr.Point(365, 418))
    ship2.setWidth(18)
    ship2.setOutline('brown')
    ship2.draw(window)

    ship3 = gr.Line(gr.Point(240, 409), gr.Point(365, 409))
    ship3.setOutline('black')
    ship3.draw(window)

    ship4 = gr.Line(gr.Point(250, 436), gr.Point(355, 436))
    ship4.setWidth(18)
    ship4.setOutline('brown')
    ship4.draw(window)

    ship5 = gr.Line(gr.Point(240, 427), gr.Point(365, 427))
    ship5.setOutline('black')
    ship5.draw(window)

    ship6 = gr.Line(gr.Point(300, 400), gr.Point(300, 300))
    ship6.setWidth(5)
    ship6.setOutline('brown')
    ship6.draw(window)

    sail = gr.Oval(gr.Point(290, 385), gr.Point(320, 310))
    sail.setFill('white')
    sail.draw(window)
def dr_ship_two():
    ship1 = gr.Line(gr.Point(130, 300), gr.Point(275, 300))
    ship1.setWidth(18)
    ship1.setOutline('brown')
    ship1.draw(window)

    ship2 = gr.Line(gr.Point(140, 318), gr.Point(265, 318))
    ship2.setWidth(18)
    ship2.setOutline('brown')
    ship2.draw(window)

    ship3 = gr.Line(gr.Point(140, 309), gr.Point(265, 309))
    ship3.setOutline('black')
    ship3.draw(window)

    ship4 = gr.Line(gr.Point(150, 336), gr.Point(255, 336))
    ship4.setWidth(18)
    ship4.setOutline('brown')
    ship4.draw(window)

    ship5 = gr.Line(gr.Point(140, 327), gr.Point(265, 327))
    ship5.setOutline('black')
    ship5.draw(window)

    ship6 = gr.Line(gr.Point(200, 300), gr.Point(200, 200))
    ship6.setWidth(5)
    ship6.setOutline('brown')
    ship6.draw(window)

    sail = gr.Oval(gr.Point(190, 285), gr.Point(220, 210))
    sail.setFill('white')
    sail.draw(window)
def dr_cloud1():
    cloud1 = gr.Circle(gr.Point(0, 20), 40)
    cloud1.setFill('white')
    cloud1.draw(window)

    cloud2 = gr.Circle(gr.Point(70, 20), 46)
    cloud2.setFill('white')
    cloud2.draw(window)

    cloud3 = gr.Circle(gr.Point(10, 60), 22)
    cloud3.setFill('white')
    cloud3.draw(window)

    cloud4 = gr.Circle(gr.Point(40, 50), 30)
    cloud4.setFill('white')
    cloud4.draw(window)
def dr_cloud2():
    cloud5 = gr.Circle(gr.Point(500, 50), 60)
    cloud5.setFill('white')
    cloud5.draw(window)

    cloud6 = gr.Circle(gr.Point(450, 20), 30)
    cloud6.setFill('white')
    cloud6.draw(window)
dr_sky()
dr_sea()
dr_wave()
dr_ship_one()
dr_ship_two()
dr_cloud1()
dr_cloud2()

window.getMouse()
