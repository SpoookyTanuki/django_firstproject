from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)

import os
workdir = "/Users/elenapalenova/Desktop/パイソン paison/homeworks/block_4_django/dj-homeworks/first-project"
dirs = os.listdir(workdir)

for file in dirs:
    print(file)