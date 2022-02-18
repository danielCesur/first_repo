from sqlalchemy import create_engine
import pandas as pd

if __name__ == '__main__':
    engine =  create_engine('sqlite:///ejercicio_sqlite.db', echo = True)

    # Load pandas dataframe df with data from players.csv
    df = pd.read_csv("all_players.csv", low_memory=False)
    # Get new dataset df_summary containing only selected columns
    df_summary = df[['Player', 'Club', 'Year', 'MINS', 'POS']]
    # Create connection
    connection = engine.connect()
    # Begin transaction
    transaction = connection.begin()
    # insert each row of the dataframe in the table "Players" of the database
    for row in df_summary.index:
        # build the query
        query = f'insert into Players values("{df_summary["Player"][row]}","{df_summary["Club"][row]}",{df_summary["Year"][row]},{df_summary["MINS"][row]},"{df_summary["POS"][row]}")'
        #execute the query
        connection.execute(query)
        print(f'Registro {row} de {len(df_summary)}')
        print(query)
    # commit transaction
    transaction.commit()
    # close connection
    connection.close()
    # query: select player name of those with MINS > 3000
    df_result = pd.read_sql("SELECT player, mins FROM Players WHERE mins > 3000", con="sqlite:///ejercicio_sqlite.db")
    # execute the select using pandas capabilities
    print(df_result)
    df2.to_csv('out.csv', index=False)