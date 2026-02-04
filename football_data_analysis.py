import marimo

__generated_with = "0.19.6"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    import numpy as np

    # pandas display options
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)

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
    return COL_LABELS, np, pd


@app.cell
def _(COL_LABELS, pd):
    df_ = pd.read_csv(
        "https://www.football-data.co.uk/mmz4281/2526/E1.csv",
        usecols=COL_LABELS.keys(),
    )
    df2 = df_.rename(columns=COL_LABELS)


    df2
    return (df2,)


@app.cell
def _(df2, pd):
    df2["match_date_time"] = pd.to_datetime(
        (df2["match_date"] + " " + df2["kickoff_time"]),
        format="mixed",
        dayfirst=True,
    )
    df3 = df2.drop(columns=["match_date", "kickoff_time"])
    df3["match_day_name"] = df3["match_date_time"].dt.dayofweek

    target_team = "Southampton"
    df_saints = df3.loc[
        (df3["home_team"] == target_team) | (df3["away_team"] == target_team)
    ].reset_index()

    df_saints
    return df_saints, target_team


@app.cell
def _(df_saints, np, target_team):
    df_saints['home_away_flag'] = np.where(
        df_saints['home_team'] == target_team,
        'H',
        'A'
    )

    points_condition = [
        (df_saints['home_away_flag'] == 'H') & (df_saints['home_goals_ft'] > df_saints['away_goals_ft']),
        (df_saints['home_away_flag'] == 'H') & (df_saints['home_goals_ft'] < df_saints['away_goals_ft']),
        (df_saints['home_away_flag'] == 'A') & (df_saints['away_goals_ft'] > df_saints['home_goals_ft']),
        (df_saints['home_away_flag'] == 'A') & (df_saints['away_goals_ft'] < df_saints['home_goals_ft']),
    ]

    points_map = [
        3,
        0,
        3,
        0
    ]

    df_saints['points'] = np.select(
        points_condition,
        points_map,
        default=1
    )

    df_saints
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
