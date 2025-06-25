#--------- 1. Import libraries ---------#
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

#--------- 2. Load Dataset ---------#
# Set random seed for reproducibility
np.random.seed(0)

# Load iris dataset
iris = load_iris()

# Create a dataframe with the four feature variables
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# View top 5 rows
print(f'\nDataset:')
print(df.head())

#--------- 3. Create training and test data ---------#
# Label train/test data with random boolean based on 0.75 threshold
df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.75

# Create two new dataframes for train and test
train, test = df[df['is_train']==True], df[df['is_train']==False]
print('\nDataset Observations:')
print(f'Number of observations in the training data: {len(train)}')
print(f'Number of observations in the test data: {len(test)}')

#--------- 4. Preprocess data ---------#
# List of feature column names
features = df.columns[:4]

# Convert species names to numeric labels for training
y = pd.factorize(train['species'])[0]
print(f'\nTarget:')
print(f'{y}')

#--------- 5. Train classifier ---------#
clf = RandomForestClassifier(n_jobs=2, random_state=0)

# Train the classifier
clf.fit(train[features], y)

#--------- 6. Make predictions ---------#
preds = clf.predict(test[features])

#--------- 7. Evaluate ---------#
# Create confusion matrix
print(f'\nConfusion Matrix:')
print(pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species']))

#--------- 8. View feature importance ---------#
print(f'\nFeatures:')
print(list(zip(features, clf.feature_importances_)))