# Dette programmet tegner sirkler som øker i størrelse i løpet av 3 sekunder.

from ezgraphics import GraphicsWindow
win = GraphicsWindow()
can = win.canvas()

teller = 0
x_pos = 10

#Her inkrementerer jeg stoerrelse med 50, x_pos med 10 og teller med 0.0001.
stoerrelse = 50
while teller < 9:
    can.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    stoerrelse += 50
    x_pos += 10
    teller += 0.0001
