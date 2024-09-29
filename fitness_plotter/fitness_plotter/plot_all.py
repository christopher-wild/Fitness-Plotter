import argparse
import folium
from glob import glob
from pathlib import Path
from fitness_plotter.garmin.fit_file import FitFile

def get_args():
    parser = argparse.ArgumentParser(description="Plot all activities in a directory")
    parser.add_argument("-d", "--directory", type=str, help="Directory containing .fit files")
    parser.add_argument("-o", "--output", type=str, help="Output file name, should be an html file (default: 'map.html')", default="map.html")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    m = folium.Map()

    for fit_file in glob(str(Path(args.directory + "/*.fit"))):
        fit = FitFile(fit_file)
        sport = fit.sport
        if sport == 'running':
            color = 'blue'
        elif sport == 'cycling':
            color = 'red'
        elif sport == 'swimming':
            color = 'green'
        else:
            color = 'black'
        if polyline := fit.polyline:
            folium.PolyLine(polyline, color=color, opacity=0.4).add_to(m)
        
    m.save(Path(args.output))