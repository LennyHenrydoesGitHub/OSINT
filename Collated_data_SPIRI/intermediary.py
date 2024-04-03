# If you don't have pandas installed
# Install pip
# Install plotly and pandas with pip
import pandas as pd
import plotly.express as px
import numpy as np
import argparse
import math

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
    print("==============Supplier Countries==============")
    print(df['Supplier'].unique())
    print("==============Year of order==============")
    print(df['Year of order'].unique())
    print("==============Number ordered==============")
    print(df['Number ordered'].unique())
    print("==============Weapon designation==============")
    print(df['Weapon designation'].unique())
    print("==============Weapon description==============")
    print(df['Weapon description'].unique())
    print("==============Number delivered==============")
    print(df['Number delivered'].unique())
    print("==============Year(s) of delivery==============")
    print(df['Year(s) of delivery'].unique())
    print("==============status==============")
    print(df['status'].unique())
    print("==============Comments==============")
    print(df['Comments'].unique())
    print("==============SIPRI TIV per unit==============")
    print(df['SIPRI TIV per unit'].unique())
    print("==============SIPRI TIV for total order==============")
    print(df['SIPRI TIV for total order'].unique())
    print("==============SIPRI TIV of delivered weapons==============")
    print(df['SIPRI TIV of delivered weapons'].unique())

#Usage -- Uncomment lines below
#info_more(df)

def pick_country(df, name, as_what):
    name = str(name)
    as_what = str(as_what)
    df_country = df[df[as_what] == name]
    filepath = "output/" + name + "_" + as_what + ".csv"
    df_country.to_csv(filepath, index=False)
    #print(df_country["Year(s) of delivery"].iloc[10].type())

    for i in range(0,df_country.shape[0]):
        if df_country["Year(s) of delivery"].iloc[i] != None:
            print(len(df_country["Year(s) of delivery"].iloc[i]))
            print(df_country["Year(s) of delivery"].iloc[i])

    print(f"DataFrame saved to {filepath}")

#Year of Order
def pick_time_period_yr_of_order(df, name, as_what, start, end):
    name = str(name)
    as_what = str(as_what)
    start = int(start)
    end = int(end)
    if end < start:
        start,end = end,start  
    df_country = df[df[as_what] == name].copy()  # Ensure to work with a copy
    df_country.loc[:, 'Year of order'] = df_country['Year of order'].astype(int)
    df_time_period = df_country[(df_country['Year of order'] >= start) & (df_country['Year of order'] <= end)]
    filepath = f"output/{name}_{as_what}_{start}_to_{end}.csv"
    df_time_period.to_csv(filepath, index=False)
    print(f"DataFrame saved to {filepath}")

#Year of delivery - unstable
def pick_time_period_yr_of_delivery(df, name, as_what, start, end):
    name = str(name)
    as_what = str(as_what)
    start = int(start)
    end = int(end)
    if end < start:
        start,end = end,start  
    
    df_country = df[df[as_what] == name].copy()  # Ensure to work with a copy

    # Convert 'Year(s) of delivery' to numeric, treating non-numeric values as NaN
    df_country.loc[:, 'Year(s) of delivery'] = pd.to_numeric(df_country['Year(s) of delivery'], errors='coerce')

    for i in range(df_country.shape[0]):
        if not np.isnan(df_country['Year(s) of delivery'].iloc[i]):  # Check if value is not NaN
            year = df_country['Year(s) of delivery'].iloc[i]
            if isinstance(year, float):  # Check if it's a float
                year = int(year)  # Convert to integer
            if len(str(year)) != 4:
                year = int(str(year)[-4:])
            df_country.loc[df_country.index[i], 'Year(s) of delivery'] = year
        
    df_time_period = df_country[(df_country['Year of order'] >= start) & (df_country['Year of order'] <= end)]
    filepath = f"output/{name}_{as_what}_{start}_to_{end}.csv"
    df_time_period.to_csv(filepath, index=False)
    print(f"DataFrame saved to {filepath}")
    

if __name__ == "__main__":
    # Setting up argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', '--filepath', type=str, help='Filepath of the CSV file')
    parser.add_argument('--show-info', action='store_true', help='Show basic info of DataFrame of CSV')
    parser.add_argument('--info-more', action='store_true', help='Show more detailed info of DataFrame of CSV')
    parser.add_argument('-c', nargs=2, metavar=('NAME', 'AS_WHAT'), help='e.g.usage: python intermediary.py -f filename -c "Belarus" "Recipient"')
    parser.add_argument('-ct', nargs=4, metavar=('NAME', 'AS_WHAT', 'START', 'END'), help='e.g. usage: python intermediary.py -f all_alphabetical_by_recipient.csv -ct "Brazil" "Supplier" 2010 2023')
    #This one is faulty
    parser.add_argument('-t', nargs=4, metavar=('NAME', 'AS_WHAT', 'START', 'END'), help='e.g. usage: python intermediary.py -f all_alphabetical_by_recipient.csv -t "Brazil" "Supplier" 2010 2023')

    args = parser.parse_args()

    # Checking if filepath is provided
    if args.filepath:
        df = pd.read_csv(args.filepath, encoding='latin1')
        if args.show_info:
            show_info(df)
        elif args.info_more:
            info_more(df)
        elif args.c:
            pick_country(df, args.c[0], args.c[1])
        elif args.ct:
            pick_time_period_yr_of_order(df, args.ct[0], args.ct[1], args.ct[2], args.ct[3])
        elif args.t:
            pick_time_period_yr_of_delivery(df, args.t[0], args.t[1], args.t[2], args.t[3])
        else:
            print("No action specified. Use --show-info or --info-more.")

    else:
        print("Filepath not provided. Use -f or --filepath option.")