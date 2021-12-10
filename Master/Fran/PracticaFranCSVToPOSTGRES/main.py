import pandas as pd
import psycopg2
from psycopg2 import Error

pd.set_option('max_columns', None)
equipos = pd.read_csv("teams.csv")
dfequipos = pd.DataFrame(equipos)
jugadores = pd.read_csv("players.csv")
dfjugadores = pd.DataFrame(jugadores)
estadisticas = pd.read_csv("ranking.csv")
dfestadisticas = pd.DataFrame(estadisticas)

dfjugadores = dfjugadores.drop(dfjugadores[dfjugadores['SEASON'] != 2019].index)
dfjugadores = dfjugadores.drop(['PLAYER_ID', 'SEASON'], axis=1)

dfequipos = dfequipos.drop(
    ['LEAGUE_ID', 'MIN_YEAR', 'MAX_YEAR', 'ABBREVIATION', 'YEARFOUNDED', 'CITY', 'ARENA', 'ARENACAPACITY', 'OWNER',
     'GENERALMANAGER', 'HEADCOACH', 'DLEAGUEAFFILIATION', 'NICKNAME'], axis=1)

dfestadisticas = dfestadisticas.drop(dfestadisticas[dfestadisticas['SEASON_ID'] != 22019].index)
dfestadisticas['STANDINGSDATE'] = pd.to_datetime(dfestadisticas['STANDINGSDATE'], format='%Y-%m-%d')
dfestadisticas = dfestadisticas.loc[(dfestadisticas['STANDINGSDATE'] == '2019-12-10')]
dfestadisticas = dfestadisticas.drop(
    ['LEAGUE_ID', 'SEASON_ID', 'CONFERENCE', 'STANDINGSDATE', 'G', 'W', 'L', 'HOME_RECORD', 'ROAD_RECORD',
     'RETURNTOPLAY'], axis=1)


dfEqEst = pd.merge(left=dfestadisticas,right=dfequipos, left_on='TEAM_ID', right_on='TEAM_ID')
dfFINAL = pd.merge(left=dfestadisticas,right=dfjugadores, left_on='TEAM_ID', right_on='TEAM_ID')
dfFINAL = dfFINAL.drop(['TEAM_ID'], axis=1)

try:
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="fran")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE estadisticas
              (EQUIPO             TEXT    NOT NULL,
              PORCENTAJE_VICTORIAS      REAL    NOT NULL,
              NOMBRE_JUGADOR         TEXT  NOT NULL); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")
    record = 0
    for row in dfFINAL.index:
        equipo = dfFINAL["TEAM"][row]
        porcentajeVictorias = dfFINAL["W_PCT"][row]
        nombreJugador = dfFINAL["PLAYER_NAME"][row]
        insert_query = """INSERT INTO estadisticas (EQUIPO, PORCENTAJE_VICTORIAS, NOMBRE_JUGADOR) VALUES (%s , %s, 
        %s) """
        cursor.execute(insert_query, (equipo, porcentajeVictorias, nombreJugador))
        record += 1

    connection.commit()
    print("Inserted successfully " + str(record) + " rows")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")