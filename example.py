import pandas_profiling
import pandas as pd
import numpy as np
import datetime

data = {
    'id': [chr(97+c) for c in range(1,10)],
    'x': [50, 50, -10, 0, 0, 5, 15, -3, None],
    'y': [0.000001, 654.152, None, 15.984512, 3122, -3.1415926535, 111, 15.9, 13.5],
    'cat': ['a', 'texto largo de ejemplo', u'Riñón', '', None, 'algo de HTML <b> B.s </div> </div> HTML ','c','c','c'],
    's1': np.ones(9),
    's2': [u'texto constante $ % value {obj} ' for _ in range(1, 10)],
    'somedate': [
        datetime.date(2011, 7, 4), 
        datetime.datetime(2022, 1, 1, 13, 57),
        datetime.datetime(1990, 12, 9), np.nan,
        datetime.datetime(1990, 12, 9), datetime.datetime(1950, 12, 9),
        datetime.datetime(1898, 1, 2), datetime.datetime(1950, 12, 9),
        datetime.datetime(1950, 12, 9)]
    
}
df = pd.DataFrame(data)
df['somedate'] = pd.to_datetime(df['somedate'])
profile = pandas_profiling.ProfileReport(df)
profile.to_file(outputfile="/tmp/myoutputfile2.html")
