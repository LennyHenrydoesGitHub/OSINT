import plotly.express as px
import pandas as pd

# Replace 'file_path.csv' with the path to your CSV file
file_path = 'final_matrix_data.csv'

# Import the CSV file as a DataFrame
df = pd.read_csv(file_path)

# Create the choropleth map
fig = px.choropleth(df, 
                    locations="Country code", 
                    color="No. of Military Conflicts", 
                    hover_name="Country Name", 
                    animation_frame="Year", 
                    range_color=[0, 4], 
                    color_continuous_scale="Portland")

# Add a title to the plot
fig.update_layout(title_text='Military Conflicts by Country and Year')


fig.show()
