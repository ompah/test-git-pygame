import yaml

def text_to_yaml(file_path):
    """
    Converts a structured text file into a YAML file.
    - Lines without `: ` are treated as a new card's name.
    - Lines with `: ` are parsed as key-value pairs.

    Args:
        file_path (str): Path to the input text file.

    Returns:
        str: The generated YAML content.
    """
    cards = []
    current_card = {}
   # file_path = 'ticket-raw.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if not line:  # Skip empty lines
                continue
            
            #make cards with name
            if ": " not in line:
                if current_card:  # Save the current card if it exists
                    cards.append(current_card)
                    current_card = {}
                    line = line.replace('"', '').replace('“', '').replace('”','').replace('…','...').replace('\u2018', "'").replace('\u2019', "'").replace('\u2026', "'").replace('\n', " ")     
                current_card["name"] = line
            
                # Add additional attributes with default or dynamic values
                current_card["id"] = len(cards) + 1  # Example: ID based on current number of cards
                current_card["effect"] = "effexct default"  # Example: ID based on current number of cards
                current_card["story_points"] = 1  # Default point value
                current_card["card_type"] = "default type"  # Default card type


            else:
                # Split into key-value pairs
                key, value = line.split(": ", 1)  # Part before ":" is key, the other is value
                key = key.lower().replace(" ", "_")  # Normalize key
                value = value.replace('"', '').replace('“', '').replace('”','').replace('…','...').replace('\u2018', "'").replace('\u2019', "'").replace('\u2026', "'").replace('\n', " ")     
                current_card[key] = value
                        

        print("\ntotal cards: ",len(cards))
        # Add an extra newline after each object (excluding the last one)


    # Add the last card if it exists
    if current_card:
        cards.append(current_card)

    # Convert to YAML format
    return yaml.dump({"cards": cards}, sort_keys=False, default_flow_style=False)


if __name__ == "__main__":
    # Files 
    input_file = "ticket-raw.txt"  
    output_file = "converted-carddata.yaml"  

    # Convert text to YAML
    yaml_content = text_to_yaml(input_file)

    # Write YAML content to a file
    with open(output_file, "w") as file:
        file.write(yaml_content)

    print(f"YAML content written to {output_file}")


