import openpyxl
import google.generativeai as genai
import time
start_time = time.time()

# Load the Excel file
excel_file = 'questions.xlsx'  # Replace with your file name
workbook = openpyxl.load_workbook(excel_file)

genai.configure(api_key="add you api key")

model = genai.GenerativeModel('gemini-1.5-flash')

filename = "program"#if you want to change file name 

sheet = workbook.active
i = 0


def clean_text(text):
    if text.startswith('```cpp'):
        text = text[6:].lstrip()
    
    if text.endswith('```'):
        text = text[:-3].rstrip()
    
    return text




try:
    for row in sheet.iter_rows(min_col=2, max_col=2, min_row=1, values_only=True):
        i += 1  
        cell_value = row[0]
        if cell_value is not None:

            prompt = cell_value + "  in c++ using namespace std only give C++ code as text" # this prompt that you can change if want more clear responce

            time.sleep(2) # change if you want to make this code fast but there is request time limit 
            response = model.generate_content(prompt)  

            cleaned_text = clean_text(response.text)
            
            #save file in programs folder
            with open(f"programs/{filename}_{i}.cpp", 'w') as file:
                file.write(cleaned_text)
                
except Exception as e:
    print(response)

end_time = time.time()
time_taken = end_time - start_time
print(time_taken)
