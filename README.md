# AKTA_chromatogram
This is a Python script to help extracting the data from Unicorn file acquired using ÄKTA purifier and reconstruct the chromatogram.

This repository is based in the great [pyCORN](https://github.com/pyahmed/PyCORN) python library.
The pyCORN repository contains an amazing [shiny web app](http://pycornweb.appspot.com).
You can just drag and drop your report.res file from Unicorn software and get your interactive view of chromatogram.
If you want to customize the elements in your chromatogram, then this Repo can help you out in a easy was.

Install the **pyCORN** package.

```python
pip install pycorn
```

Import the module `pc_res3` from **pycorn** to extract the data from the unicorn file and the module `rc` from **matplotlib** to use **LaTex** sythax.
Load the **matplotlib** and **numpy** libraries.

```python
from pycorn import pc_res3
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

# activate latex text rendering
rc('text', usetex=True)
```

Create an object of the class `pc_res3`. The class pc_res3 is used to parse ÄKTA report.res files.

```python
# load the unicorn file from the path
unicorn_file = pc_res3("/AKTA/report.res")

# Parse the file
unicorn_file.load()

# This will show the available data in the file (detectors, etc.)
print(list(unicorn_file.keys()))
```

There are 2 elements in the unicorn_data, the absorbance (mAu) and the elution volume (mL). We will separate them to plot the absorbance against the elution volume.

```python
# data: contains the actual data with x/y-pairs as tuples
unicorn_data = unicorn_file["UV1_280nm"]["data"]
elution = [elem1 for elem1, elem2 in unicorn_data]
absorbance = [elem2 for elem1, elem2 in unicorn_data]

# extract the fraction annotation
fraction_data = unicorn_file["Fractions"]["data"]
fraction_ellution = [elem1 for elem1, elem2 in fraction_data]
fraction = [elem2 for elem1, elem2 in fraction_data]

# remove the last fraction annotation as it has the waste entry
fraction_ellution.pop()
fraction.pop()

# coerse the fraction annotation to integer
fraction = [int(i) for i in fraction]
```

Now we can plot the data using **matplotlib**.

```python
plt.plot(elution, absorbance, linewidth=2.0, color = 'steelblue')
plt.ylabel('Absorbance (mAu)', weight='bold')
plt.xlabel('Elution volume (mL)', weight='bold')
plt.title(r'SEC of $B. jararaca$ venom')
plt.legend(['280 nm'])
plt.style.use('default')
plt.gcf().set_size_inches(10, 5)
plt.savefig('SEC_adult.png', dpi=300)
```

We can also add the fraction annotation to the chromatogram.

```python
plt.plot(elution, absorbance, linewidth=2.0, color = 'steelblue')
plt.ylabel('Absorbance (mAu)', weight='bold')
plt.xlabel('Elution volume (mL)', weight='bold')
plt.title(r'SEC of $B. jararaca$ venom - Adult')
plt.legend(['280 nm'])
plt.style.use('default')
for i in range(len(fraction)):
    plt.text(fraction_ellution[i], fraction[i], str(i+1), fontsize=5, color='red')
plt.gcf().set_size_inches(10, 5)
plt.savefig('SEC_adult_fractions.png', dpi=300)
```
