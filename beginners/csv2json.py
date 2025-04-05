
import csv
import json

def csv_to_json(csv_file_path):
    data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    json_data = json.dumps(data, indent=4)
    return json_data

def main():
    csv_file = input("Enter CSV file path: ")
    try:
        json_output = csv_to_json(csv_file)
        output_file = csv_file.rsplit('.', 1)[0] + '.json'
        with open(output_file, 'w') as json_file:
            json_file.write(json_output)
        print(f"JSON data has been saved to {output_file}")
        
    except FileNotFoundError:
        print("Error: CSV file not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
