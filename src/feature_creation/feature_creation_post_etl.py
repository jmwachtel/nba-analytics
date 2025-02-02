import datetime
import pytz
import sys
import pandas as pd
from sqlalchemy import create_engine

sys.path.append('../../')
from passkeys import RDS_ENDPOINT, RDS_PASSWORD

pd.options.display.max_columns = 100
pd.options.display.width = 0


class FeatureCreation:
    """
    Data pipeline class for transforming inbound unclean dataset
    into cleaned and fully featurized model ready dataset.
    Use this area to create new feature sets
    from new and existing data sources
    in order to add predictive and informative power to downstream models.
    """
    def __init__(self, df):
        self.inbound_df = df
        self.wdf = df.copy()

    def create_target(self):
        """
        Regression target is the Actual Home Margin of the game.

        Classification target is IF
        the Actual Home Margin of the game
        is Greater Than the Predicted Home Margin.
        """
        self.wdf.insert(
            1,
            "REG_TARGET_actual_home_margin",
            self.wdf["home_score"] - self.wdf["away_score"],
        )
        self.wdf.insert(
            1,
            "CLS_TARGET_home_margin_GT_home_spread",
            (self.wdf["home_score"] - self.wdf["away_score"]) >
            -self.wdf["home_spread"],
        )

    def create_base_feature_set(self):
        """
        Model prep for original data sources including:
        - Historic team and odds data from Covers
        - Live team and odds data from Covers
        - Point in time standings and team/opponent stats
          from NBA Stats
        """

        team_abbrv_dict = {
            "ATL": 1,
            "BKN": 2,
            "BOS": 3,
            "CHA": 4,
            "CHI": 5,
            "CLE": 6,
            "DAL": 7,
            "DEN": 8,
            "DET": 9,
            "GSW": 10,
            "HOU": 11,
            "IND": 12,
            "LAC": 13,
            "LAL": 14,
            "MEM": 15,
            "MIA": 16,
            "MIL": 17,
            "MIN": 18,
            "NOP": 19,
            "NYK": 20,
            "OKC": 21,
            "ORL": 22,
            "PHI": 23,
            "PHX": 24,
            "POR": 25,
            "SAS": 26,
            "SAC": 27,
            "TOR": 28,
            "UTA": 29,
            "WAS": 30,
        }
        self.wdf.insert(
            3,
            "home_team_num",
            [
                team_abbrv_dict[x] if isinstance(x, str) else 0
                for x in self.wdf["home_team"]
            ],
        )
        self.wdf.insert(
            4,
            "away_team_num",
            [
                team_abbrv_dict[x] if isinstance(x, str) else 0
                for x in self.wdf["away_team"]
            ],
        )
        self.wdf.insert(
            5,
            "league_year_end",
            [
                int(x[-2:]) if isinstance(x, str) else 0
                for x in self.wdf["league_year"]
            ],
        )

        self.wdf.insert(6, "fd_line_home", self.wdf.pop("fd_line_home"))
        self.wdf.insert(7, "dk_line_home", self.wdf.pop("dk_line_home"))
        self.wdf.insert(8, "covers_consensus_home",
                        self.wdf.pop("covers_consensus_home"))

    def seasonal_effects(self):
        seasons = {
            "2023": {
                "abbrv": "2022-23",
                "start": "October 18, 2022",
                "end": "April 10, 2023",
            },
            "2022": {
                "abbrv": "2021-22",
                "start": "October 19, 2021",
                "end": "April 10, 2022",
            },
            "2021": {
                "abbrv": "2020-21",
                "start": "December 22, 2020",
                "end": "May 16, 2021",
            },
            "2020": {
                "abbrv": "2019-20",
                "start": "October 22, 2019",
                "end": "August 14, 2020",
            },
            "2019": {
                "abbrv": "2018-19",
                "start": "October 16, 2018",
                "end": "April 10, 2019",
            },
            "2018": {
                "abbrv": "2017-18",
                "start": "October 17, 2017",
                "end": "April 11, 2018",
            },
            "2017": {
                "abbrv": "2016-17",
                "start": "October 25, 2016",
                "end": "April 12, 2017",
            },
            "2016": {
                "abbrv": "2015-16",
                "start": "October 27, 2015",
                "end": "April 13, 2016",
            },
            "2015": {
                "abbrv": "2014-15",
                "start": "October 28, 2014",
                "end": "April 15, 2015",
            },
            "2014": {
                "abbrv": "2013-14",
                "start": "October 29, 2013",
                "end": "April 16, 2014",
            },
            "2013": {
                "abbrv": "2012-13",
                "start": "October 30, 2012",
                "end": "April 17, 2013",
            },
            "2012": {
                "abbrv": "2011-12",
                "start": "December 25, 2011",
                "end": "April 26, 2012",
            },
            "2011": {
                "abbrv": "2010-11",
                "start": "October 26, 2010",
                "end": "April 13, 2011",
            },
            "2010": {
                "abbrv": "2009-10",
                "start": "October 27, 2009",
                "end": "April 14, 2010",
            },
        }
        self.wdf['day_of_season'] = self.wdf.apply(
            lambda x: (x['game_date'] - pd.to_datetime(seasons[
                f'20{x["league_year_end"]}']['start'])).days,
            axis=1)

    # Define new feature set methods here.

    def finalize_data(self):
        """
        Used to implement dataset ease of use improvements like:
        - Setting Datatypes
        - Renaming Features
        - Reordering Features
        """
        always_drop_features = [
            "game_date", "home_score", "away_score", "home_result",
            "covers_game_url", "home_spread_result", "pred_date",
            "fd_line_price_home", "fd_line_price_away", "dk_line_price_home",
            "dk_line_price_away", "fd_line_away", "dk_line_away",
            "raptor1_pre", "raptor2_pre", "raptor_prob1", "raptor_prob2",
            "quality", "importance", "total_rating_538"
        ]
        self.wdf = self.wdf.drop(columns=always_drop_features)

        self.wdf = self.wdf.drop(columns=[
            "home_team",
            "away_team",
            "league_year",
            "covers_consensus_away",
        ])

        for column in list(self.wdf):
            if self.wdf[column].dtype == 'float64':
                self.wdf[column] = pd.to_numeric(self.wdf[column],
                                                 downcast='float')
            if self.wdf[column].dtype == 'int64':
                self.wdf[column] = pd.to_numeric(self.wdf[column],
                                                 downcast='integer')

    def run_all_steps(self):
        self.create_target()
        self.create_base_feature_set()
        self.seasonal_effects()
        # Add new feature set methods here.
        self.finalize_data()


