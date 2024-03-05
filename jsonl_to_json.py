from dotenv import load_dotenv
import os

load_dotenv()
initial_dataset = os.getenv('INITIAL_DATASET')

file = open(initial_dataset, 'r')

with open('filtered.json' , 'w') as writeFile:
    for line in file:
        writeFile.write(line + ", ")

file.close()
writeFile.close()