import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.metrics import accuracy_score


def convert_date_to_int(datetime):
    return int(datetime.strftime("%Y%m%d%H%M"))


# read data by pandas
observations = pd.read_csv("datasets/train_observations.csv")
availability = pd.read_csv("datasets/train_availability.csv")

# change column with date to int
observations['timestamp'] = pd.to_datetime(observations['timestamp'])
observations['timestamp'] = observations['timestamp'].apply(lambda d: convert_date_to_int(d))

# change string values in columns to int representatives
label_encoder = preprocessing.LabelEncoder()
observations['route_id'] = label_encoder.fit_transform(observations['route_id'])

label_encoder = preprocessing.LabelEncoder()
availability['status'] = label_encoder.fit_transform(availability['status'])

# machine learning

train_ids = int(len(observations) / 3)

# Decision
clf = DecisionTreeClassifier().fit(observations[:train_ids], availability[:train_ids].status)
y_pred = clf.predict(observations[train_ids:])
print(accuracy_score(availability[train_ids:].status, y_pred))
print(clf.score(observations[train_ids:], availability[train_ids:].status))
