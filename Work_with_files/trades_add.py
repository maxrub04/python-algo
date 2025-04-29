import csv
import json
#basic
def add_trade(info):
    try:
        with open("trades.txt", "a",encoding="utf-8") as file:
            file.write(f"{info}\n")
    except Exception as e:
        print(f"Error during adding info{e}")

add_trade("Buy bitcoin, 2, 2500 price")


#csv
def update_prices(input_file,output_file):
    try:
        with open(input_file, mode="r", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            data = [row for row in reader if row]  #deletes empty rows

        for row in data[1:]:
            row[1] = str(round(float(row[1]) * 1.05, 3))
        with open(output_file, mode="w", encoding="utf-8", newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(data)

    except FileNotFoundError:
        print(f"File {input_file} is not found.")
    except Exception as e:
        print(f"ERROR: {e}")

update_prices("trades.csv", "updated_trades.csv")

#json

def update_config(input_file, output_file, new_limits):
    try:
        with open(input_file, mode="r", encoding="utf-8") as infile:
            config = json.load(infile)

        config['limits'] = new_limits

        with open(output_file, mode="w", encoding="utf-8") as outfile:
            json.dump(config, outfile, indent=4)

    except FileNotFoundError:
        print(f"Файл {input_file} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка в формате JSON в файле {input_file}.")
    except Exception as e:
        print(f"Ошибка при обработке JSON: {e}")

new_limits = {
    "max_trade_amount": 100000,
    "min_trade_amount": 100
}
update_config("config.json", "updated_config.json", new_limits)
