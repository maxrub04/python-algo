import csv
import json

#basic data
with open("example.txt","r",encoding="utf-8") as file:
    content=file.read()
    print(content)

data=("hello, everyone. "
      "this is a new file that\n"
      "been created")
with open("output_data.txt","w",encoding="utf-8") as file:
    file.write(data)


#CSV
with open("trades.csv","r",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    headers = next(reader,None)
    print(f"Headers: {headers}")

    for row in reader:
        if row:   #deletes empty rows
            print("Row of data: ",row)

data =[
    ["Base","Quote","Price"],
    ["EUR","USD",1.135],
    ["USD","JPY",143.41]
]

with open("output_data.csv","w",newline="",encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerows(data)


#JSON
with open("trades.json","r",encoding="utf-8") as json_file:
    data = json.load(json_file)
    print(f"Data from JSON: {data}")

data =[{
    "Name":"EUR/USD",
    "Base":"EUR",
    "Quote":"USD",
    "Price":1.135,
    "Exchange":"OANDA"
}]

new_data = {
    "Name": "GBP/USD",
    "Base": "GBP",
    "Quote": "USD",
    "Price": 1.250,
    "Exchange": "OANDA"
}
data.append(new_data)
with open("output_data.json","w",encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)