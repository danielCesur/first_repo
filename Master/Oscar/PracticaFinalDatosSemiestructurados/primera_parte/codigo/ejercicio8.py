import pandas as pd

if __name__ == '__main__':
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 3)
    # Load pandas dataframe df with data from players.csv
    df = pd.read_csv("../../data/all_players.csv", low_memory=False)
    # Get new dataset df_summary containing only selected columns
    df_summary = df[['Player', 'G']]
    df2 = df_summary.groupby(['Player']).sum()
    df2.sort_values(by=['G'], inplace=True, ascending=False)

    result = df2.head(1)
    result.to_csv('../KPIs/resultado8.csv')
    print(result)
