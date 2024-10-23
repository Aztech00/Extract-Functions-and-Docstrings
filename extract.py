def extract_functions(python_filename, output_filename):
    function_names = []
    docstrings = []
    docstring_to_add = ""
    is_docstring = 0
    with open(python_filename, 'r') as file:
        for line in file:
            if "def" in line:
                function_names.append(line[4:-2])
                
            if not('"""' in line) and is_docstring == 1:
                docstring_to_add += line
            if line.count('"""') == 2:
                line = line.replace('"""', '')
                docstrings.append(line)
            elif line.count('"""') == 1 and is_docstring == 0:
                is_docstring = 1
                docstring_to_add += line
            elif line.count('"""') == 1 and is_docstring == 1:
                is_docstring = 0
                docstring_to_add += line
                docstring_to_add = docstring_to_add.replace('"""', '')
                docstrings.append(docstring_to_add)
                docstring_to_add = ""
            

            

            

    with open(output_filename, 'w') as file:
        for i in range(len(function_names)):
            file.write(f"{i + 1}. ")
            file.write(f"{function_names[i]}\n")
            file.write(docstrings[i])
            file.write("\n")

extract_functions('python_script.py', "test1.txt")
