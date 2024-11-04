import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function to load and preprocess the data
def load_and_preprocess(csv_url):
    """Load dataset and rename columns for easier access."""
    df = pd.read_csv(csv_url)
    df = df.rename(columns={
        'beer_servings': 'beer',
        'spirit_servings': 'spirits',
        'wine_servings': 'wine',
        'total_litres_of_pure_alcohol': 'total_alcohol'
    })
    return df

# Function to calculate basic statistics
def calculate_basic_stats(df):
    return df[['beer', 'spirits', 'wine', 'total_alcohol']].describe()

# Function to get top N countries by total alcohol consumption
def get_top_countries_by_alcohol(df, n=5):
    return df.nlargest(n, 'total_alcohol')[['country', 'total_alcohol']]

# Function to compute correlation matrix
def compute_correlation_matrix(df):
    """Compute correlation matrix between types of alcohol consumption."""
    return df[['beer', 'spirits', 'wine', 'total_alcohol']].corr()

# Function to plot average servings for each type of drink
def plot_average_servings(df):
    avg_servings = df[['beer', 'spirits', 'wine']].mean()
    avg_servings.plot(kind='bar', color=['gold', 'lightblue', 'pink'])
    plt.title("Average Servings of Beer, Spirits, and Wine")
    plt.xlabel("Type of Drink")
    plt.ylabel("Average Servings")
    plt.savefig("average_servings.png", bbox_inches='tight')  
    plt.close()

def plot_top_countries(df):
    top_5 = df.nlargest(5, 'total_alcohol')
    plt.figure(figsize=(5, 6))
    sns.barplot(data=top_5, x='total_alcohol', y='country', 
                palette='viridis', hue= None, legend= False)
    plt.title("Top 5 Countries by Total Alcohol Consumption")
    plt.xlabel("Total Alcohol Consumption (Litres)")
    plt.ylabel("Country")
    plt.savefig("top_countries.png", bbox_inches='tight')  
    plt.close()

def plot_servings_distributions(df):
    plt.figure(figsize=(14, 10))
    sns.histplot(df['beer'], kde=True, color='gold', bins=20)
    plt.title('Distribution of Beer Servings')
    plt.xlabel('Beer Servings')
    plt.ylabel('Frequency')
    plt.savefig("beer_distribution.png")
    plt.close()

    sns.histplot(df['spirits'], kde=True, color='lightblue', bins=20)
    plt.title('Distribution of Spirit Servings')
    plt.xlabel('Spirit Servings')
    plt.ylabel('Frequency')
    plt.savefig("spirit_distribution.png")
    plt.close()

    sns.histplot(df['wine'], kde=True, color='pink', bins=20)
    plt.title('Distribution of Wine Servings')
    plt.xlabel('Wine Servings')
    plt.ylabel('Frequency')
    plt.savefig("wine_distribution.png")
    plt.close()

    sns.histplot(df['total_alcohol'], kde=True, color='purple', bins=20)
    plt.title('Distribution of Total Alcohol Consumption')
    plt.xlabel('Total Litres of Pure Alcohol')
    plt.ylabel('Frequency')
    plt.savefig("total_alcohol_distribution.png")
    plt.close()



# Function to classify countries based on alcohol consumption level
def classify_and_count_categories(df):
    def classify_consumption(total_alcohol):
        if total_alcohol < 3:
            return "Low"
        elif total_alcohol <= 6:
            return "Moderate"
        else:
            return "High"
    
    df['consumption_category'] = df['total_alcohol'].apply(classify_consumption)
    return df
