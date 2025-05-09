import pandas as pd

# Constants
CHARACTER_FILE = "Simpsons_Dataset\\simpsons_characters.csv"
SCRIPT_FILE = "Simpsons_Dataset\\simpsons_script_lines.csv"

KEY_EPISODE_INFORMATION = ["episode_id", "timestamp_in_ms", "character_id", "spoken_words", "word_count"]
EPISODE_SORTING_KEY = ["episode_id", "timestamp_in_ms"]

SORTED_INFO = "Processed_simpsons_dataset\\sorted_script_lines.csv"
STOP_DATASET = "Processed_simpsons_dataset\\stop_words_dataset.csv"