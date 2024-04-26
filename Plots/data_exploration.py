import pandas as pd
import plotly.express as px

f = "../Visualization/conversion.csv"
country_codes = pd.read_csv('../Visualization/country_codes-ICB.csv')
trade_data = pd.read_csv('../ICB DATA/all_alphabetical_by_recipient.csv')
icb2 = pd.read_csv('../ICB DATA/icb2v15.csv')

code_to_name = dict(zip(country_codes['Country codes'], country_codes['Name']))
icb2['country'] = icb2['actor'].map(code_to_name)


def plot(df, x, y, title):
    fig = px.bar(df, x=x, y=y, title=title)

    fig.update_layout(margin={"r": 50, "t": 150, "l": 150, "b": 10})
    fig.update_layout(
        font=dict(size=25)
    )
    fig.show()


def countries_involvement_in_wars():
    countries_appearing_in_data = []
    list_of_countries = []

    for i in range(icb2.shape[0]):
        countries_appearing_in_data.append(icb2.loc[i]['country'])
        if not list_of_countries.__contains__(icb2.loc[i]['country']):
            list_of_countries.append(icb2.loc[i]['country'])

    appearances = []
    for country in list_of_countries:
        appearances.append([country, countries_appearing_in_data.count(country)])

    df = pd.DataFrame(appearances, columns=["", "Number of times involved in wars"])
    df = df.sort_values(by=['Number of times involved in wars'], ascending=False)
    return df


def suppliers_ranked():
    orders = []
    list_of_countries = []

    for i in range(trade_data.shape[0]):
        orders.append([trade_data.loc[i]['Supplier'], trade_data.loc[i]['SIPRI TIV for total order']])
        if not list_of_countries.__contains__(trade_data.loc[i]['Supplier']):
            list_of_countries.append(trade_data.loc[i]['Supplier'])

    list_of_countries.remove("Soviet Union")
    list_of_countries.remove("East Germany (GDR)")
    list_of_countries.remove("Czechoslovakia")

    appearances = []
    for country in list_of_countries:
        total = 0
        for order in orders:
            if country == order[0]:
                total += order[1]
            if order[0] == "Soviet Union" and country == "Russia":
                total += order[1]
            if order[0] == "East Germany (GDR)" and country == "Germany":
                total += order[1]
            if order[0] == "Czechoslovakia" and country == "Czechia":
                total += order[1]
        appearances.append([country, total])

    df = pd.DataFrame(appearances, columns=["", "TIV of arms exported"])
    df = df.sort_values(by=['TIV of arms exported'], ascending=False)
    return df


def importers_ranked():
    orders = []
    list_of_countries = []

    for i in range(trade_data.shape[0]):
        orders.append([trade_data.loc[i]['Recipient'], trade_data.loc[i]['SIPRI TIV for total order']])
        if not list_of_countries.__contains__(trade_data.loc[i]['Recipient']):
            list_of_countries.append(trade_data.loc[i]['Recipient'])

    list_of_countries.remove("Soviet Union")
    list_of_countries.remove("East Germany (GDR)")

    appearances = []
    for country in list_of_countries:
        total = 0
        for order in orders:
            if country == order[0]:
                total += order[1]
            if order[0] == "Soviet Union" and country == "Russia":
                total += order[1]
            if order[0] == "East Germany (GDR)" and country == "Germany":
                total += order[1]
        appearances.append([country, total])

    df = pd.DataFrame(appearances, columns=["", "TIV of arms imported"])
    df = df.sort_values(by=['TIV of arms imported'], ascending=False)
    return df


def scatter_plot_relation():
    df = countries_involvement_in_wars()
    # df = df.sort_values(by=[''])

    df2 = importers_ranked()
    # df2 = df2.sort_values(by=[''])

    df3 = suppliers_ranked()
    df3 = df3.sort_values(by=[''])

    data = []
    i = 1
    for _, row2 in df2.iterrows():
        j = 1
        last_row = 100
        for _, row in df.iterrows():
            # for _, row3 in df3.iterrows():
            # if (row[''] != "United States" and row[''] != "Russia" and row[''] != "France"
                    # and row[''] != "United Kingdom" and row[''] != "Israel"):
                if row[''] == row2[''] and row[''] != "Thailand":
                    # if row3['TIV of arms exported'] > 500000:
                    #     top_exports = 5
                    # elif row3['TIV of arms exported'] > 100000:
                    #     top_exports = 4
                    # elif row3['TIV of arms exported'] > 50000:
                    #     top_exports = 3
                    # elif row3['TIV of arms exported'] > 10000:
                    #     top_exports = 2
                    # elif row3['TIV of arms exported'] > 5000:
                    #     top_exports = 1
                    # else:
                    #     top_exports = 0
                    data.append([row[''], j, i, row['Number of times involved in wars'],
                                 round(row2['TIV of arms imported'])])
                if row['Number of times involved in wars'] < last_row:
                    j += 1
                last_row = row['Number of times involved in wars']
        i += 1

    df = pd.DataFrame(data, columns=['Country name', 'Rank_wars', 'Rank_imports',
                                     'Number of times involved in wars', 'TIV of arms imported'])
    return df


# df = countries_involvement_in_wars()
# df = df[df['Number of times involved in wars'] > 15]
# plot(df, "", "Number of times involved in wars", 'Countries that participated in more than 15 wars, 1949-2022')

# df = suppliers_ranked()
# df = df[df['TIV of arms exported'] >= 30000]
# plot(df, "", "TIV of arms exported", 'Countries with the highest TIV of exported arms, 1949-2022')

df = importers_ranked()
df = df[df['TIV of arms imported'] >= 20000]
plot(df, "", "TIV of arms imported", 'Countries with the highest TIV of imported arms, 1949-2022')

# df = scatter_plot_relation()
# fig = px.scatter(df, y="TIV of arms imported", x='Number of times involved in wars',
#                  hover_data=['Country name', 'Rank_wars', 'Rank_imports'], trendline="ols")
#
# fig.update_layout(margin={"r": 50, "t": 150, "l": 150, "b": 10})
# fig.update_layout(
#     font=dict(size=25)
# )
# fig.show()
