import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def upload_data():
    file_path = input("Enter the path to the CSV file: ")
    df = pd.read_csv(file_path)
    return df

def specify_data_file():
    # Prompt user to specify data file path
    pass

def enter_data_manually():
    data = input("Enter the data manually (CSV format, each row separated by newline): ")
    df = pd.read_csv(pd.compat.StringIO(data))
    return df

def perform_analysis(df):
    X = df.drop(columns=[target_column])
    y = df[target_column]
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
        
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

def display_results(results):
    X = df.drop(columns=[target_column])
    y = df[target_column]
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
        
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

def main():
    # Main function to orchestrate the workflow
    option = input("Choose data input option: (1) Upload data, (2) Specify data file, (3) Enter data manually: ")
    
    if option == "1":
        data = upload_data()
    elif option == "2":
        data = specify_data_file()
    elif option == "3":
        data = enter_data_manually()
    else:
        print("Invalid option.")
        return
    
    results = perform_analysis(data)
    display_results(results)

if __name__ == "__main__":
    main()
