import time

def fetch_data():
    time.sleep(2)  # Imitation of input/output delay
    return "Data fetched"
def main():
    result1 = fetch_data()
    result2 = fetch_data()
    print(result1,result2)

main()