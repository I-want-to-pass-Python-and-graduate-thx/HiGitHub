import pandas as pd

# Load the CSV file with 'latin1' encoding
file_path = 'C:\\Users\\VR\\Documents\\python_code\\pe8_data.csv'
data = pd.read_csv(file_path, encoding='latin1')


# Ensure all kind of records below are strings
data['HOME'] = data['HOME'].astype(str)
data['AWAY'] = data['AWAY'].astype(str)
data['W-L'] = data['W-L'].astype(str)

# Function to convert W-L record to win percentage
def win_percentage(record):
    try:
        wins, losses = map(int, record.split('-'))
        return wins / (wins + losses)
    except ValueError:
        return None

# Clean HOME and AWAY columns
data['HOME'] = data['HOME'].apply(lambda x: x if '-' in x else None)
data['AWAY'] = data['AWAY'].apply(lambda x: x if '-' in x else None)

# 1. Eastern Conference Teams with Home Win-Loss Percentage Lower than Away Win-Loss Percentage
eastern_teams = data[data['Conference'] == 'Eastern']
eastern_teams['Home_PCT'] = eastern_teams['HOME'].apply(win_percentage)
eastern_teams['Away_PCT'] = eastern_teams['AWAY'].apply(win_percentage)
lower_home_pct_teams = eastern_teams[eastern_teams['Home_PCT'] < eastern_teams['Away_PCT']]

# 2. Conference with Higher Average Difference of "PF minus PA"
data['PF'] = pd.to_numeric(data['PF'], errors='coerce')
data['PA'] = pd.to_numeric(data['PA'], errors='coerce')
data['PF_PA_Diff'] = data['PF'] - data['PA']
conference_diff = data.groupby('Conference')['PF_PA_Diff'].mean()

# 3. Ranking Teams Based on Wins Against Other Conference's Teams
data[['CONF_Wins', 'CONF_Losses']] = data['CONF'].str.split('-').apply(lambda x: pd.Series(map(int, x)))
data['InterConf_Wins'] = data['CONF_Wins'] - data['CONF_Losses']
ranking = data.sort_values(by='InterConf_Wins', ascending=False)

# Display results
lower_home_pct_teams_result = lower_home_pct_teams[['Team', 'Home_PCT', 'Away_PCT']]
conference_diff_result = conference_diff
ranking_result = ranking[['Team', 'InterConf_Wins']]

print(lower_home_pct_teams_result)
print(conference_diff_result)
print(ranking_result.head())
