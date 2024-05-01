import plotly.express as px
import pandas as pd

# Replace 'file_path.csv' with the path to your CSV file
file_path = 'final_matrix_data.csv'

# Import the CSV file as a DataFrame
df = pd.read_csv(file_path)

convert = pd.read_csv("./converter")
name_to_name = dict(zip(convert['Name 1'], convert[' Name 2']))
df['Country Name'] = df['Country Name'].map(name_to_name)

# df = pd.read_csv("./conversion/conversion.csv")
# df = df.sort_values(by=['Country Name'])
# df = df.sort_values(by=['Year'])

df2 = pd.read_csv("../Collated_data_SPIRI/all_alphabetical_by_recipient.csv")
df2 = df2.sort_values(by=['Recipient'])

header = ['Country name', 'Year', 'Country code', 'No. of Military Conflicts', 'Suppliers']
new_data = []
i = 0
for index, row in df.iterrows():
    if i < 120:
        data = []
        suppliers = []
        for index2, row2 in df2.iterrows():
            if row['Country Name'] == row2['Recipient']:
                if row['Year'] == row2["Year of order"]:
                    print(row2['Supplier'])
                    data.append(row2['Supplier'])
                    if not suppliers.__contains__(row2['Supplier']):
                        suppliers.append(row2['Supplier'])
        new_suppliers = []
        for supplier in suppliers:
            new_suppliers.append([supplier, data.count(supplier)])
        new_data.append([row['Country Name'], row['Year'], row['Country code'], row['No. of Military Conflicts'], new_suppliers])
    i += 1
new_df = pd.DataFrame(data=new_data, columns=header)
print(new_df)

# Create the choropleth map
fig = px.choropleth(new_df,
                    locations="Country code",
                    color="No. of Military Conflicts",
                    hover_name="Country name",
                    hover_data=["Suppliers"],
                    animation_frame="Year",
                    range_color=[0, 4],
                    color_continuous_scale="Portland")

# Add a title to the plot
fig.update_layout(title_text='Military Conflicts by Country and Year')

# Customize hover information to include data from the second DataFrame
# fig.update_traces(hovertemplate='<b>%{hovertext}</b><br>' +
#                                   'No. of Military Conflicts: %{z}<br>' +
#                                   '<extra>Testing</extra>')

fig.show()

fig.write_html("./html_maps/model3_map.html")
