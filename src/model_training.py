from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error , mean_squared_error , r2_score
import pandas as pd
import joblib
def model_training(df):

    x = df.drop('AQI', axis = 1)
    y = df['AQI']

    x_train , x_test , y_train , y_test = train_test_split(x ,y, test_size =0.2 , random_state=26)
    
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = RandomForestRegressor(n_estimators=100)
    model.fit(x_train_scaled, y_train)
    model_pred = model.predict(x_test_scaled)
    
    mse = mean_squared_error(y_test, model_pred)
    print(f'Mean Squared Error: {mse}')

    R2_Score = r2_score(y_test, model_pred)
    print(f'R2 Score: {R2_Score}')

    return model


if __name__ == "__main__":
    df = pd.read_csv('data/processed/air_quality_clean.csv')
    model = model_training(df)
    print(model)
    joblib.dump(model , 'models/aqi_model.pkl')