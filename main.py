from tkinter import *
import requests
import json

# sending HTTP 'get' request to pokeapi to retrieve data
api_url = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(api_url)
print(response.json())
print(response.status_code)

# setting up window for UI
window = Tk()
window.title("Pokedex")
window.geometry(newGeometry = "400x400")
window["bg"] = "yellow"
search_bar = Entry(window, text = "", bg = "white", fg = "black", bd = 2)
search_bar.place(x = int(window.winfo_screenmmwidth()) / 2, y = int(window.winfo_screenmmheight()) / 2)
print(search_bar.winfo_rootx())
print(search_bar.winfo_rooty())
search_button = Button(window, text = "Search", fg = "red")
search_button.place(x = (int(window.winfo_screenmmwidth()) / 2) + 35, y = int(search_bar.winfo_rooty() + 150))
window.mainloop()