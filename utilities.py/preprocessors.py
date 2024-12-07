import os
import re
import csv
import json

def line_valid(text):
    """
    As we can see the important information like
    * "Oracle-X"
    * "Oracle-X is a cutting-edge AI agent blending..."
    * "Oracle-X embodies elgance and reliability"

    are all preceded by the its corresponding key i.e.

    * "name": for "Oracle-X"
    * "description": for Oracle-X is a cutting-edge AI agent blending..."

    what we want is to only extract the lines with these specific 
    features i.e. the line must contain a ":" and that it must 
    be preceded by a string e.g. "Oracle-X" and not some other 
    character like {, [, 

    constraints that must be met if the line is to be valid
    line contains at least ":"
    ":" is succeeded by " "
    ":" is preceded by a "<some string>"

    include these
    ['"', 'n', 'a', 'm', 'e', '"', ':', ' ', '"', 'o', 'r', 'a', 'c', 'l', 'e', '-', 'x', '"', ',']
    ['"', 's', 'y', 'm', 'b', 'o', 'l', 'i', 's', 'm', '"', ':', ' ', '"', 'r', 'e', 'p', 'r', 'e', 's', 'e', 'n', 't', 's', ' ', 't', 'r', 'u', 's', 't', ',', ' ', 'e', 'n', 'l', 'i', 'g', 'h', 't', 'e', 'n', 'm', 'e', 'n', 't', ',', ' ', 'a', 'n', 'd', ' ', 'i', 'n', 't', 'e', 'l', 'l', 'i', 'g', 'e', 'n', 'c', 'e', ' ', 'w', 'i', 't', 'h', 'i', 'n', ' ', 'a', ' ', 'd', 'y', 'n', 'a', 'm', 'i', 'c', ' ', 'a', 'n', 'd', ' ', 'c', 'o', 'm', 'p', 'l', 'e', 'x', ' ', 'e', 'c', 'o', 's', 'y', 's', 't', 'e', 'm', '.', '"']
    "The blockchain whispers of new trends. Shall we dive into its insights?",
    "Market sentiment leans toward optimism. Could this be the moment to act?",
    "A new project emerges-its tokenomics and roadmap align with innovation. Let’s evaluate further."
    
    exclude these:
    ['}', ',']
    ['{']
    ['"', 'd', 'a', 't', 'a', 'd', 'r', 'i', 'v', 'e', 'n', 'd', 'e', 'c', 'i', 's', 'i', 'o', 'n', 's', '"', ':', ' ', '{']
    ['"', 'm', 'i', 's', 's', 'i', 'o', 'n', 'a', 'n', 'd', 'v', 'i', 's', 'i', 'o', 'n', '"', ':', ' ', '{']
    """
    # print(text)
    # matches any string enclosed in double quotes if 
    # there is none that means only "{", "}", etc. are found
    pattern_1 = r'"[A-Za-z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?\s]*"'
    match_1 = re.match(pattern_1, text)
    str_key_exists = bool(match_1)

    # but some cases are if string is enclosed in double quotes and that
    # string contains more double quotes
    pattern_2 = r'"[A-Za-z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*": [\{\[]'
    match_2 = re.match(pattern_2, text)
    str_value_exists = not bool(match_2)
    return str_key_exists and str_value_exists
    

