# Customarily, we import and start H2O as follows:
import h2o
h2o.init()  # Will set up H2O cluster using all available cores
# To create an H2OFrame object from a python tuple:
df = h2o.H2OFrame(((1, 2, 3),
                   ('a', 'b', 'c'),
                   (0.1, 0.2, 0.3)))
df
# To create an H2OFrame object from a python list:
df = h2o.H2OFrame([[1, 2, 3],
                   ['a', 'b', 'c'],
                   [0.1, 0.2, 0.3]])
df
# To create an H2OFrame object from a python dict (or collections.OrderedDict):
df = h2o.H2OFrame({'A': [1, 2, 3],
                   'B': ['a', 'b', 'c'],
                   'C': [0.1, 0.2, 0.3]})
df

# To create an H2OFrame object from a dict with specified column types:
df2 = h2o.H2OFrame({'A': [1, 2, 3],
                    'B': ['a', 'a', 'b'],
                    'C': ['hello', 'all', 'world'],
                    'D': ['12MAR2015:11:00:00', '13MAR2015:12:00:00', '14MAR2015:13:00:00']},
                   column_types=['numeric', 'enum', 'string', 'time'])

df2

df2.types

import numpy as np
df = h2o.H2OFrame(np.random.randn(100,4).tolist(), column_names=list('ABCD'))
df.head()
df.tail(5)

df.columns

df.describe()

df['A']

df[1]

df[['B','C']]

df[0:2]

df[2:7, :]

df2[ df2["B"] == "a", :]

df3 = h2o.H2OFrame({'A': [1, 2, 3,None,''],
                    'B': ['a', 'a', 'b', 'NA', 'NA'],
                    'C': ['hello', 'all', 'world', None, None],
                    'D': ['12MAR2015:11:00:00',None,'13MAR2015:12:00:00',None,'14MAR2015:13:00:00']},
                   column_types=['numeric', 'enum', 'string', 'time'])

df3

df3["A"].isna()

df3[ df3["A"].isna(), "A"] = 5
df3

df4 = h2o.H2OFrame({'A': [1, 2, 3,None,''],
                    'B': ['a', 'a', 'b', 'NA', 'NA'],
                    'C': ['hello', 'all', 'world', None, None],
                    'D': ['12MAR2015:11:00:00',None,'13MAR2015:12:00:00',None,'14MAR2015:13:00:00']},
                   column_types=['numeric', 'enum', 'string', 'time'])

df4.mean()

df4["A"].mean()  # check if this behaviour or the one above is a bug

df4["A"].mean(na_rm=True)

df5 = h2o.H2OFrame(np.random.randn(100,4).tolist(), column_names=list('ABCD'))
df5.apply(lambda x: x.mean(na_rm=True))  # TODO na_rm is required

df5.apply(lambda row: sum(row), axis=1)

df6 = h2o.H2OFrame(zip(np.random.randint(0, 7, size=100)))
df6.hist(plot=False)

df7 = h2o.H2OFrame( zip(['Hello', 'World', 'Welcome', 'To', 'H2O', 'World']))
df7
df7.countmatches('l')
df7.sub('o','0')
df7.strsplit('(l)+')

df8 = h2o.H2OFrame(np.random.randn(100,4).tolist(), column_names=list('ABCD'))
df9 = h2o.H2OFrame(np.random.randn(100,4).tolist(), column_names=list('ABCD'))
df8.rbind(df9)
df8.cbind(df9)

df10 = h2o.H2OFrame( { 'A': ['Hello', 'World', 'Welcome', 'To', 'H2O', 'World'],
                       'n': [0,1,2,3,4,5]} )
df11 = h2o.H2OFrame(zip(np.random.randint(0, 10, size=100)), column_names=['n'])
df11.merge(df10)