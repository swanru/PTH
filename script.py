import os
import argparse
from time import time
import pandas as pd
var_array = [i for i in range(101)]
# TODO: Silakan buat kode Anda di bawah ini.
result = 0
for i in range(len(var_array)):
	result += var_array[i]
rata2 = result/(len(var_array))
print(rata2)