import pandas as pd
from sklearn.svm import SVC
import joblib
from sklearn.preprocessing import StandardScaler

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

