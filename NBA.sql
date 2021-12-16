Drop Table if exists Player;
Drop Table if exists Schedule;
Drop Table if exists Support_Staff;
Drop Table if exists Manager;
Drop Table if exists Coach;
Drop Table if exists Dietician;
Drop Table if exists Physiotherapist;
Drop Table if exists Team;
Drop Table if exists Matches;
Drop Table if exists has_match_stats;
Drop Table if exists plays;
Drop Table if exists updates;
Drop Table if exists Check_up;
Drop Table if exists goes_for;
Drop Table if exists coaches;

CREATE TABLE Player
(
  player_id INT NOT NULL,
  player_name VARCHAR(1000) NOT NULL,
  age INT NOT NULL,
  date_of_birth DATE NOT NULL,
  pos VARCHAR(100) NOT NULL,
  height FLOAT NOT NULL,
  weight FLOAT NOT NULL,
  status VARCHAR(20) NOT NULL,
  PRIMARY KEY (player_id)
);

CREATE TABLE Schedule
(
  schedule_id INT NOT NULL,
  practice_date DATE NOT NULL,
  practice_day CHAR NOT NULL,
  practice_time VARCHAR(5) NOT NULL,
  no_of_hours INT NOT NULL,
  session_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (schedule_id)
);

CREATE TABLE Support_Staff
(
  support_id VARCHAR(10) NOT NULL,
  support_name VARCHAR(1000) NOT NULL,
  employment_status VARCHAR(100) NOT NULL,
  PRIMARY KEY (support_id)
);

CREATE TABLE Manager
(
  support_id VARCHAR(10) NOT NULL,
  PRIMARY KEY (support_id),
  FOREIGN KEY (support_id) REFERENCES Support_Staff(support_id)
  on delete cascade
);

CREATE TABLE Coach
(
  start_year INT NOT NULL,
  support_id VARCHAR(10) NOT NULL,
  PRIMARY KEY (support_id),
  FOREIGN KEY (support_id) REFERENCES Support_Staff(support_id)
  on delete cascade
);

CREATE TABLE Dietician
(
  avail_date DATE NOT NULL,
  support_id VARCHAR(10) NOT NULL,
  PRIMARY KEY (support_id),
  FOREIGN KEY (support_id) REFERENCES Support_Staff(support_id)
  on delete cascade
);

CREATE TABLE Physiotherapist
(
  available_dates DATE NOT NULL,
  support_id VARCHAR(10) NOT NULL,
  PRIMARY KEY (support_id),
  FOREIGN KEY (support_id) REFERENCES Support_Staff(support_id)
  on delete cascade
);

CREATE TABLE Team
(
  team_id INT NOT NULL,
  team_name VARCHAR(100) NOT NULL,
  year INT NOT NULL,
  player_id INT NOT NULL,
  PRIMARY KEY (team_id, year),
  FOREIGN KEY (player_id) REFERENCES Player(player_id)
  on delete cascade
);

CREATE TABLE Matches
(
  match_id INT NOT NULL,
  match_date DATE,
  home_points INT,
  away_points INT,
  season INT,
  opponent_team VARCHAR(1000),
  city VARCHAR(100),
  arena VARCHAR(100),
  home_fg_per FLOAT,
  away_fg_per FLOAT,
  home_ft_per FLOAT,
  away_ft_per FLOAT,
  home_3_per FLOAT,
  away_3_per FLOAT,
  home_assists INT,
  away_assists INT,
  home_rebounds INT,
  away_rebounds INT,
  home_wins INT,
  PRIMARY KEY (match_id)
);

CREATE TABLE plays
(
  match_id INT NOT NULL,
  team_id INT NOT NULL,
  year INT NOT NULL,
  PRIMARY KEY (match_id),
  FOREIGN KEY (match_id) REFERENCES Matches(match_id)
  on delete cascade,
  FOREIGN KEY (team_id, year) REFERENCES Team(team_id, year)
  on delete cascade
);

CREATE TABLE has_match_stats
(
  FGM INT,
  FGA INT,
  FG_percent DECIMAL(5,3),
  FG3M INT,
  FG3A INT,
  FG3_percent DECIMAL(5,3),
  FTM INT,
  FTA INT,
  FT_percent DECIMAL(5,3),
  Offensive_rebound INT,
  Defensive_rebounds INT,
  rebounds INT,
  assists INT,
  steals INT,
  blocked_shots INT,
  turnovers INT,
  personal_fouls INT,
  points_scored INT,
  player_id INT NOT NULL,
  match_id INT NOT NULL,
  PRIMARY KEY (player_id, match_id),
  FOREIGN KEY (player_id) REFERENCES Player(player_id)
  on delete cascade,
  FOREIGN KEY (match_id) REFERENCES Matches(match_id)
  on delete cascade
);

CREATE TABLE updates
(
  schedule_id INT NOT NULL,
  support_id VARCHAR(10) NOT NULL,
  PRIMARY KEY (schedule_id, support_id),
  FOREIGN KEY (schedule_id) REFERENCES Schedule(schedule_id)
  on delete cascade,
  FOREIGN KEY (support_id) REFERENCES Coach(support_id)
  on delete cascade
);

CREATE TABLE coaches
(
  support_id VARCHAR(10) NOT NULL,
  team_id INT NOT NULL,
  year INT NOT NULL,
  PRIMARY KEY (team_id, year, support_id),
  FOREIGN KEY (support_id) REFERENCES Coach(support_id)
  on delete cascade
);

CREATE TABLE Contract
(
  start_year INT NOT NULL,
  end_year INT NOT NULL,
  fa_year INT NOT NULL,
  salary INT NOT NULL,
  aav INT NOT NULL,
  player_id INT NOT NULL,
  approval_status VARCHAR(20) NOT NULL,
  support_id VARCHAR(10) NOT NULL,
  PRIMARY KEY (start_year, player_id),
  FOREIGN KEY (player_id) REFERENCES Player(player_id)
  on delete cascade,
  FOREIGN KEY (support_id) REFERENCES Manager(support_id)
  on delete cascade
);

CREATE TABLE Check_up
(
  check_up_date DATE NOT NULL,
  bp INT,
  cholestrol INT,
  bpm INT,
  oxygen INT,
  injuries VARCHAR(100),
  support_id_p VARCHAR(10) NOT NULL,
  support_id_d VARCHAR(10) NOT NULL,
  PRIMARY KEY (check_up_date),
  FOREIGN KEY (support_id_p) REFERENCES Physiotherapist(support_id)
  on delete cascade,
  FOREIGN KEY (support_id_d) REFERENCES Dietician(support_id)
  on delete cascade
);

CREATE TABLE goes_for
(
  check_up_date DATE NOT NULL,
  player_id INT NOT NULL,
  PRIMARY KEY (check_up_date, player_id),
  FOREIGN KEY (check_up_date) REFERENCES Check_up(check_up_date)
  on delete cascade,
  FOREIGN KEY (player_id) REFERENCES Player(player_id)
  on delete cascade
);
