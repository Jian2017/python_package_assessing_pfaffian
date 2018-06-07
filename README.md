# (1) python_package_assessing_pfaffian (PPAP)
PPAP is a python package to evalute the [pfaffian](https://en.wikipedia.org/wiki/Pfaffian) of even by even dimensional skew-symmetric matrix.
<img src="https://hashtagbay.com/wp-content/uploads/product/1758/1480201210.png" alt="drawing" width="200px"/>

For example, apply Wick's theorem to four fermions average, we can calculate it from two fermions average:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b81699c87476cad783fefde4d3c775827b1e2760" alt="drawing" width="200px"/>


# (2) how to use
very simple, download the package to your fold, and run this code
```{python}
import numpy as np
from pf import pf

N=20
X=np.random.random((2*N,2*N))
S=X.transpose()-X

pf(S)  # evaluting the pfaffian of matrix S
```

# (3) benchmarking


