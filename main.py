import csv
import json

csv_file_path = 'tuning.csv'

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        user_content, assistant_content = row
        
        message_json = {
            "messages": [
                {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_content}
            ]
        }
        
        print(json.dumps(message_json))