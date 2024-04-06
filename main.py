import csv
import json

# Path to your CSV file
csv_file_path = 'data/tuning.csv'
# Path to the output JSONL file
jsonl_file_path = 'data/tuning.jsonl'

# Open the CSV file for reading
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file, open(jsonl_file_path, mode='w', encoding='utf-8') as jsonl_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    
    for row in csv_reader:
        user_content, assistant_content = row

        system_message = "Marv is a factual chatbot that is also sarcastic."
        
        message_json = {
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_content}
            ]
        }
        
        # Write the JSON object to the JSONL file, one object per line
        jsonl_file.write(json.dumps(message_json) + '\n')