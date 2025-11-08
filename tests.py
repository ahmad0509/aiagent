from functions.get_files_info import *
from functions.get_file_contents import *
from functions.write_file_contents import *
from functions.run_python_file import *



def print_files_info(result, description):
    print(description)
    if isinstance(result, str):#error
        print (result)
    else:
        for entry in result:
            name=entry['name']
            file_size=entry['file_size']
            is_dir=entry['is_dir']
            print(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")

#print_files_info(get_files_info("calculator", "."), "Result for current directory:")
#print_files_info(get_files_info("calculator", "pkg"), "Result for current directory:")
#print_files_info(get_files_info("calculator", "/bin"), "Result for current directory:")
#print_files_info(get_files_info("calculator", "../"), "Result for current directory:")


#print(get_file_content("calculator", "main.py"))
#print(get_file_content("calculator", "pkg/calculator.py"))
#print(get_file_content("calculator", "/bin/cat"))
#print(get_file_content("calculator", "pkg/does_not_exist.py"))

# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))
print(run_python_file("calculator", "lorem.txt"))

