from ezgraphics import GraphicsWindow
win = GraphicsWindow()
canvas = win.canvas()

canvas.drawOval(100, 40, 200, 150)
canvas.drawOval(100, 175, 200, 150)
canvas.drawOval(75, 100, 75, 50)
canvas.drawOval(250, 100, 75, 50)

win.wait()
