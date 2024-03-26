import requests
import csv
from datetime import datetime

# API endpoint URL
api_url = "https://danepubliczne.imgw.pl/api/data/synop/station/krakow"

# Function to fetch data from the API
def fetch_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to save data to the CSV file
def save_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['timestamp', 'id_stacji', 'stacja', 'data_pomiaru', 'godzina_pomiaru', 'temperatura',
                      'predkosc_wiatru', 'kierunek_wiatru', 'wilgotnosc_wzgledna',
                      'suma_opadu', 'cisnienie']  # Replace with actual field names
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file is empty, write the header
        if csvfile.tell() == 0:
            writer.writeheader()

            # Convert numeric values to floats
        for key, value in data.items():
            if key.startswith('value'):
                data[key] = float(value)

        # Write the data
        writer.writerow(data)

# Main script
if __name__ == "__main__":
    # Generate a timestamp for the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Fetch data from the API
    api_data = fetch_data()

    if api_data:
        # Add the timestamp to the data
        api_data['timestamp'] = timestamp

        # Save data to the CSV file
        save_to_csv(api_data, '/PiServer/Weather_Krakow.csv')  # Replace XXX with the actual drive letter

        print("Data saved successfully.")
    else:
        print("Failed to fetch data. Exiting.")
