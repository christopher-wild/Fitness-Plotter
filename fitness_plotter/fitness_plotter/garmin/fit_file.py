from pathlib import Path
from garmin_fit_sdk import Decoder, Stream 
import logging
class FitFile:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        stream = Stream.from_file(self.file_path)
        self.messages = Decoder(stream).read()[0]

    @property
    def polyline(self):
        polyline = []
        try: 
            for record in self.messages['record_mesgs']:
                try:
                    polyline.append([record['position_lat'] * (180 / 2**31), record['position_long'] * (180 / 2**31)]) # Convert garmin's 32-bit lat/long to decimal
                except KeyError: # Not all messages have position data
                    pass
            return polyline
        except KeyError:
            logging.info(f"No activity messages in {self.file_path}")
        

    @property
    def sport(self):
        try:
            sport = self.messages['sport_mesgs'][0]['sport']
        except KeyError:
            sport = ''
        return sport
