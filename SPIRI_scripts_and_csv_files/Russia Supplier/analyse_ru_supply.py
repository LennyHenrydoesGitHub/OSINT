# If you don't have pandas installed
# Install pip
# Install plotly and pandas with pip
import pandas as pd
import plotly.express as px
import numpy as np

#Enter file path from your local machine
filepath = "/Users/smaranda/Documents/Data_Science/SPIRI_scripts_and_csv_files/Trade Registry/Russia Supplier/trade-register.csv"

df = pd.read_csv(filepath, encoding='latin1')

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
    
def info_more(df):
    print("==============Recipient Countries==============")
    print(df['Recipient'].unique())
    print("==============Arms==============")
    print(df['Weapon designation'].unique())
    print("==============Descriptions==============")
    print(df['Weapon description'].unique())
    

#Usage -- Uncomment lines below
#info_more(df)

def occurance_of_country_in_registry(country):
    return(df["Recipient"] == country).sum()

def gather_all_country_occurances():
    occurances = []
    for i in df['Recipient'].unique():
        pair = [i, occurance_of_country_in_registry(i)]
        occurances.append(pair)
    
    return occurances

def occurance_ranking_descending():
    pairs = gather_all_country_occurances()
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    #For ascending ranking remove .reverse()
    sorted_pairs.reverse()
    return sorted_pairs

def show_occurance_of_countries_descending():
    counts = occurance_ranking_descending()

    x_values = [item[0] for item in counts]
    y_values = [item[1] for item in counts]

    print('x_values')
    print(x_values)
    print('y_values')
    print(y_values)

    df = pd.DataFrame({'Country Supplied By Russia and former Soviet Union With Arms': x_values, 'Number Of Trades In The Year Range 1950 - 2023': y_values})

    # Create bar plot using Plotly Express
    fig = px.bar(df, title= 'Number Of Arm Trades In The Year Range 1950 - 2023 Supplied By Russia and former Soviet Union To Recipient Countries',x='Country Supplied By Russia and former Soviet Union With Arms', y='Number Of Trades In The Year Range 1950 - 2023', template="simple_white")
    # Increase font size
    # Calculate statistics
    median_value = np.median(y_values)
    average_value = np.mean(y_values)

    # Add annotations for median and average values
    # Calculate statistics
    median_value = np.median(y_values)
    average_value = np.mean(y_values)
    std_deviation_value = np.std(y_values)
    min_value = np.min(y_values)
    max_value = np.max(y_values)

    # Add annotations for statistics
    fig.update_layout(annotations=[
        dict(
            x=0.5,
            y=median_value,
            xref='paper',
            yref='y',
            text=f'Median: {median_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        dict(
            x=0.5,
            y=average_value,
            xref='paper',
            yref='y',
            text=f'Average: {average_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-60
        ),
        dict(
            x=0.5,
            y=std_deviation_value,
            xref='paper',
            yref='y',
            text=f'Standard Deviation: {std_deviation_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-80
        ),
        dict(
            x=0.5,
            y=min_value,
            xref='paper',
            yref='y',
            text=f'Minimum: {min_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-100
        ),
        dict(
            x=0.5,
            y=max_value,
            xref='paper',
            yref='y',
            text=f'Maximum: {max_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-120
        )
    ])

    fig.write_html("plotly_graph.html")
    fig.show()

#Usage -- Uncomment lines below
#show_occurance_of_countries_descending()

def occurance_of_armament_category_in_registry(category):
    return(df["Weapon description"] == category).sum()

def gather_all_arms_category_occurances():
    occurances = []
    for i in df['Weapon description'].unique():
        pair = [i, occurance_of_armament_category_in_registry(i)]
        occurances.append(pair)
    
    return occurances

def arms_category_ranking_descending():
    pairs = gather_all_arms_category_occurances()
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    #For ascending ranking remove .reverse()
    sorted_pairs.reverse()
    return sorted_pairs

def show_occurance_of_arms_category_descending():
    counts = arms_category_ranking_descending()

    x_values = [item[0] for item in counts]
    y_values = [item[1] for item in counts]

    df = pd.DataFrame({'Armament Category': x_values, 'Number of Trades': y_values})

    # Create bar plot using Plotly Express
    fig = px.bar(df,title='Number Of Trades Based On Armament Category Between 1950 To 2023 With Russia and Former Soviet Union As Supplier Country', x='Armament Category', y='Number of Trades', template="simple_white")
    # Add annotations for median and average values
    # Calculate statistics
    median_value = np.median(y_values)
    average_value = np.mean(y_values)
    std_deviation_value = np.std(y_values)
    min_value = np.min(y_values)
    max_value = np.max(y_values)

    # Add annotations for statistics
    fig.update_layout(annotations=[
        dict(
            x=0.5,
            y=median_value,
            xref='paper',
            yref='y',
            text=f'Median: {median_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        dict(
            x=0.5,
            y=average_value,
            xref='paper',
            yref='y',
            text=f'Average: {average_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-60
        ),
        dict(
            x=0.5,
            y=min_value,
            xref='paper',
            yref='y',
            text=f'Minimum: {min_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-100
        ),
        dict(
            x=0.5,
            y=max_value,
            xref='paper',
            yref='y',
            text=f'Maximum: {max_value}',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-120
        )
    ])

     
    fig.write_html("traded-weapon-categories.html") 
    fig.show()

