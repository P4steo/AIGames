import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.metrics import accuracy_score


def convert_date_to_int(datetime):
    return int(datetime.strftime("%Y%m%d%H%M"))


def convert_date_to_vil_file_name(datetime):
    return int(datetime.strftime("VIL-%Y-%d-%m-%H_00Z.npz"))


def choose_vil_path(datetime):
    path = ""
    if datetime.datetime(2020, 1, 1) <= datetime <= datetime.datetime(2020, 3, 31):
        path = "VIL_merc_2020_01-03"
    elif datetime.datetime(2020, 4, 1) <= datetime <= datetime.datetime(2020, 5, 31):
        path = "VIL_merc_2020_04-06"
    elif datetime.datetime(2020, 7, 1) <= datetime <= datetime.datetime(2020, 12, 31):
        path = "VIL_merc_2020_07-12"
    elif datetime.datetime(2021, 1, 1) <= datetime <= datetime.datetime(2021, 5, 31):
        path = "VIL_merc_2021_01-06"
    elif datetime.datetime(2021, 7, 1) <= datetime <= datetime.datetime(2021, 12, 31):
        path = "VIL_merc_2021_07-12"
    else:
        path = ""
        # fix no data

    # generate whole path template "folder/convert_date_to_vil_file_name(datetime)"
    return path


# read data by pandas
observations = pd.read_csv("datasets/train_observations.csv")
availability = pd.read_csv("datasets/train_availability.csv")
route_definitions = pd.read_csv("datasets/route_definitions.csv")

# change column with date to int
observations['timestamp'] = pd.to_datetime(observations['timestamp'])
observations['timestamp'] = observations['timestamp'].apply(lambda d: convert_date_to_int(d))

# change string values in columns to int representatives
label_encoder = preprocessing.LabelEncoder()
observations['route_id'] = label_encoder.fit_transform(observations['route_id'])

label_encoder = preprocessing.LabelEncoder()
availability['status'] = label_encoder.fit_transform(availability['status'])

# join observations and status to one table
joined = pd.merge(observations, availability[["observation_id", "status"]], on="observation_id", how="left")

# machine learning

train_ids = int(len(observations) / 3)

# Decision
clf = DecisionTreeClassifier().fit(observations[:train_ids], availability[:train_ids].status)
y_pred = clf.predict(observations[train_ids:])
print(accuracy_score(availability[train_ids:].status, y_pred))
print(clf.score(observations[train_ids:], availability[train_ids:].status))
