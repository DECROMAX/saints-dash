import pandas as pd


COL_LABELS = {
    "Div": "division",
    "Date": "match_date",
    "Time": "kickoff_time",
    "HomeTeam": "home_team",
    "AwayTeam": "away_team",
    "FTHG": "home_goals_ft",
    "FTAG": "away_goals_ft",
    "FTR": "result_ft",
    "HTHG": "home_goals_ht",
    "HTAG": "away_goals_ht",
    "HTR": "result_ht",
    "Referee": "referee",
    "HS": "home_shots",
    "AS": "away_shots",
    "HST": "home_shots_on_target",
    "AST": "away_shots_on_target",
    "HC": "home_corners",
    "AC": "away_corners",
}

df = pd.read_csv('https://www.football-data.co.uk/mmz4281/2526/E1.csv', usecols=COL_LABELS.keys())
df = df.rename(columns=COL_LABELS)

df['match_date_time'] = pd.to_datetime((df['match_date'] + ' ' + df['kickoff_time']), format='mixed', dayfirst=True)