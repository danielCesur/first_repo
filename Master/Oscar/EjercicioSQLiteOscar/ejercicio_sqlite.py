from sqlalchemy import create_engine
import pandas as pd

if __name__ == '__main__':
    engine =  create_engine('sqlite:///ejercicio_sqlite.db', echo = True)

    # Load pandas dataframe df with data from players.csv
    df = pd.read_csv("all_players.csv", low_memory=False)
    # Get new dataset df_summary containing only selected columns
    df = pd.DataFrame(columns=['player', 'club', 'year', 'mins', 'pos'])
    df_summary = df[['home', 'away', 'date', 'home_score', 'away_score']]
    # Create connection

    # Begin transaction

    # insert each row of the dataframe in the table "Players" of the database
    for row in df_summary.index:
        # build the query

        #execute the query
        connection.execute(query)
        print(f'Registro {row} de {len(df_summary)}')

    # commit transaction

    # close connection

    # query: select player name of those with MINS > 3000
    df_result = # execute the select using pandas capabilities
    print(df_result)
