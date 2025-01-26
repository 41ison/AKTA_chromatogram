# Python script to extract data from Unicorn file - ÄKTA
# author: Alison FA Chaves

# Install the pycorn package and import the module.

pip install pycorn
from pycorn import pc_res3
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

# activate latex text rendering
rc('text', usetex=True)

#Create an object of the class pc_res3. The class pc_res3 is used to parse ÄKTA res files.

# load the unicorn file from the path
# you need to change the path to the location of your file
unicorn_file = pc_res3("/AKTA/report.res")

# Parse the file
unicorn_file.load()

# This will show the available data in the file (detectors, etc.)
print(list(unicorn_file.keys()))

#There are 2 elements in the unicorn_data, the absorbance (mAu) and the elution volume (mL). We will separate them to plot the absorbance against the elution volume.

# data: contains the actual data with x/y-pairs as tuples
unicorn_data = unicorn_file["UV1_280nm"]["data"]
elution = [elem1 for elem1, elem2 in unicorn_data]
absorbance = [elem2 for elem1, elem2 in unicorn_data]
# fraction annotation
fraction_data = unicorn_file["Fractions"]["data"]
fraction_ellution = [elem1 for elem1, elem2 in fraction_data]
fraction = [elem2 for elem1, elem2 in fraction_data]
# remove the last fraction annotation
fraction_ellution.pop()
fraction.pop()
# coerse the fraction annotation to integer
fraction = [int(i) for i in fraction]

# Now we can plot the data using matplotlib.

# Plot the data using matplotlib
plt.plot(elution, absorbance, linewidth=2.0, color = 'steelblue')
plt.ylabel('Absorbance (mAu)', weight='bold')
plt.xlabel('Elution volume (mL)', weight='bold')
plt.title(r'SEC of $B. jararaca$ venom')
plt.legend(['280 nm'])
plt.style.use('default')
plt.gcf().set_size_inches(10, 5)
#plt.show()

plt.savefig('SEC_plot.png', dpi=300)

# We can also add the fraction annotation to the chromatogram.

# plot the fraction annotation in the chromatogram
plt.plot(elution, absorbance, linewidth=2.0, color = 'steelblue')
plt.ylabel('Absorbance (mAu)', weight='bold')
plt.xlabel('Elution volume (mL)', weight='bold')
plt.title(r'SEC of $B. jararaca$ venom - Adult')
plt.legend(['280 nm'])
plt.style.use('default')
for i in range(len(fraction)):
    plt.text(fraction_ellution[i], fraction[i], str(i+1), fontsize=5, color='red')
plt.gcf().set_size_inches(10, 5)
plt.savefig('SEC_plot_fractions.png', dpi=300)
