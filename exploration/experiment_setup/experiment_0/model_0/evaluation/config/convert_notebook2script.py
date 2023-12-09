import json

if __name__ == "__main__":
    
    data = json.load(open('./preprocessing.ipynb'))

    python_script_file = open("./src/main.py", "w")

    for cell in data['cells']:
        if cell['cell_type']=='code' and cell['source']:
            if "# input-data-definition (DON'T REMOVE THIS COMMENT)" in cell['source'][0]:
                python_script_file.write(''.join(cell['source']))
                python_script_file.write('\n\n')
            if "# input-data-ingestion (DON'T REMOVE THIS COMMENT)" in cell['source'][0]:
                python_script_file.write(''.join(cell['source']))
                python_script_file.write('\n\n')
            if "# process (DON'T REMOVE THIS COMMENT)" in cell['source'][0]:
                python_script_file.write(''.join(cell['source']))
                python_script_file.write('\n\n')
            if "# output-data-storing (DON'T REMOVE THIS COMMENT)" in cell['source'][0]:
                python_script_file.write(''.join(cell['source']))
                python_script_file.write('\n\n')
        if cell['cell_type']=='raw' and cell['source']:
            if "# step-execution (DON'T REMOVE THIS COMMENT)" in cell['source'][0]:
                python_script_file.write(''.join(cell['source']))
                python_script_file.write('\n\n')

    python_script_file.close()
    