import numpy
import pandas as pd
import scipy
from scipy import sparse

data = numpy.load('../npz/plik1.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])

sparsed_data = scipy.sparse.load_npz('../npz/plik1.npz')
df = pd.DataFrame.sparse.from_spmatrix(sparsed_data)
print(df)

# df = pd.DataFrame.from_dict({item: data[item] for item in data.files}, orient='index')
# dd = pd.DataFrame.from_dict({item: [data[item]] for item in data.files}, orient='index')
# print(dd.head())

