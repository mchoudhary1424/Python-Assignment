import tkinter as tk
import requests

def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city name.")
        return
    
    try:
        # Fetching simple text-based weather data
        url = f"https://wttr.in/{city}?format=%C+%t\nHumidity:+%h\nWind:+%w"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200 and "Unknown location" not in response.text:
            result_label.config(text=f"Location: {city.title()}\n\n{response.text}")
        else:
            result_label.config(text="Error: City not found.")
            
    except Exception:
        result_label.config(text="Connection Error: Could not reach server.")

# GUI Window Setup
app = tk.Tk()
app.title("Weather App")
app.geometry("350x250")

# Widgets
label = tk.Label(app, text="Enter City Name:", font=("Arial", 11, "bold"))
label.pack(pady=10)

city_entry = tk.Entry(app, font=("Arial", 12), width=20, justify="center")
city_entry.pack(pady=5)

search_btn = tk.Button(app, text="Get Weather", font=("Arial", 10), command=fetch_weather)
search_btn.pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

app.mainloop()
