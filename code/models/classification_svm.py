import pandas as pd
from sklearn.svm import SVC
import joblib
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def svm_classifier(train_dir_data,trained_models):
    # Load your dataset into a pandas DataFrame
    data = pd.read_csv(train_dir_data)
    # Separate the features (X) and the target variable (y)
    df_data = data.drop(data.columns[-1], axis=1)
    df_label = data.iloc[:, -1]
    # Scale the features using StandardScaler
    scaler = StandardScaler()
    df_data_train_scaled = scaler.fit_transform(df_data)
    # Create an SVM classifier
    svm_classifier = SVC(kernel='linear')
    # Train the classifier on the training data
    svm_classifier.fit(df_data_train_scaled, df_label)
    joblib.dump(svm_classifier, trained_models)


def svm_classifier_test(path_test_data,predictions_svm_dir,path_model):
    # Load your dataset into a pandas DataFrame
    data = pd.read_csv(path_test_data)
    # Separate the features (X) and the target variable (y)
    df_data = data.drop(data.columns[-1], axis=1)
    # Scale the features using StandardScaler
    scaler = StandardScaler()
    df_data_test_scaled = scaler.fit_transform(df_data)
    # Use the loaded classifier for predictions
    loaded_classifier = joblib.load(path_model)
    y_pred = loaded_classifier.predict(df_data_test_scaled)
    # Create a DataFrame from predictions
    predictions_df = pd.DataFrame(y_pred)
    # Save predictions to a CSV file
    # Define the file names for the training and test sets
    predictions_file_name = path_test_data.stem + 'prediction.csv'
    prediction_file = Path.joinpath(predictions_svm_dir, predictions_file_name)
    predictions_df.to_csv(prediction_file, index=False)


def svm_accuricy_test(path_test_data, path_prediction_data):
    # Load your dataset into a pandas DataFrame
    data_test = pd.read_csv(path_test_data)
    data_originial_label = data_test.iloc[:, -1]
    data_prediction = pd.read_csv(path_prediction_data)
    accuracy = accuracy_score(data_originial_label,data_prediction)
    print(path_test_data.stem + f"Accuracy: {accuracy}")




