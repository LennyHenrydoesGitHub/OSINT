# If you don't have pandas or plotly installed
# Install pip
# Install plotly and pandas with pip

import pandas as pd
import plotly.express as px

#Enter filepath from your local machine to make script work
filepath = '/Users/smaranda/Documents/Data_Science/SPIRI_scripts_and_csv_files/Military_spending_all_world/Share_of_Gov_spending.csv'
df = pd.read_csv(filepath, encoding='latin1')

Regions = ["Africa", "Americas", "Asia & Oceania", "Europe", "Middle East"]
Sub_regions = ["North Africa", "sub-Saharan Africa", "Central America and the Caribbean", 
               "North America", "South America", "South Asia", "East Asia", "South East Asia", 
               "Central Europe", "Eastern Europe", "Western Europe"]

def show_info(df):
    print("==============Shape==============")
    print(df.shape)
    print("==============Info==============")
    print(df.info())
    print("==============Columns==============")
    print(df.columns)
    print("==============Data Frame==============")
    print(df)

#Usage -- Uncomment lines below
#show_info(df)

def show_percentage_of_gov_spending_by_year(year):
    fig = px.scatter(df, y=str(year), x="Country", title='Military expenditure by country as percentage of government spending, 1949-2022', color = 'Country')
    fig.show()

#Usage -- Uncomment lines below
#show_percentage_of_gov_spending_by_year(2022)
#show_percentage_of_gov_spending_by_year(2021)

def show_rpercentage_of_gov_spending_by_country(country_name):
    df_sample = df[df["Country"] == str(country_name)]
    df_sa_transpose = df_sample.set_index("Country").transpose()

    fig = px.line(df_sa_transpose, x=df_sa_transpose.index, y=country_name, title= 'Military expenditure in ' + country_name + 'as percentage of government spending, 1949-2022')
    fig.show()

#Usage -- Uncomment lines below
#show_rpercentage_of_gov_spending_by_country("Romania")
#show_rpercentage_of_gov_spending_by_country("Insert Country")

#show_rpercentage_of_gov_spending_by_country("Morocco")

def compare_percentage_gov_spending_by_countries_line_plot(countries_list):
    # Initialize an empty dataframe to store concatenated data
    df_concatenated = pd.DataFrame()

    # Concatenate data for each region
    for region_name in countries_list:
        df_sample = df[df["Country"] == str(region_name)]
        df_transpose = df_sample.set_index("Country").transpose()
        df_concatenated[region_name] = df_transpose[region_name]

    # Reset the index of the concatenated dataframe
    df_concatenated.reset_index(inplace=True)

    # Melt the dataframe to long format
    df_melted = pd.melt(df_concatenated, id_vars='index', var_name='Country', value_name='Percentage of Gov Spending')

    # Plot the data using Plotly Express
    fig = px.line(df_melted, x='index', y='Percentage of Gov Spending', color='Country',
                  title='Military expenditure by country as percentage of government spending, 1949-2022')
    fig.show()

#Usage -- Uncomment lines below
#compare_percentage_gov_spending_by_countries_line_plot([enter your list here])
#compare_percentage_gov_spending_by_countries_line_plot(["Algeria", "Libya", "Morocco"])

    
def compare_percentage_gov_spending_by_countries_bar_plot(countries_list):
    # Initialize an empty dataframe to store concatenated data
    df_concatenated = pd.DataFrame()

    # Concatenate data for each region
    for region_name in countries_list:
        df_sample = df[df["Country"] == str(region_name)]
        df_transpose = df_sample.set_index("Country").transpose()
        df_concatenated[region_name] = df_transpose[region_name]

    # Reset the index of the concatenated dataframe
    df_concatenated.reset_index(inplace=True)

    # Melt the dataframe to long format
    df_melted = pd.melt(df_concatenated, id_vars='index', var_name='Country', value_name='Percentage of Gov Spending')

    # Plot the data using Plotly Express
    fig = px.bar(df_melted, x='index', y='Percentage of Gov Spending', color='Country',
                  title='Military expenditure by country as percentage of government spending, 1949-2022')
    fig.show()

#Usage -- Uncomment lines below
#compare_percentage_gov_spending_by_countries_bar_plot([enter your list here])
#compare_percentage_gov_spending_by_countries_bar_plot(["Algeria", "Libya", "Morocco"])
    
df_melt = df.melt(id_vars=["Country"], 
        var_name="year", 
        value_name="Percentage of Gov spending")


def annimation():
    fig = px.scatter(df_melt, y='Percentage of Gov spending' , x="Country", title='Military expenditure by country as percentage of government spending, 1949-2022', 
                 color = 'Country', animation_frame="year", animation_group="Country")
    fig.show()

#Usage -- Uncomment lines below
annimation()