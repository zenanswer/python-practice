#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# Create the watermark from an image
c = canvas.Canvas('watermark.pdf')
c = canvas.Canvas("form.pdf", pagesize=(1024,768))
c.setLineWidth(.4)
c.setFont('Helvetica', 28)


# Draw the image at x, y. I positioned the x,y to be where i like here
# c.drawImage('test.png', 15, 720)

# Add some custom text for good measure
c.saveState()
#c.translate(3.5*cm, 15.5*cm)
#c.rotate(45)
c.setFillColorRGB(106/256, 106/256, 106/256)
c.rotate(45)
c.drawString(600, -100,"Created by Wang Xuechen")
c.restoreState()
c.save()

