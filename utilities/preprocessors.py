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



def cohere(row):
    """
    restructures the meaningless number values in the dataframe
    and forms a coherent and meaningful sentence out of it

    args:
        row - row of a dataframe
    """
    message = ""
    df_indeces = row.keys()
    for df_index in df_indeces:
        if type(df_index) != int:
            # if header is a string specify the header in the message
            message += f"{df_index.lower().capitalize()} is {row[df_index] if not pd.isnull(row[df_index]) else "empty"}, "
        else:
            message += f"{row[df_index]} "
        

    return message



# Using recursion to get all values from nested dictionary
def extract_keys_values(file: dict):
    """
    extracts all information in nested dictionaries including
    key and value pair, recursively
    """
    try:    
        non_dict_vals = []

        for key, value in file.items():
            if isinstance(value, dict):
                non_dict_vals.extend(extract_keys_values(value))

            # this is if the value of corresponding key is an iterable
            # that may or may not contain purely single values or iterables
            # or another nested dictionary
            elif isinstance(value, list):
                for i in value:
                    if isinstance(i, dict):
                        non_dict_vals.extend(extract_keys_values(i))
                    else:
                        non_dict_vals.append(f'{key} is {i}')

            # this is if value of correspoinding key is purely an int, str, date,
            # or any value that is a non iterable
            else:
                non_dict_vals.append(f'{key} is {value}')

        return non_dict_vals
    except AttributeError:
        print(file)


        
def normalize_and_clean(text):
    text = str(text)

    # standardization and normalization
    text = re.sub(r" US ", " american ", text)
    text = text.lower()
    text = re.sub(r"’", "'", text)
    text = re.sub(r"i'm", "i am ", text)

    text = re.sub(r"don't", "do not ", text)
    text = re.sub(r"didn't", "did not ", text)
    text = re.sub(r"aren't", "are not ", text)
    text = re.sub(r"weren't", "were not", text)
    text = re.sub(r"isn't", "is not ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"doesn't", "does not ", text)
    text = re.sub(r"shouldn't", "should not ", text)
    text = re.sub(r"couldn't", "could not ", text)
    text = re.sub(r"mustn't", "must not ", text)
    text = re.sub(r"wouldn't", "would not ", text)

    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"that's", "that is ", text)
    text = re.sub(r"he's", "he is ", text)
    text = re.sub(r"she's", "she is ", text)
    text = re.sub(r"it's", "it is ", text)
    text = re.sub(r"that's", "that is ", text)

    text = re.sub(r"could've", "could have ", text)
    text = re.sub(r"would've", "would have ", text)
    text = re.sub(r"should've", "should have ", text)
    text = re.sub(r"must've", "must have ", text)
    text = re.sub(r"i've", "i have ", text)
    text = re.sub(r"we've", "we have ", text)

    text = re.sub(r"you're", "you are ", text)
    text = re.sub(r"they're", "they are ", text)
    text = re.sub(r"we're", "we are ", text)

    text = re.sub(r"you'd", "you would ", text)
    text = re.sub(r"they'd", "they would ", text)
    text = re.sub(r"she'd", "she would ", text)
    text = re.sub(r"he'd", "he would ", text)
    text = re.sub(r"it'd", "it would ", text)
    text = re.sub(r"we'd", "we would ", text)

    text = re.sub(r"you'll", "you will ", text)
    text = re.sub(r"they'll", "they will ", text)
    text = re.sub(r"she'll", "she will ", text)
    text = re.sub(r"he'll", "he will ", text)
    text = re.sub(r"it'll", "it will ", text)
    text = re.sub(r"we'll", "we will ", text)

    text = re.sub(r"\n't", " not ", text)
    text = re.sub(r"\'s", " ", text) 
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text) 
    
    text = re.sub(r"%", " percent ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ", text)
    text = re.sub(r"\+", " ", text)
    text = re.sub(r"\-", " ", text)
    text = re.sub(r"\=", " ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)

    # cleaning
    # remove a url in the content
    text = re.sub(r"(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))", " ", text)

    # anything that doesn't match the pattern is a obscure 
    # special character. Remove it
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)

    # remove any number that exeeds more than 4 digits
    text = re.sub(r"[0-9]{10,}", " ", text)
    # text = re.sub(r",", " ", text)

    # removes any colon preceded by an https or http
    text = re.sub(r"(?<=https):", " ", text)
    text = re.sub(r"https", " ", text)
    
    # duplicate whitespaces will be condensed into one
    text = re.sub(r"\s{2,}", " ", text)
    text = text.strip()
    
    return text



def clean_and_split_data(name, data, output_dir: str | None=None, char_limit: int=700, max_rows: int=40, cleaner=normalize_and_clean):
    """
    Cleans and splits text data:
    - Removes numbering at the start of lines.
    - Converts text to lowercase.
    - Splits each row to ensure it doesn't exceed the character limit.
    - Outputs multiple files if the number of rows exceeds max_rows.
    """
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

    # Process each row to enforce character limits
    output_lines = []
    for line in data:
        line = cleaner(line)
        print(line)
        output_lines.extend(split_into_chunks(line, char_limit))

    # Write to multiple files if necessary
    base_name = name

    
    if output_dir != None:
        # if output already exists use that folder (meaning don't overwrite)
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