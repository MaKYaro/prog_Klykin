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
def dr_ship(L: float):
    ship1 = gr.Line(gr.Point(130+L, 300+L), gr.Point(275+L, 300+L))
    ship1.setWidth(18)
    ship1.setOutline('brown')
    ship1.draw(window)

    ship2 = gr.Line(gr.Point(140+L, 318+L), gr.Point(265+L, 318+L))
    ship2.setWidth(18)
    ship2.setOutline('brown')
    ship2.draw(window)

    ship3 = gr.Line(gr.Point(140+L, 309+L), gr.Point(265+L, 309+L))
    ship3.setOutline('black')
    ship3.draw(window)

    ship4 = gr.Line(gr.Point(150+L, 336+L), gr.Point(255+L, 336+L))
    ship4.setWidth(18)
    ship4.setOutline('brown')
    ship4.draw(window)

    ship5 = gr.Line(gr.Point(140+L, 327+L), gr.Point(265+L, 327+L))
    ship5.setOutline('black')
    ship5.draw(window)

    ship6 = gr.Line(gr.Point(200+L, 300+L), gr.Point(200+L, 200+L))
    ship6.setWidth(5)
    ship6.setOutline('brown')
    ship6.draw(window)

    sail = gr.Oval(gr.Point(190+L, 285+L), gr.Point(220+L, 210+L))
    sail.setFill('white')
    sail.draw(window)
def dr_cloud1(N: float):
    cloud1 = gr.Circle(gr.Point(0+N, 20), 40)
    cloud1.setFill('white')
    cloud1.draw(window)

    cloud2 = gr.Circle(gr.Point(70+N, 20), 46)
    cloud2.setFill('white')
    cloud2.draw(window)

    cloud3 = gr.Circle(gr.Point(10+N, 60), 22)
    cloud3.setFill('white')
    cloud3.draw(window)

    cloud4 = gr.Circle(gr.Point(40+N, 50), 30)
    cloud4.setFill('white')
    cloud4.draw(window)
def dr_cloud2(M: float):
    cloud5 = gr.Circle(gr.Point(500-M, 50), 60)
    cloud5.setFill('white')
    cloud5.draw(window)

    cloud6 = gr.Circle(gr.Point(450-M, 20), 30)
    cloud6.setFill('white')
    cloud6.draw(window)
dr_sky()
dr_sea()
dr_wave()
L=int(input("Enter ship's coordinate:"))
dr_ship(L)
L=int(input("Enter ship's coordinate:"))
dr_ship(L)
N=int(input("Enter cloud's coordinate:"))
dr_cloud1(N)
M=int(input("Enter cloud's coordinate:"))
dr_cloud2(M)
N=int(input("Enter cloud's coordinate:"))
dr_cloud1(N)
M=int(input("Enter cloud's coordinate:"))
dr_cloud2(M)



window.getMouse()
