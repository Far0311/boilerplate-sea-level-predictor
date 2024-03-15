import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    Line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_val1 = np.arrange(df['Year'].min(), 2051, 1) # creates a NumPy array containing a sequence of numbers starting from the minimum value of the 'Year' column in the df and ending at 2050 (since the second argument is exclusive), with a step size of 1.
    y_val1 = x_val1*Line1.slope + Line1.intercept # corresponding y-value based on the slope 

    plt.plot(x_val1, y_val1)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000] #df starting from year 2000

    Line2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_val2 = np.arrange(df_2000['Year'].min(), 2051, 1) # creates a NumPy array containing a sequence of numbers starting from the minimum value of the 'Year' column in the df and ending at 2050 (since the second argument is exclusive), with a step size of 1.
    y_val2 = x_val2*Line2.slope + Line2.intercept # corresponding y-value based on the slope 

    plt.plot(x_val2, y_val2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()