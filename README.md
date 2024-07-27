# food-truck-challenge-
Food Truck Finder
Welcome to the Food Truck Finder project! This Python script searches through a CSV file to find food trucks that serve your favorite foods. It is simple to use, even if you are new to Python.

What You Need:
Before you begin, ensure you have:

Python: It can be downloaded and installed from the official Python website.
Pandas' Library: Install it with the following command:
bash
Copy the code and run pip install pandas.

HOW TO USE SCRIPT
Get the script.

Use Git to clone it.
Prepare your data.

Make sure your CSV file has the following columns: FoodItems, Applicant, and LocationDescription.
Save this file where you can easily find it.
Run the script.
Open your terminal or command prompt and navigate to the script-containing folder. To run it, enter this command:

bash
Copy the code: python your_script_name.py "Food Item" --filepath "path/to/your/file.csv".
Replace your_script_name.py with the name of your script, 
"Food Item" with the item you're looking for, and 
"path/to/your/file.csv" with the location where your file is saved.

For example, if you want to find trucks serving "tacos" and your file is in C:/Users/username/Documents/food_trucks.csv, you would run: 

Copy the code for food_truck_finder.py from bash to Python. "Tacos" --filepath "C:/Users/username/Documents/food_trucks.csv"
Check the results:

The script will provide a list of food trucks that sell the item you're looking for. It will display the truck's name and location.
Command Line Options
Food item (required): The name of the food you are looking for.
--filepath is optional. Path to your CSV file. If you don't specify it, it will use the default path.
Example Output:
If you search for "tacos," the script may show:

Copy CSS code.
Taco Truck A is located downtown, while Taco Stand B is on Main Street.
If no food trucks are found, it will read:

arduino
Copy code.
Food truck is not available. Tacos

Common Issues encountered
File Not Found: Double-check the file path to ensure that the CSV file exists.
Missing Columns: Check that your CSV has the required columns: FoodItems, Applicant, and LocationDescription.

Contributing
Have any ideas or found a bug? Please let me know by creating an issue or submitting a pull request.

Enjoy your food truck adventure!


