import sys
import tkinter
import tkinter.messagebox
from tkintermapview import TkinterMapView


class App(tkinter.Tk):

    APP_NAME = "DJI sniffer"
    WIDTH = 1500
    HEIGHT = 700

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title(self.APP_NAME)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Set the map
        self.map_widget = TkinterMapView(width=self.WIDTH, height=self.HEIGHT, corner_radius=0)
        self.map_widget.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
        # List of the markers (drones)
        self.marker_list = []

    # Add a new marker (drone)
    def save_marker(self,marker):
        self.marker_list.append(marker)

    # Clear the marker list
    def clear_marker_list(self):
        for m in self.marker_list:
            m.delete()
        self.marker_list.clear()

    # To display the map
    def start(self):
        self.mainloop()