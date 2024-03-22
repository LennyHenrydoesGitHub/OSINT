# If you don't have pandas installed
# Install pip
# Install plotly and pandas with pip
import pandas as pd
import plotly.express as px

# Add your file path
file_path = '/Users/smaranda/Documents/Data_Science/SPIRI_scripts_and_csv_files/Military_spending_all_world/Share_of_GDP_all_world.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, encoding='latin1')

# Filter data for North America and China
north_us_data = df[df['Country'] == 'North America']
china_data = df[df['Country'] == 'China']

# Plot the scatter plot
fig = px.scatter(df, x='2020', y='2019', color="Country")

# Add title to the plot
fig.update_layout(title='Percentage of Country GDP Allocated to Military Spending in 2020 & 2019')

# Show the plot
fig.show()



# Display the DataFrame
#print(df)

#print a column
#print(df['2014'])

#print(df.info())

#print(df.head(n=5))

#print(df.columns)

#print(df['Country'])

# Open a file in write mode

#print(df.loc[2])


#df[df['Country'] == 'Africa'].describe().to_csv(file_path_out, index=False, header=False)    

#row access
#df.loc[0]
    
