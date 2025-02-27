from tkinter import *
from ttkwidgets import TimeLine
from datetime import datetime
import webbrowser

class UserView:
    def __init__(self):
        pass
    def setController(self, controller):
        self.controller = controller
        self.root = Tk()

    def run(self):
        self.asteroids = self.controller.fetchData()
        width=1400
        Label(self.root, text=f"Asteroids today: {datetime.now().date()}", font=("Arial", 18)).grid(row=0, column=0, pady=10)
        Label(self.root, text='Right-click on asteroids to display information', font=("Arial", 14)).grid(row=1, column=0, pady=10)
        timeline = TimeLine(
            self.root,
            categories={"1":{"text": "Asteroids"}},
            height=10,
            width=width,
            extend=True,
            start=0.0,
            finish=24.0,
            resolution= 24/width,
            unit='h',
            zoom_enabled=False
        )
        Label(self.root, text="Asteroid Information", font=("Arial", 14)).grid(row=3, column=0, pady=20)
        nameLabel = Label(self.root, text="", font=("Arial", 10))
        nameLabel.grid(row=4, column=0, pady=5)
        timeLabel = Label(self.root, text="", font=("Arial", 10))
        timeLabel.grid(row=5, column=0, pady=5)
        diameterLabel = Label(self.root, text="", font=("Arial", 10))
        diameterLabel.grid(row=6, column=0, pady=5)
        velocityLabel = Label(self.root, text="", font=("Arial", 10))
        velocityLabel.grid(row=7, column=0, pady=5)
        distanceLabel = Label(self.root, text="", font=("Arial", 10))
        distanceLabel.grid(row=8, column=0, pady=5)
        linkLabel = Label(self.root, text="", font=("Arial", 10))
        linkLabel.grid(row=9, column=0, pady=5)
        for id, asteroid in enumerate(self.asteroids):
            timeline.tag_configure(str(id), right_callback=lambda *args, ida=id: self.update_information(ida, nameLabel, timeLabel, diameterLabel, velocityLabel, distanceLabel, linkLabel))
            time = self.time_to_float(str(asteroid['time']))
            timeline.create_marker("1", time, time+0.21, background="white", text='O', move=False, tags=(str(id),))
        timeline.draw_timeline()
        timeline.grid(row=2, column=0, padx=10, pady=10)
        self.root.geometry("1500x1080")
        self.root.mainloop()
        
    def callback(self, url):
        webbrowser.open_new_tab(url)
    
    def time_to_float(self, time_str):
        h, m = time_str.split(':')
        return int(h) + int(m) / 60
    
    def update_information(self, id, nameLabel, timeLabel, diameterLabel, velocityLabel, distanceLabel, linkLabel):
        nameLabel.config(text=f"name: {self.asteroids[id]['name']}")
        timeLabel.config(text=f"time: {self.asteroids[id]['time']}")
        diameterLabel.config(text=f"diameter: {self.asteroids[id]['diamter_m']}m")
        velocityLabel.config(text=f"velocity: {self.asteroids[id]['velocity_kms']}km/s")
        distanceLabel.config(text=f"distance: {self.asteroids[id]['distance_km']}km")
        linkLabel.config(text=f"link: {self.asteroids[id]['link']}", cursor="hand2")
        linkLabel.bind("<Button-1>", lambda e: self.callback(self.asteroids[id]['link']))
        if(self.asteroids[id]['hazardous']):
            nameLabel.config(fg='#f00')
        else:
            nameLabel.config(fg='#000')

