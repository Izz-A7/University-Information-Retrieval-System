# University-Information-Retrieval-System
This project is a Python script that retrieves information about universities based on user input. The script reads data from two CSV files, one containing information about top universities worldwide and the other containing information about capital cities around the world. The script allows users to input a country name and retrieve information about universities in that country.

## Skills Learned
- Reading data from CSV files
- Parsing and manipulating data
- Creating and using functions
- Writing to files
- Error handling

## Usage
To use this script, simply run the getInformation function with the desired country name and the paths to the university and capital CSV files. The script will create an output file called output.txt with information about the universities in the selected country.

## Constants
The script defines several constants at the beginning of the file.

## Functions
The script includes several functions, including:

- categorizeTopUni: Parses data from the top university CSV file and returns it as separate lists.
- categorizeCapitals: Parses data from the capital CSV file and returns it as separate lists.
- countUni: Counts the number of universities in the top university CSV file.
- availCountriesContinents: Returns a list of available countries and continents based on the data in the two CSV files.
- info: Retrieves information about universities in a selected country.
- capitalInfo: Retrieves information about the capital city of a selected country and universities in that city.

## Limitations
This script is a basic simulation of a university information retrieval system and does not include many of the features of a real system. Additionally, the script has limited error handling and may crash if the user inputs invalid data.

## Possible Improvements
Adding more features, such as searching for universities by name or field of study
Improving the error handling to prevent crashes from invalid data
Enhancing the user interface to make it more user-friendly

## Conclusion
This project taught me valuable skills in data manipulation and parsing, as well as how to read from and write to CSV files. I also gained experience in creating functions and error handling. Overall, this project helped me develop my skills as a Python programmer and gave me a solid foundation for future projects.
