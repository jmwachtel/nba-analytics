# PostgreSQL Tables

## Tables 
Create each of the tables in the PostgreSQL database.

### NBA Traditional Statistics
CREATE TABLE nba_traditional(
    date varchar NOT NULL,
    team varchar NOT NULL,
    gp int4,
    win int4,
    loss int4,
    w_pct float4,
    mins float4,
    pts float4,
    fgm float4,
    fga float4,
    fg_pct float4,
    fg3m float4,
    fg3a float4,
    fg3_pct float4,
    ftm float4,
    fta float4,
    ft_pct float4,
    oreb float4,
    dreb float4,
    reb float4,
    ast float4,
    tov float4,
    stl float4,
    blk float4,
    blka float4,
    pf float4,
    pfd float4,
    p_m float4
);

### NBA Advanced Statistics
CREATE TABLE nba_advanced(
    date varchar NOT NULL,
    team varchar NOT NULL,
    offrtg float4,
    defrtg float4,
    netrtg float4,
    ast_pct float4,
    ast_v_tov float4,
    ast_ratio float4,
    oreb_pct float4,
    dreb_pct float4,
    reb_pct float4,
    tov_pct float4,
    efg_pct float4,
    ts_pct float4,
    pace float4,
    pie float4,
    poss int4
);


### NBA Four Factors Statistics
CREATE TABLE nba_four_factors(
    date varchar NOT NULL,
    team varchar NOT NULL,
    fta_rate float4,
    opp_efg_pct float4,
    opp_fta_rate float4,
    opp_tov_pct float4,
    opp_oreb_pct float4
);

### NBA Miscellaneous Statistics
CREATE TABLE nba_misc(
    date varchar NOT NULL,
    team varchar NOT NULL,
    pts_off_tov float4,
    second_pts float4,
    fbps float4,
    pitp float4,
    opp_pts_off_tov float4,
    opp_second_pts float4,
    opp_fbps float4,
    opp_pitp float4
);

### NBA Scoring Statistics
CREATE TABLE nba_scoring(
    date varchar NOT NULL,
    team varchar NOT NULL,
    pct_fga_2pt float4,
    pct_fga_3pt float4,
    pct_pts_2pt float4,
    pct_pts_2pt_mid float4,
    pct_pts_3pt float4,
    pct_pts_fbps float4,
    pct_pts_ft float4,
    pct_pts_off_tov float4,
    pct_pts_pitp float4,
    pct_ast_2fgm float4,
    pct_uast_2fgm float4,
    pct_ast_3fgm float4,
    pct_uast_3fgm float4,
    pct_ast_fgm float4,
    pct_uast_fgm float4
);

### NBA Opponent Statistics
CREATE TABLE nba_opponent(
    date varchar NOT NULL,
    team varchar NOT NULL,
    opp_fgm float4,
    opp_fga float4,
    opp_fg_pct float4,
    opp_3pm float4,
    opp_3pa float4,
    opp_3pt_pct float4,
    opp_ftm float4,
    opp_fta float4,
    opp_ft_pct float4,
    opp_oreb float4,
    opp_dreb float4,
    opp_reb float4,
    opp_ast float4,
    opp_tov float4,
    opp_stl float4,
    opp_blk float4,
    opp_blka float4,
    opp_pf float4,
    opp_pfd float4,
    opp_pts float4,
    opp_pm float4
);

### NBA Speed and Distance Statistics
CREATE TABLE nba_speed_distance(
    date varchar NOT NULL,
    team varchar NOT NULL,
    dist_feet float4,
    dist_miles float4,
    dist_miles_off float4,
    dist_miles_def float4,
    avg_speed float4,
    avg_speed_off float4,
    avg_speed_def float4
);

### NBA Shooting Statistics
CREATE TABLE nba_shooting(
    date varchar NOT NULL,
    team varchar NOT NULL,
    fgm_ra float4,
    fga_ra float4,
    fg_pct_ra float4,
    fgm_paint float4,
    fga_paint float4,
    fg_pct_paint float4,
    fgm_mr float4,
    fga_mr float4,
    fg_pct_mr float4,
    fgm_lc3 float4,
    fga_lc3 float4,
    fg_pct_lc3 float4,
    fgm_rc3 float4,
    fga_rc3 float4,
    fg_pct_rc3 float4,
    fgm_c3 float4,
    fga_c3 float4,
    fg_pct_c3 float4,
    fgm_atb3 float4,
    fga_atb3 float4,
    fg_pct_atb3 float4
);