if __name__ == "__main__":
    username = "postgres"
    password = RDS_PASSWORD
    endpoint = RDS_ENDPOINT
    database = "nba_betting"
    port = "5432"

    todays_datetime = datetime.datetime.now(pytz.timezone("America/Denver"))
    yesterdays_datetime = todays_datetime - datetime.timedelta(days=1)
    yesterdays_date_str = yesterdays_datetime.strftime("%Y%m%d")
    todays_date_str = todays_datetime.strftime("%Y%m%d")

    with create_engine(
            f"postgresql+psycopg2://{username}:{password}@{endpoint}/{database}"
    ).connect() as connection:

        # df = pd.read_sql_table("combined_inbound_data", connection) # Full Table. Takes Awhile

        # ----- CREATE TODAYS RECORDS -----

        dates = [todays_date_str]

        # dates = [
        #     '20221018', '20221019', '20221020', '20221021', '20221022',
        #     '20221023', '20221024', '20221025', '20221026', '20221027',
        #     '20221028'
        # ]

        for date in dates:
            record_count = pd.read_sql(
                f"SELECT COUNT(*) FROM combined_inbound_data WHERE game_id LIKE '{date}%%'",
                connection).iloc[0][0]
            if record_count > 0:
                query = f"SELECT * FROM combined_inbound_data WHERE game_id LIKE '{date}%%'"
                df = pd.read_sql(query, connection)

                feature_pipeline = FeatureCreation(df)
                feature_pipeline.run_all_steps()
                model_ready_df = feature_pipeline.wdf
                print(model_ready_df.info(verbose=True, show_counts=True))

                # model_ready_df.to_sql(
                #     "model_training_data",
                #     connection,
                #     index=False,
                #     if_exists="append")  # Replace if full table. Otherwise Append
            else:
                print(f"No Records for {date}")

        # ----- UPDATE YESTERDAYS SCORES -----

        dates = [yesterdays_date_str]

        for date in dates:
            record_count = pd.read_sql(
                f"SELECT COUNT(*) FROM combined_inbound_data WHERE game_id LIKE '{date}%%'",
                connection).iloc[0][0]
            if record_count > 0:
                query = f"SELECT * FROM combined_inbound_data WHERE game_id LIKE '{date}%%'"
                df = pd.read_sql(query, connection)

                feature_pipeline = FeatureCreation(df)
                feature_pipeline.run_all_steps()
                model_ready_df = feature_pipeline.wdf
                print(model_ready_df.info(verbose=True, show_counts=True))

                record_list_of_dicts = model_ready_df.to_dict(orient="records")

                for game_result in record_list_of_dicts:
                    game_id = game_result["game_id"]

                #     stmt = f"""
                #             DELETE FROM model_training_data
                #             WHERE game_id = '{game_id}'
                #             ;
                #             """

                #     connection.execute(stmt)

                # model_ready_df.to_sql("model_training_data",
                #                         connection,
                #                         index=False,
                #                         if_exists="append")
            else:
                print(f"No Records for {date}")
