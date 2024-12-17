import pandas as pd
from collections import Counter

INPUT_FILE_NAME = "input_rosters/roster_test_1.txt"
OUTPUT_FILE_NAME = "output_rosters/rosters_test_1.txt"

# changed "HBP" -> "HBP_hitter" and "HBP_pitcher" to avoid dupes
RAW_COLUMNS_STRING = "id, del, team_id, Team Name, League Name, LastName, FirstName, NickName, UniformNumber, DayOB, MonthOB, YearOB, NationalityID, Nation, CityID, City, facial_type, Height (cm), Weight (kg), Bats, Throws, Position, ML Service, 40 man roster service, pro years, options used, Contact vL, Gap vL, Power vL, Eye vL, Avoid K vL, BABIP vL, Contract Vr, Gap Vr, Power vR, Eye vR, Ks vR, BABIP vR, Contact Pot, Gap Pot, Power Pot, Eye Pot, Ks Pot, BABIP Pot, HBP_hitter, GB Batter type, FB Batter type, speed, steal rate, steal, running, sac bunt, bunt hit,Move vL, Control vL, Movement vR, Control vR, Move Pot, Control Pot, HBP_pitcher, WP, Balk, Stamina, Hold, GB%, Velocity, ArmSlot, Infield Range, Infield Error, Infield Arm, DP, CatcherAbil, Catcher Arm, OF Range, OF Error, OF Arm, PExp, CExp, 1bExp, 2bExp, 3bExp, ssExp, LFExp, CFExp, RFExp, use expected, expected level, expected ab, expected avg, expected 2b, expected 3b, expected hr, expected bb, expected k, expected hbp, contract y1, contract y2, contract y3, contract y4, contract y5, contract y6, contract y7, contract y8, contract y9, contract y10, contract current year (0 = first year), extension y1, extension y2, extension y3, extension y4, extension y5, extension y6, extension y7, extension y8, extension y9, extension y10, greed, loyalty, play_for_winner, work_ethic, intelligence, leader ability, Stuff Overall, Stuff R/L split, Stuff Pot., Fastball (scale: 0-5), Slider, Curveball, Changeup, Cutter, Sinker, Splitter, Forkball, Screwball, Circlechange, Knucklecurve, Knuckleball, Fastball Pot.(scale: 0-5), Slider Pot., Curveball Pot., Changeup Pot., Cutter Pot., Sinker Pot., Splitter Pot., Forkball Pot., Screwball Pot., Circlechange Pot., Knucklecurve Pot., Knuckleball Pot., Hitter 3B/2B ratio, pbabip, lahman_id, bbref_id, bbrefminors_id, twitter_handle, Catcher Framing"
COLUMNS = [block.strip() for block in RAW_COLUMNS_STRING.split(",")]

# Default major league is Major League Baseball
MAJOR_LEAGUE_NAME = "Major League Baseball"


id2name = {} # Map (unique) team ID to team name
id2league = {} # Map (unique) team ID to league name
ml_name2id = {} # Map major league team name to (unique) team ID
ml_affils = {} # Map major league team (unique) ID to list of minor league affiliate team IDs


def parse_teams(df: pd.DataFrame) -> None:
    """
    Parses the teams of the roster file and populates the dictionaries for use

    Args:
        df (DataFame): The loaded roster dataframe
    """

    # First part of file is major league IDs
    # Iterate until we read "//" to indicate end
    with open(INPUT_FILE_NAME) as f:
        next(f) # Skip first header line
        for line in f:
            line = line[:-1]
            if line == "//": break
            line = line[2:].split(" ")
            team_id = int(line[0])
            team_name = ' '.join(line[4:])
            
            id2name[team_id] = team_name
            id2league[team_id] = MAJOR_LEAGUE_NAME
            ml_name2id[team_name] = team_id
            ml_affils[team_id] = []
        
    # Iterate through df to find minor-league affiliates


if __name__ == "__main__":
    df = pd.read_csv(INPUT_FILE_NAME, sep=',', names=COLUMNS, comment='/', index_col=False)
    parse_teams(df)
    df.to_csv(OUTPUT_FILE_NAME, sep=',', index=False, header=False)