def clean_and_split_data(input_path: str, output_dir: str, char_limit: int=700, max_rows: int=40):
    """
    Cleans and splits text data:
    - Removes numbering at the start of lines.
    - Converts text to lowercase.
    - Splits each row to ensure it doesn't exceed the character limit.
    - Outputs multiple files if the number of rows exceeds max_rows.
    """

    # # test out cognitive core 12 file first
    # if "Core 11" not in input_path:
    #     print(f"input_path: {input_path} skipped")
    #     return

    # helper function to split the lines into chunks of char_limit (700) lines
    def split_into_chunks(text, limit):
        """
        Splits a text into chunks no larger than the character limit.
        

        e.g "  "description": "Oracle-X is a...knowledge."," is a string
        or line that may ocntain 700+ characters 
        """
        
        chunks = []

        # if the length of line is bigger than limit i.e. 900 > 700
        # then the line is sliced into 700 character strings
        # and the next slice i.e. 700:900 or [700] to [899] is now set
        # as the next string to be processed but since slice [700] to [899]
        # length of 200 is now less than limit of 700 loop is terminated
        # and the final 200 characters are appended to the chunks list
        while len(text) > limit:
            chunks.append(text[:limit].strip())
            text = text[limit:]
        if text:
            chunks.append(text.strip())

        # chunks = [<chunk 1 of 700 char string>, <chunk 2 of 700 char string>, ..., <chunk n of <=700 char string>]
        return chunks

    # Read and clean the data
    with open(input_path, 'r', encoding='utf-8', errors='replace') as file:
        data = file.readlines()

    # Process each row to enforce character limits
    output_lines = []
    for line in data:
        # sample lines
        # "name": "Oracle-X"
        # "description": "Oracle-X is a...knowledge."

        # Convert to lowercase and remove extra spaces
        line = line.strip().lower()

        # Remove numbering period, parenthesis, whitespace
        line = re.sub(r'^\d+[\.\)]?\s*', '', line)

        # replace all occurences of \n or \\n with whitespace
        line = re.sub(r'\\n', ' ', line)
        
        if not line_valid(line):
            continue

        # extract corresponding value from key of
        # valid line by removing key
        line = re.sub(r'"[A-Za-zA-Za-z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*":\s', '', line)

        # remove trailing ',' at the end of each valid line
        line = line.rstrip(',')

        # final strip
        line = line.strip()

        # remove first and alst occurence of '"' chars
        line = line[1:-1] if line.startswith('"') and line.endswith('"') else line
        
        print(f"valid line: {line}")
        

        output_lines.extend(split_into_chunks(line, char_limit))

    # Write to multiple files if necessary
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    os.makedirs(output_dir, exist_ok=True)

    
    for i in range(0, len(output_lines), max_rows):
        """
        if there were 100 output lines and we wanted only
        40 lines per file, we would increment from
        0:0+40 or [0] to [39]
        40:40+40 or [40] to [79]
        80:80+40 or [80] to [119] 
        
        but in slicing arrays 
        when an array is only of a certain length and our end 
        index exceeds it we only really get the slice until the end of the array 
        so in essence we get only [80] to [99]
        """
        chunk = output_lines[i:i + max_rows]

        """40 is the max amount of rows"""
        output_file = os.path.join(output_dir, f"{base_name}_processed_part{i // max_rows + 1}.txt")
        print(f"output file: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(line + '\n' for line in chunk)

        print(f"File {output_file} has been created with {len(chunk)} lines.")

def convert_csv_to_txt(csv_path, txt_path, char_limit=700):
    """Converts a CSV file to a TXT file, enforcing a character limit per row."""
    def split_into_chunks(text, limit):
        """Splits a text into chunks no larger than the character limit."""
        chunks = []
        while len(text) > limit:
            chunks.append(text[:limit].strip())
            text = text[limit:]
        if text:
            chunks.append(text.strip())
        return chunks

    with open(csv_path, 'r', encoding='utf-8', errors='replace') as csv_file:
        reader = csv.reader(csv_file)
        output_lines = []
        for row in reader:
            row_text = ' '.join(row).strip()
            output_lines.extend(split_into_chunks(row_text, char_limit))

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.writelines(line + '\n' for line in output_lines)

    print(f"Converted {csv_path} to TXT format at {txt_path}.")

def convert_json_to_txt(json_path, txt_path, char_limit=700):
    """Converts a JSON file to a TXT file, enforcing a character limit per row."""
    def split_into_chunks(text, limit):
        """Splits a text into chunks no larger than the character limit."""
        chunks = []
        while len(text) > limit:
            chunks.append(text[:limit].strip())
            text = text[limit:]
        if text:
            chunks.append(text.strip())
        return chunks

    with open(json_path, 'r', encoding='utf-8', errors='replace') as json_file:
        data = json.load(json_file)
        output_lines = []

        if isinstance(data, list):
            for entry in data:
                entry_text = json.dumps(entry).strip()
                output_lines.extend(split_into_chunks(entry_text, char_limit))
        elif isinstance(data, dict):
            entry_text = json.dumps(data).strip()
            output_lines.extend(split_into_chunks(entry_text, char_limit))

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.writelines(line + '\n' for line in output_lines)

    print(f"Converted {json_path} to TXT format at {txt_path}.")

def process_all_files_in_directory(input_dir, output_dir, char_limit=700, max_rows=40):
    """
    Processes all text, CSV, and JSON files in a directory, cleaning and splitting them into rows within the character limit.
    Converts CSV and JSON files to TXT files before processing.
    Outputs multiple files if the number of rows exceeds max_rows.
    """
    if not os.path.exists(input_dir):
        print(f"Input directory {input_dir} does not exist.")
        return
    
    # exist_ok = True is so that when the output dir exists
    # os.makedirs won't raise an error because if a dir already
    # exists and we make an extra folder/directory we would 
    # have to override the existing one, which will need our
    # permission and cannot be done programmatically 
    os.makedirs(output_dir, exist_ok=True)

    input_files = [f for f in os.listdir(input_dir) if f.endswith(('.txt', '.csv', '.json'))]

    # <file name>.json
    # <file name>.json
    # <file name>.txt
    # <file name>.txt
    # <file name>.csv
    # <file name>.csv
    for input_file in input_files:
        # <file name>
        input_file_path = os.path.join(input_dir, input_file)

        try:
            if input_file.endswith('.csv'):
                # output dir is joined by input file path
                temp_txt_path = os.path.join(output_dir, input_file.replace('.csv', '.txt'))
                convert_csv_to_txt(input_file_path, temp_txt_path, char_limit)
                print(f"Converted {input_file} to TXT format at {temp_txt_path}.")
                input_file_path = temp_txt_path

            if input_file.endswith('.json'):
                temp_txt_path = os.path.join(output_dir, input_file.replace('.json', '.txt'))
                convert_json_to_txt(input_file_path, temp_txt_path, char_limit)
                print(f"Converted {input_file} to TXT format at {temp_txt_path}.")
                input_file_path = temp_txt_path

            clean_and_split_data(input_file_path, output_dir, char_limit, max_rows)
            print(f"Processed: {input_file_path}")

        except Exception as e:
            print(f"Error processing file {input_file}: {e}")