
# Dataframe from CSV is created from 2014 EPA data. All weights are in millions of tons. 
#Containers and packaging, durable goods, and nondurable goods are the distinct categories of plastic municipal waste. 
# See link for PDF source: https://www.epa.gov/sites/production/files/2016-11/documents/2014_smmfactsheet_508.pdf

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("/Users/Ashley/workspace/plastics/plastics_weights.csv")
df.head()

df['percent_recycled'] = (df['weight_recycled']/df['weight_generated'])*100

df['percent_combusted'] = (df['weight_combusted']/df['weight_generated'])*100

df['percent_landfilled'] = (df['weight_landfilled']/df['weight_generated'])*100

df = df.round(2)
df.head()


df2 = pd.DataFrame(df, columns = ['percent_recycled', 'percent_combusted', 'percent_landfilled'])
df2.plot.bar(figsize=(10,6))
ax = plt.subplot()
ax.set_xticklabels(['Total \n Plastics', 'Containers \n & \n Packaging', 'Durable \n Goods', 'Nondurable \n Goods'], 
            fontsize = 12, rotation = 0)
ax.tick_params(labelsize = 12)
ax.legend(['Recycled', 'Combusted', 'Landfilled'], 
            fontsize = 12, loc='center left', bbox_to_anchor = (1,0.5))
plt.ylim([0,100])
plt.xlabel('Categories', fontsize = 14, fontweight = 'bold')
plt.ylabel('Percent of Municipal Solid Waste', fontsize = 14, fontweight = 'bold')
plt.title('Plastics in Municipal Solid Waste in USA, 2014', fontsize = 16, fontweight = 'bold')
plt.show()