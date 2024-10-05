import argparse
import folium
from tqdm import tqdm
from glob import glob
from pathlib import Path
from fitness_plotter.garmin.fit_file import FitFile

def get_args():
    parser = argparse.ArgumentParser(description="Plot all activities in a directory")
    parser.add_argument("-d", "--directory", type=str, help="Directory containing .fit files")
    parser.add_argument("-o", "--output", type=str, help="Output file name, should be an html file (default: 'map.html')", default="map.html")
    return parser.parse_args()

def plot_all():
    args = get_args()
    m = folium.Map()
    fit_files = glob(str(Path(args.directory + "/*.fit")))

    if len(fit_files) == 0:
        raise ValueError(f"No .fit files found in {args.directory}")
    for fit_file in tqdm(fit_files):
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
    print(f"{len(fit_files)} files saved to {args.output}")

if __name__ == "__main__":
    plot_all()