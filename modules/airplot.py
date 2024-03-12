from airData import currentAirData
import matplotlib.pyplot as plt

def visualize_air_quality(data):
    labels = ['PM2.5', 'PM10', 'O3', 'NO2', 'SO2', 'CO']
    values = [data['pm25'], data['pm10'], data['o3'], data['no2'], data['so2'], data['co']]

    # Bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=['blue', 'green', 'orange', 'red', 'purple', 'brown'])
    plt.title('Air Quality Components')
    plt.xlabel('Air Quality Components')
    plt.ylabel('Concentration (µg/m³ or ppm)')
    plt.show()

# Example usage
check = currentAirData(11.635250, 78.148880)

if check['success']:
    visualize_air_quality(check)
else:
    print("Failed to fetch air quality data.")
