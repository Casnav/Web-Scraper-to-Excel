import pandas as pd
import os

def convert_to_excel():
    file_actual = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(file_actual, "books.csv")
    
    print(f"Searching file in: {csv_path}")
    print(f"¿The file exists? {os.path.exists(csv_path)}")
    
    try:
        df = pd.read_csv(csv_path, encoding='utf-8-sig')
        print(f"CSV readed: {len(df)} lines")
        
        excel_path = os.path.join(file_actual, "books_analysis.xlsx")
        df.to_excel(excel_path, index=False)
        print(f"Excel generated: {excel_path}")
        return True
    except FileNotFoundError:
        print("not Found books.csv")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    convert_to_excel()