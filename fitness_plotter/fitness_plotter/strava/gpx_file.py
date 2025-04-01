from pathlib import Path

import gpxpy

class GPXFile:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        with open(self.file_path) as f:
            self.gpx = gpxpy.parse(f)

    @property
    def polyline(self):
        polyline = []
        for record in self.gpx.tracks[0].segments[0].points:
            polyline.append([record.latitude, record.longitude])
        return polyline

    @property
    def sport(self):
        return self.gpx.tracks[0].name
    
    @property
    def date(self):
        return self.gpx.time