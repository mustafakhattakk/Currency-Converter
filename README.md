Currency Converter

This is a simple currency converter program built using Python and the tkinter library for the graphical user interface. The program fetches the latest exchange rates from an API provided by Open Exchange Rates to convert currencies.

Installation

Clone the repository to your local machine
bash

git clone https://github.com/your-username/currency-converter.git


Install the required packages:

pip install tkinter requests


Get an API key from Open Exchange Rates by signing up for a free account on their website and paste it in the code where it says "app_id=" in the API_BASE_URL variable.
Usage

To run the program, simply execute the "currency_converter.py" file. A GUI window will appear with input fields for the amount to convert and the currencies to convert from and to. You can select the currencies from drop-down menus. Click the "Convert" button to initiate the currency conversion process, and the converted amount will be displayed in the result label below the input fields. The "Reset" button clears the input fields and the result label.

Contributing

If you would like to contribute to the project, feel free to fork the repository and create a pull request with your changes.

License

This project is licensed under the MIT License.

Acknowledgments

The program uses the Open Exchange Rates API for fetching exchange rates.
The GUI is built using the tkinter library in Python.
