import plotly.express as px
import pandas as pd

# Replace 'file_path.csv' with the path to your CSV file
# file_path = 'final_matrix_data.csv'
#
# # Import the CSV file as a DataFrame
# df = pd.read_csv(file_path)

df = pd.read_csv("conversion.csv")
df = df.sort_values(by=['Country Name'])
df = df.sort_values(by=['Year'])

# Create the choropleth map
fig = px.choropleth(df, 
                    locations="Country code",
                    # color="No. of Military Conflicts",
                    color="Conflict",
                    hover_name="Country Name",
                    animation_frame="Year",
                    range_color=[-0.5, 1],
                    color_continuous_scale="blues")

# Add a title to the plot
fig.update_layout(title_text='Military Conflicts by Country and Year')

fig.show()

fig.write_html("./html_maps/real_map_colorblind.html")
