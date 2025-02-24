import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

def process_data(dataframe):
    frequency_table = dataframe.groupby(['weather', 'winds'])['pilot_can_fly?'].value_counts().unstack().fillna(0)
    print(frequency_table) # Frequency table

    # Label encode
    dataframe['weather'] = preprocessing.LabelEncoder().fit_transform(dataframe['weather'])
    dataframe['winds'] = preprocessing.LabelEncoder().fit_transform(dataframe['winds'])
    dataframe['pilot_can_fly?'] = preprocessing.LabelEncoder().fit_transform(dataframe['pilot_can_fly?'])

    features = dataframe.drop(columns=['pilot_can_fly?'])
    targets = dataframe['pilot_can_fly?']

    features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.2, random_state=42)

    return features_train, features_test, targets_train, targets_test

# Train classifier
def build_model(features_train, targets_train):
    model = BernoulliNB(alpha=1.0) # Correct zero probability. Laplacian correction
    model.fit(features_train, targets_train)
    return model

# Evaluate
def evaluate(model, features_test, targets_test):
    likelihood = np.exp(model.feature_log_prob_)
    print(f'\nLikelihood: \n{likelihood}') # Likelihood

    probability = model.predict_proba(features_test) # Posterior probability
    print(f'\nProbabilities: \n{probability}')

    predicted = model.predict(features_test)
    print(f'\nPredicted classes: {predicted}')

    accuracy = accuracy_score(targets_test, predicted)
    print(f'\nAccuracy: {accuracy}')

    f1 = f1_score(predicted, targets_test, average="weighted")
    print("F1 Score:", f1)

def main():
    dataframe = pd.read_csv('aviation_dataset.csv')
    features_train, features_test, targets_train, targets_test = process_data(dataframe)
    model = build_model(features_train, targets_train)
    evaluate(model, features_test, targets_test)

if __name__ == '__main__':
    main()