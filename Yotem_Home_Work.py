# import psychrolib as ps
import pandas as pd
import numpy as np

# ps.SetUnitSystem(ps.SI)
# Constants

df = pd.read_csv(r'C:\Google One\Work\Urecsys\Energy_Calculator\vitania')



# Outdoor conditions

# Process
Outdoor_temp = 30  # °C
Outdoor_RH = 70  # %
Indoor_set_temp: 17  # °C
# System
Flow_rate = 25000  # cfm
Chillers_COP = 3
