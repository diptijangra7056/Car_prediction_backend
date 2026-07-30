import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from pathlib import Path

# Current directory (backend)
current_directory = Path(__file__).parent

# Load dataset
data_path = current_directory / "Car_Price_Prediction.csv"
df = pd.read_csv(data_path)

# Features and target
X = df[["Year", "Mileage"]]
y = df["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
model_path = current_directory / "model.pkl"
joblib.dump(model, model_path)

print("✅ Model trained and saved successfully as model.pkl")









# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# import joblib
# from pathlib import Path

# current_directory=Path(__file__).parent
# #data loaded
# df=pd.read_csv('backend/Car_Price_Prediction.csv')
# x=df[["Year","Mileage"]]
# y=df['Price']
# x_train,x_test,y_train,y_test=train_test_split(
#     x,y,test_size=0.2,random_state=42
#     )
# model=LinearRegression()
# model.fit(x_train,y_train)
# joblib.dump(model,current_directory/'model.pkl')
# print("model trained and saved succesfully as model.pkl")



# predictions=model.predict(x_test)

# print("predictions made!")
# print(f"first 10 predictions: {predictions[:10]}")

# accuracy=accuracy_score(y_test,predictions)
# print(f"Accuracy: {accuracy:.2f}")

# cm=confusion_matrix(y_test,predictions)
# print(f"Confusion Matrix:")
# print(cm)