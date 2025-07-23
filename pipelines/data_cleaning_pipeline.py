import pandas as pd

def read_data(file_path):
    """Read the sample data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Perform data cleaning operations on the DataFrame."""
    # Example cleaning operations
    df.dropna(inplace=True)  # Remove missing values
    df['Sales'] = df['Sales'].replace('[\$,]', '', regex=True).astype(float)  # Clean sales column
    df['Date'] = pd.to_datetime(df['Date'])  # Convert date column to datetime
    return df

def save_cleaned_data(df, output_path):
    """Save the cleaned DataFrame to a new CSV file."""
    df.to_csv(output_path, index=False)

def main():
    input_file = '../data/sample_data.csv'
    output_file = '../data/cleaned_data.csv'
    
    # Read the data
    data = read_data(input_file)
    
    # Clean the data
    cleaned_data = clean_data(data)
    
    # Save the cleaned data
    save_cleaned_data(cleaned_data, output_file)

if __name__ == "__main__":
    main()