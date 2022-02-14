#ip install benfordslawp
from benfordslaw import benfordslaw
import matplotlib.pyplot as plt
import pandas as pd


# Initialize
bl = benfordslaw(alpha=0.05)

def extracting_data():
    df = pd.read_csv("census_2009b.dms", sep="\t")
    dataset = df['7_2009']
    results = bl.fit(dataset)
    return results

def plotting(extraxcting):
    bl.plot(title='Benford\'s Law Distribution for 7_2009 column')
    plt.plot(bl.results['percentage_emp'][:,0], bl.results['percentage_emp'][:,1], label='Empirical distribution')
    plt.plot(bl.results['percentage_emp'][:,0], bl.leading_digits, label='Benfords Distribution')
    plt.legend()
    plt.grid(True)
    plt.xlabel('Leading digits')
    plt.ylabel('Frequency [%]')
    print(f"P-value = {bl.results['P']}")
    print(f"t-score = {bl.results['t']}")
    plt.savefig('Benfords_Distribution.jpg', dpi=300)


extraxcting = extracting_data()
plotting(extraxcting)
