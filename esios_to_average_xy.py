#!/usr/bin/env python3
"""
Grid Simulator
Copyright (C) 2019 Alberto Ruiz <aruiz@gnome.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import sys
from datetime import datetime
from dateutil import parser

rawcurve = json.load(open(sys.argv[1]))

hourysamples = {}
for sample in rawcurve:
    hour = parser.parse(sample["datetime"]).strftime("%H:%M:%S")
    l = hourysamples.get(hour, [])
    l.append(sample["value"])
    hourysamples[hour] = l

dayaverage = { 'x': [], 'y': [] }
for k,v in hourysamples.items():    
    avg = 0
    length = len(v)
    for i in v:
        avg = avg + i/length
    dayaverage["x"].append(k)
    dayaverage["y"].append(avg)

print(json.dumps(dayaverage))