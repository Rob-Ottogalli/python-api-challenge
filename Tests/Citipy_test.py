# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:39:28 2020

@author: Rob-Desktop
"""

import time
from citipy import citipy

city = citipy.nearest_city(40.71, 74.00)

print(city.city_name, city.country_code)

for x in range(0,10):
    print(x)
    time.sleep(1.5)