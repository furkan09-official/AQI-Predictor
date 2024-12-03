import pandas as pd
from sklearn.preprocessing import OrdinalEncoder


def load_data(filepath):
    return pd.read_csv(filepath)



def preprocessed_data(df):
    df = df.dropna()
    df = df.drop(columns = ['Date', 'City'],axis = 1)
    encoding = {
    'Good': 1,
    'Satisfactory': 2,
    'Moderate': 3,
    'Poor': 4, 
    'Very Poor': 5,
    'Severe': 6
   }

    df['AQI_Category_Encoded'] = df['AQI_Category'].map(encoding)

    return df

  


def save_precessed_data(df,filepath):
    df.to_csv(filepath , index = False)




if __name__ == "__main__":
    df = load_data('data/raw/city_day.csv')
    df = preprocessed_data(df)
    save_precessed_data(df, 'data/processed/air_quality_clean.csv')
    print(df.head())
    print(df['AQI_Bucket'].value_counts())

