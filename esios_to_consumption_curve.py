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

rawcurve = json.load(open(sys.argv[1]))

initialdate = rawcurve[0]["datetime"]
hourysamples = [sample["value"] for sample in rawcurve]



print(json.dumps({"samples": hourysamples, "start": initialdate}))