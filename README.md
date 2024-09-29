# Fitness-Plotter

Small project to plot fitness activities (currently Garmin) onto an interactive map

## Installation

1. Make sure you have a local python installation
2. Download the repository from Github and extract all
3. Install fitness-plotter locally by navigating to the directory in terminal and typing `pip install .`

## Getting your Garmin data
1. Bulk download your garmin activity data, this can be requested from [garmin](https://www.garmin.com/en-US/account/datamanagement/exportdata/)
2. Extract/unzip the data and locate the `UploadedFiles_0-_Part1.zip` file, for my device and at time of writing it was in `DI_CONNECT/DI-Connect-Uploaded-Files`
3. Extract/unzip the `UploadedFiles_0-_Part1.zip` file, this is where the activity data is stored

## Usage
1. Use the `plot_all` command to plot all activities on a single map and save it as an html file
   1. `-d` is used to point to the directory with your .fit files in , e.g. `plot_all -d "home/documents/my_garmin/UploadedFiles_0-_Part1.zip"`
   2. `-o` is optional for giving the output file a new name or destination, e.g. `plot_all -d "/home/documents/my_garmin/UploadedFiles_0-_Part1.zip" -o "my_map_1.html"`, default is `map.html` saved to the current working directory
 

## Contributing and Feedback

Please raise any issues you find on the github issues page, any feedback is very welcome.

If you want to contribute feel free to fork the repository and request a merge with your changes. 

**This code is only tested with a forerunner 45, if you have another device and it does not work feel free to raise an issue**

Finally if you want to run this code but struggle with any of the steps you can reach out either through the issues or my email found in the pyproject.toml file.