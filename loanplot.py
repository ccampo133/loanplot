import os
from datetime import datetime

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import numpy as np


def loadcsv(filename):
    to_date = lambda x: datetime.strptime(x, '%m/%d/%Y')
    return np.genfromtxt(filename, delimiter=',', names=True, dtype=None, converters={'date': to_date})


data = np.array([loadcsv('data/' + filename) for filename in os.listdir('data') if filename.endswith('.csv')])

dates = np.array([])
amounts = np.array([])
principal = np.array([])
interest = np.array([])

for row in data:
    dates = np.concatenate([dates, row['date']])
    amounts = np.concatenate([amounts, row['amount']])
    principal = np.concatenate([principal, row['principal']])
    interest = np.concatenate([interest, row['interest']])

isorted = np.argsort(dates)
cumulative_amts = np.cumsum(amounts[isorted])
cumulative_princ = np.cumsum(principal[isorted])
cumulative_int = np.cumsum(interest[isorted])
unpaid = cumulative_princ[-1] - cumulative_princ

plt.stackplot(dates[isorted], cumulative_int, cumulative_princ, colors=['#377EB8', '#55BA87'])
plt.ylim(0, np.max(cumulative_amts) + 0.05 * np.max(cumulative_amts))

# Create the legend manually
plt.legend(
    [mpatches.Patch(color='red'), mpatches.Patch(color='#55BA87'), mpatches.Patch(color='#377EB8')],
    ['Unpaid Principal', 'Principal', 'Interest'],
    loc=0,
    fontsize='small'
)

plt.plot(dates[isorted], unpaid, 'r--')

# Set up axes
y_format = tkr.FuncFormatter(lambda val, pos: '${0:,.2f}'.format(val))
ax = plt.gca()
ax.yaxis.set_major_formatter(y_format)
plt.grid(alpha=0.3)
plt.rc('xtick', labelsize=8)

plt.savefig('loans.png', dpi=300, bbox_inches='tight')
