import csv
import json

def read_trade_data(filename):
    """
    Function reads trade data from a CSV or JSON file.

    Arguments:
            filename (str): Path to the data file.

    Returns:
            list: List of dictionaries with trade data or empty list on error.
    """

    try:
        if filename.endswith('.csv'):
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        elif filename.endswith('.json'):
            with open(filename, mode='r', encoding='utf-8') as file:
                data = json.load(file)
        else:
            raise ValueError("USE CSV or JSON FILE")

        return data

    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"ERROR: WRONG FORMAT IN JSON FILE '{filename}'.")
        return []
    except ValueError as ve:
        print(f"ERROR: {ve}")
        return []
    except Exception as e:
        print(f"UNKNOWN ERROR: {e}")
        return []

data = read_trade_data('trades.csv')
print(data)