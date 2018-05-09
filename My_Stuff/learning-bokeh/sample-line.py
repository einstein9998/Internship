#!/usr/bin/env python
from bokeh.plotting import figure, output_file, show
import numpy as np

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

output_file("lines.html")

p = figure(title="simple line example", x_axis_label="x",  y_axis_label="y")

p.line(x, y, legend="Temp.", line_width=2)

save(p)