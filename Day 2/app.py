import json

# Read the JSON data from the file
with open('example.json', 'r') as file:
    json_data = json.load(file)

# Find the donut with name "Old Fashioned"
for ex5 in json_data:
    if ex5['name'] == 'Old Fashioned':
        # Add a new batter named "Coffee"
        ex5['batters']['batter'].append({'id': str(int(ex5['batters']['batter'][-1]['id']) + 1), 'type': 'Coffee'})
        break  # Stop iterating since we found the donut

# Write the updated data back to the file
with open('example.json', 'w') as file:
    json.dump(json_data, file, indent=4)
