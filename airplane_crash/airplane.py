import re
import pandas as pd

# import numpy as np

'''
extract manufacturer data from the aircraft
'''
Data = pd.read_csv("PlaneCrashes.csv")

# np.random.seed(42)
obs, feat = Data.shape
Data.sample(5)

# define pattern to take first word (two, if shorter than 4)
p = re.compile('^[A-Z]{2,3}[ ]?[A-Z-]+', re.I)


def get_manufacturer(aircraft_name):
    s = re.search(p, aircraft_name)
    return None if s is None else s.group(0).upper()


# sample = Data.sample(5)
# sample["Manufacturer"] = sample['Aircraft'].apply(lambda x: get_manufacturer(str(x)))
# print(sample)
Data["Manufacturer"] = Data['Aircraft'].apply(lambda x: get_manufacturer(str(x)))
print(Data)

Data.to_csv("PlaneCrashesUpdate.csv")