### NBA Opponent Shooting Statistics
CREATE TABLE nba_opponent_shooting(
    date varchar NOT NULL,
    team varchar NOT NULL,
    opp_fgm_ra float4,
    opp_fga_ra float4,
    opp_fg_pct_ra float4,
    opp_fgm_paint float4,
    opp_fga_paint float4,
    opp_fg_pct_paint float4,
    opp_fgm_mr float4,
    opp_fga_mr float4,
    opp_fg_pct_mr float4,
    opp_fgm_lc3 float4,
    opp_fga_lc3 float4,
    opp_fg_pct_lc3 float4,
    opp_fgm_rc3 float4,
    opp_fga_rc3 float4,
    opp_fg_pct_rc3 float4,
    opp_fgm_c3 float4,
    opp_fga_c3 float4,
    opp_fg_pct_c3 float4,
    opp_fgm_atb3 float4,
    opp_fga_atb3 float4,
    opp_fg_pct_atb3 float4
);

### NBA Hustle Statistics
CREATE TABLE nba_hustle(
    date varchar NOT NULL,
    team varchar NOT NULL,
    screen_ast float4,
    screen_ast_pts float4,
    deflections float4,
    off_loose_ball_rec float4,
    def_loose_ball_rec float4,
    loose_ball_rec float4,
    pct_loose_ball_rec_off float4,
    pct_loose_ball_rec_def float4,
    charges_drawn float4,
    contested_2pt float4,
    contested_3pt float4,
    contested_shots float4
);

### Covers
CREATE TABLE covers (
    id_num int4 unique,
    date varchar NOT NULL,
    time varchar,
    team varchar NOT NULL,
    opponent varchar,
    opponent_score int4,
    score int4,
    result varchar,
    is_home bool,
    spread float4,
    spread_result varchar,
    fanduel_line_away int4,
    fanduel_line_price_away varchar,
    fanduel_line_home int4,
    fanduel_line_price_home varchar,
    draftkings_line_away int4,
    draftkings_line_price_away varchar,
    draftkings_line_home varchar,
    draftkings_line_price_home varchar,
    covers_away_consensus varchar,
    covers_home_consensus varchar,
    game_url varchar,
    league_year varchar
);

### Basketball Reference Standings
CREATE TABLE dfc_br_standings (
    team varchar NOT NULL,
    date varchar NOT NULL,
    wins int4,
    losses int4,
    win_perc float4,
    points_scored_per_game float4,
    points_allowed_per_game float4,
    expected_wins float4,
    expected_losses float4
);

### Basketball Reference Team Stats
CREATE TABLE dfc_br_team_stats (
    team varchar NOT NULL,
    date varchar NOT NULL,
    g int4,
    mp int4,
    fg int4,
    fga int4,
    fg_pct float4,
    fg3 int4,
    fg3a int4,
    fg3_pct float4,
    fg2 int4,
    fg2a int4,
    fg2_pct float4,
    ft int4,
    fta int4,
    ft_pct float4,
    orb int4,
    drb int4,
    trb int4,
    ast int4,
    stl int4,
    blk int4,
    tov int4,
    pf int4,
    pts int4
);

### Basketball Reference Opponent Stats
CREATE TABLE dfc_br_opponent_stats (
    team varchar NOT NULL,
    date varchar NOT NULL,
    opp_g int4,
    opp_mp int4,
    opp_fg int4,
    opp_fga int4,
    opp_fg_pct float4,
    opp_fg3 int4,
    opp_fg3a int4,
    opp_fg3_pct float4,
    opp_fg2 int4,
    opp_fg2a int4,
    opp_fg2_pct float4,
    opp_ft int4,
    opp_fta int4,
    opp_ft_pct float4,
    opp_orb int4,
    opp_drb int4,
    opp_trb int4,
    opp_ast int4,
    opp_stl int4,
    opp_blk int4,
    opp_tov int4,
    opp_pf int4,
    opp_pts int4
);
