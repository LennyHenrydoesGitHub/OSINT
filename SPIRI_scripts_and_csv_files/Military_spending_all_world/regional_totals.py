# If you don't have pandas installed
# Install pip
# Install plotly and pandas with pip
import pandas as pd
import plotly.express as px

#Enter file path from your local machine
filepath = "/Users/smaranda/Documents/Data_Science/SPIRI_scripts_and_csv_files/Military_spending_all_world/Regional_totals.csv"

df = pd.read_csv(filepath)

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

def show_regional_totals_by_year(year):
    fig = px.scatter(df, y=str(year), x="Region", title='Regional totals', color = 'Region')
    fig.show()

#Usage -- Uncomment lines below
#show_regional_totals_by_year(2022)
#show_regional_totals_by_year(2021)
    
def show_regional_totals_by_country(region_name):
    df_sample = df[df["Region"] == str(region_name)]
    df_sa_transpose = df_sample.set_index("Region").transpose()

    fig = px.line(df_sa_transpose, x=df_sa_transpose.index, y=region_name, title= 'Military spending in ' + region_name + ' in US$ billions at constant 2022 prices and exchange rates')
    fig.show()

#Usage -- Uncomment lines below
#show_regional_totals_by_country("North America")
#show_regional_totals_by_country("Insert Region")
show_regional_totals_by_country("Asia & Oceania")
#show_regional_totals_by_country("Europe")

def compare_regional_totals_by_countries_line_plot(regions_list):
    # Initialize an empty dataframe to store concatenated data
    df_concatenated = pd.DataFrame()

    # Concatenate data for each region
    for region_name in regions_list:
        df_sample = df[df["Region"] == str(region_name)]
        df_transpose = df_sample.set_index("Region").transpose()
        df_concatenated[region_name] = df_transpose[region_name]

    # Reset the index of the concatenated dataframe
    df_concatenated.reset_index(inplace=True)

    # Melt the dataframe to long format
    df_melted = pd.melt(df_concatenated, id_vars='index', var_name='Region', value_name='Military_Spending')

    # Plot the data using Plotly Express
    fig = px.line(df_melted, x='index', y='Military_Spending', color='Region',
                  title='Military spending in different regions in US$ billions at constant 2022 prices and exchange rates')
    fig.show()

#Usage -- Uncomment lines below
    
#All
#compare_regional_totals_by_countries_line_plot(["World", "Africa", "North Africa", "sub-Saharan Africa", "Americas",
#                                      "Central America and the Caribbean", "North America", "South America",
#                                      "Asia & Oceania", "Oceania", "South Asia", "East Asia", "South East Asia", 
#                                      "Central Asia", "Europe", "Central Europe", "Eastern Europe", "Western Europe",
#                                      "Middle East"])
    
#Without World
#compare_regional_totals_by_countries_line_plot(["Africa", "North Africa", "sub-Saharan Africa", "Americas",
#                                      "Central America and the Caribbean", "North America", "South America",
#                                      "Asia & Oceania", "Oceania", "South Asia", "East Asia", "South East Asia", 
#                                      "Central Asia", "Europe", "Central Europe", "Eastern Europe", "Western Europe",
#                                      "Middle East"])

#Without World, Europe, Africa, Americas, Asia & Oceania, Middle East 
#compare_regional_totals_by_countries_line_plot(["North Africa", "sub-Saharan Africa",
#                                      "Central America and the Caribbean", "North America", "South America",
#                                      "Oceania", "South Asia", "East Asia", "South East Asia", 
#                                      "Central Asia", "Central Europe", "Eastern Europe", "Western Europe",
#                                      ])
    

def compare_regional_totals_by_countries_bar_plot(regions_list):
    # Initialize an empty dataframe to store concatenated data
    df_concatenated = pd.DataFrame()

    # Concatenate data for each region
    for region_name in regions_list:
        df_sample = df[df["Region"] == str(region_name)]
        df_transpose = df_sample.set_index("Region").transpose()
        df_concatenated[region_name] = df_transpose[region_name]

    # Reset the index of the concatenated dataframe
    df_concatenated.reset_index(inplace=True)

    # Melt the dataframe to long format
    df_melted = pd.melt(df_concatenated, id_vars='index', var_name='Region', value_name='Military_Spending')

    # Plot the data using Plotly Express
    fig = px.bar(df_melted, x='index', y='Military_Spending', color='Region',
                  title='Military spending in different regions in US$ billions at constant 2022 prices and exchange rates')
    fig.show()

#Usage -- Uncomment lines below

#compare_regional_totals_by_countries_bar_plot(["Africa", "Americas", "Asia & Oceania", "Europe", "Middle East"])

#compare_regional_totals_by_countries_bar_plot(["North Africa", "sub-Saharan Africa",
#                                      "Central America and the Caribbean", "North America", "South America",
#                                      "Oceania", "South Asia", "East Asia", "South East Asia", 
#                                      "Central Asia", "Central Europe", "Eastern Europe", "Western Europe",
#                                      ])
    
df_melt = df.melt(id_vars=["Region"], 
        var_name="year", 
        value_name="billion US $")


def annimation():
    fig = px.scatter(df_melt, y='billion US $' , x="Region", title='Military spending in different regions in US$ billions at constant 2022 prices and exchange rates', 
                 color = 'Region', animation_frame="year", animation_group="Region")
    fig.show()

#annimation()