#Usage -- Uncomment lines below
#show_occurance_of_arms_category_descending()
    
df_aircraft = df[df["Weapon description"] == "transport helicopter"] 
df_armed_vechicles = df[df["Weapon description"] == "fighter aircraft"]
df_missiles = df[df["Weapon description"] == "SAM"]
#df_engines = df[df["Armament category"] == "Engines"]
#df_sensors = df[df["Armament category"] == "Sensors"]
#df_ships = df[df["Armament category"] == "Ships"]
#df_artillery = df[df["Armament category"] == "Artillery"] 
#df_other = df[df["Armament category"] == "Other"]
#df_air_defence_system = df[df["Armament category"] == "Air defence systems"]
#df_naval_weapons = df[df["Armament category"] == "Naval weapons"]

#df_list = [df_aircraft, df_armed_vechicles, df_missiles, df_engines, df_sensors, df_ships, df_artillery, df_other, df_air_defence_system, df_naval_weapons]

# repetitive code below not good practice i know i can;t be bothered right now

def occurance_of_country_in_registry(country):
        return(df_aircraft["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_aircraft['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Recipient Country': x_values, 'Number of Trades of Transport Helicopters': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Recipient Country', y='Number of Trades of Transport Helicopters', template="simple_white", title = "Number Of Trades Of Transport Helicopters Supplied By Russia and Former Soviet Union To Recipient Countries between 1950 to 2023")
         # Calculate statistics
        median_value = np.median(y_values)
        average_value = np.mean(y_values)
        std_deviation_value = np.std(y_values)
        min_value = np.min(y_values)
        max_value = np.max(y_values)

        # Add annotations for statistics
        fig.update_layout(annotations=[
                dict(
                x=0.5,
                y=median_value,
                xref='paper',
                yref='y',
                text=f'Median: {median_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-40
                ),
                dict(
                x=0.5,
                y=average_value,
                xref='paper',
                yref='y',
                text=f'Average: {average_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-60
                ),
                dict(
                x=0.5,
                y=min_value,
                xref='paper',
                yref='y',
                text=f'Minimum: {min_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-100
                ),
                dict(
                x=0.5,
                y=max_value,
                xref='paper',
                yref='y',
                text=f'Maximum: {max_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-120
                )
        ])
     
        fig.write_html("traded-transport-helicopters.html") 
        fig.show()

#Usage -- Uncomment lines below and replace df with df_something from the list above
# Shows occurances of sold aircrafts to all countries
#show_occurance_of_countries_descending()
        
def occurance_of_country_in_registry(country):
        return(df_armed_vechicles["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_armed_vechicles['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Recipient Country': x_values, 'Number of Trades of Fighter Aircrafts': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Recipient Country', y='Number of Trades of Fighter Aircrafts', template="simple_white", title = "Number Of Trades Of Fighter Aircrafts Supplied By Russia and Soviet Union To Recipient Countries between 1950 to 2023")
         # Calculate statistics
        median_value = np.median(y_values)
        average_value = np.mean(y_values)
        std_deviation_value = np.std(y_values)
        min_value = np.min(y_values)
        max_value = np.max(y_values)

        # Add annotations for statistics
        fig.update_layout(annotations=[
                dict(
                x=0.5,
                y=median_value,
                xref='paper',
                yref='y',
                text=f'Median: {median_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-40
                ),
                dict(
                x=0.5,
                y=average_value,
                xref='paper',
                yref='y',
                text=f'Average: {average_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-60
                ),
                dict(
                x=0.5,
                y=min_value,
                xref='paper',
                yref='y',
                text=f'Minimum: {min_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-100
                ),
                dict(
                x=0.5,
                y=max_value,
                xref='paper',
                yref='y',
                text=f'Maximum: {max_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-120
                )
        ])
     
        fig.write_html("traded-armoured-vehicles.html") 
        fig.show()

#Usage -- Uncomment lines below and replace df with df_something from the list above
# Shows occurances of sold armed vehicles to all countries
#show_occurance_of_countries_descending()
        
def occurance_of_country_in_registry(country):
        return(df_missiles["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_missiles['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Recipient Country': x_values, 'Number of Trades of  Surface-to-air Missile': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Recipient Country', y='Number of Trades of  Surface-to-air Missile', template="simple_white", title = "Number Of Trades Of Surface-to-air Missile Supplied By Russia and Former Soviet Union To Recipient Countries between 1950 to 2023")
         # Calculate statistics
        median_value = np.median(y_values)
        average_value = np.mean(y_values)
        std_deviation_value = np.std(y_values)
        min_value = np.min(y_values)
        max_value = np.max(y_values)

        # Add annotations for statistics
        fig.update_layout(annotations=[
                dict(
                x=0.5,
                y=median_value,
                xref='paper',
                yref='y',
                text=f'Median: {median_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-40
                ),
                dict(
                x=0.5,
                y=average_value,
                xref='paper',
                yref='y',
                text=f'Average: {average_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-60
                ),
                dict(
                x=0.5,
                y=min_value,
                xref='paper',
                yref='y',
                text=f'Minimum: {min_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-100
                ),
                dict(
                x=0.5,
                y=max_value,
                xref='paper',
                yref='y',
                text=f'Maximum: {max_value}',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-120
                )
        ])
     
        fig.write_html("traded-missiles.html")
        fig.show()

#Usage -- Uncomment lines below and replace df with df_something from the list above
# Shows occurances of sold missiles to all countries
show_occurance_of_countries_descending()
    
def occurance_of_country_in_registry(country):
        return(df_engines["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_engines['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Country': x_values, 'Occurances': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Country', y='Occurances', template="simple_white", title = "Occurances of Engines Sold by US to Countries below")
        fig.show()

#Usage -- Uncomment relevant lines below 
# Shows occurances of sold missiles to all countries
#show_occurance_of_countries_descending()
        
def occurance_of_country_in_registry(country):
        return(df_sensors["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_sensors['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Country': x_values, 'Occurances': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Country', y='Occurances', template="simple_white", title = "Occurances of Engines Sold by US to Countries below")
        fig.show()

#Usage -- Uncomment relevant lines below 
# Shows occurances of sold sensors to all countries
#show_occurance_of_countries_descending()
        
def occurance_of_country_in_registry(country):
        return(df_ships["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_ships['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Country': x_values, 'Occurances': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Country', y='Occurances', template="simple_white", title = "Occurances of Ships Sold by US to Countries below")
        fig.show()

#Usage -- Uncomment relevant lines below 
# Shows occurances of sold sensors to all countries
#show_occurance_of_countries_descending()

def occurance_of_country_in_registry(country):
        return(df_artillery["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_artillery['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Country': x_values, 'Occurances': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Country', y='Occurances', template="simple_white", title = "Occurances of Artillery Sold by US to Countries below")
        fig.show()

#Usage -- Uncomment relevant lines below 
# Shows occurances of sold sensors to all countries
#show_occurance_of_countries_descending()
        
def occurance_of_country_in_registry(country):
        return(df_other["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_other['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Country': x_values, 'Occurances': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Country', y='Occurances', template="simple_white", title = "Occurances of Artillery Sold by US to Countries below")
        fig.show()

#Usage -- Uncomment relevant lines below 
# Shows occurances of sold sensors to all countries
#show_occurance_of_countries_descending()
        
def occurance_of_country_in_registry(country):
        return(df_air_defence_system["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_air_defence_system['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Country': x_values, 'Occurances': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Country', y='Occurances', template="simple_white", title = "Occurances of Air Defence Systems Sold by US to Countries below")
        fig.show()

#Usage -- Uncomment relevant lines below 
# Shows occurances of sold sensors to all countries
#show_occurance_of_countries_descending()

def occurance_of_country_in_registry(country):
        return(df_naval_weapons["Recipient"] == country).sum()

def gather_all_country_occurances():
        occurances = []
        for i in df_naval_weapons['Recipient'].unique():
            pair = [i, occurance_of_country_in_registry(i)]
            occurances.append(pair)
        
        return occurances

def occurance_ranking_descending():
        pairs = gather_all_country_occurances()
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        #For ascending ranking remove line below; 
        sorted_pairs.reverse()
        return sorted_pairs

def show_occurance_of_countries_descending():
        counts = occurance_ranking_descending()

        x_values = [item[0] for item in counts]
        y_values = [item[1] for item in counts]

        df = pd.DataFrame({'Country': x_values, 'Occurances': y_values})

        # Create bar plot using Plotly Express
        fig = px.bar(df, x='Country', y='Occurances', template="simple_white", title = "Occurances of Naval Weapons Sold by US to Countries below")
        fig.show()

#Usage -- Uncomment relevant lines below 
# Shows occurances of sold sensors to all countries
#show_occurance_of_countries_descending()