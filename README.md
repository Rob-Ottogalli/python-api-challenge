# python-api-challenge
Repository for Python API Weather and Vacation Challenge

To view the data in this repository:

1. Open "start_code" folder and run "WeatherPy_Rob Ottogalli.ipynb" directly.
2. Run all cells from top to bottom to display the chart outputs.
3. Follow the Markdown instructions and the code comments to review what each cell executes.
4. After running WeatherPy, run "VacationPy_Rob Ottogalli.ipynb".
5. Run all cells from top to bottom to display the chart outputs.
6. Follow the Markdown instructions and the code comments to review what each cell executes.
7. The maps that generate can be viewed in full screen and have zooming available, as with regular Google Maps.

Notes on WeatherPy:
1. To view the CSV that generates when running this code, open the "Output" folder, and open "CityWeatherData.csv".
2. To view the scatter plot figures, open the "Output" folder, and navigate to the "Figures" folder to find all scatter plots in PNG format.

Notes on VacationPy:
1. In order to run, VacationPy uses a dataframe of cities output when running the WeatherPy code. WeatherPy must run completely in order for VacationPy to run on the data most recently collected in WeatherPy.
2. VacationPy runs dependently on data collected by WeatherPy, and filters out cities that meet certain ideal weather conditions. Within those weather conditions, VacationPy then searches for hotels within a 5000-meter radius of those cities. However, there is a possibility that no cities will be found. If this occurs, you will need to re-run WeatherPy, allow it to run completely, and then re-run VacationPy from the beginning. 