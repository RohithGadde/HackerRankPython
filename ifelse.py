#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input())
if (1 <= n) and (n <= 100):
    if n%2 != 0:
        print("Weird")
    elif (2<=n) and (n<=5):
        print("Not Weird") 
    elif (6<=n) and (n<=20):
        print("Weird")
    else:
        print("Not Weird")
