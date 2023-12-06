import pandas as pd
import requests

# Dictionary to map state names to two-letter abbreviations
state_abbreviations = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

def get_zipcode(city, state_full):
    # Convert full state name to abbreviation
    state = state_abbreviations.get(state_full)
    if not state:
        print(f"No abbreviation found for state: {state_full}")
        return None

    response = requests.get(f"http://api.zippopotam.us/us/{state}/{city}")
    if response.status_code == 200:
        data = response.json()             
        zipcode = data['places'][0]['post code']
        return zipcode
    else:
        zipcode = "N/A"    
        return zipcode

# Load your CSV file
df = pd.read_csv('crimes_by_state.csv')  # Replace with your file's path

# Apply the get_zipcode function to each row in the DataFrame
df['zipcode'] = df.apply(lambda row: get_zipcode(row['city'], row['state']), axis=1)

# Save the updated DataFrame back to a CSV
df.to_csv('updated_file.csv', index=False)  # Replace with your desired output file's path
