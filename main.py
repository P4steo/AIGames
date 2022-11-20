import numpy
import pandas as pd
import predictions as predictions
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, f1_score
import xgboost as xgb


def convert_date_to_int(datetime):
    return int(datetime.strftime("%H"))


def convert_date_to_vil_file_name(datetime):
    return int(datetime.strftime("VIL-%Y-%d-%m-%H_00Z.npz"))


# read data by pandas
observations = pd.read_csv("datasets/train_observations.csv")
availability = pd.read_csv("datasets/train_availability.csv")
route_definitions = pd.read_csv("datasets/route_definitions.csv")

# change column with date to int
observations['timestamp'] = pd.to_datetime(observations['timestamp'])
observations['timestamp'] = observations['timestamp'].apply(lambda d: convert_date_to_int(d))

# change string values in columns to int representatives
label_encoder_1 = preprocessing.LabelEncoder()
observations['route_id'] = label_encoder_1.fit_transform(observations['route_id'])

label_encoder_2 = preprocessing.LabelEncoder()
availability['status'] = label_encoder_2.fit_transform(availability['status'])

# join observations and status to one table
# joined = pd.merge(observations, availability[["observation_id", "status"]], on="observation_id", how="left")

# machine learning

train_ids = int(len(observations) / 3)

# Decision
#clf = DecisionTreeClassifier().fit(observations[:train_ids], availability[:train_ids].status)
#y_pred = clf.predict(observations[train_ids:])
#print(accuracy_score(availability[train_ids:].status, y_pred))
#print(clf.score(observations[train_ids:], availability[train_ids:].status))

data = pd.DataFrame(observations[:2*train_ids])
label = pd.DataFrame(availability[:2*train_ids].status)
# dtrain = xgb.DMatrix(data, label=label)

model = xgb.XGBClassifier()
model.fit(data, label)

# param = {'max_depth': 2, 'eta': 1, 'objective': 'binary:logistic'}
# num_round = 100
# evallist = [(dtrain, 'train')]
# bst = xgb.train(param, dtrain, num_round, evallist)

# save predictions

# prepare testing data
# test_data = pd.read_csv("datasets/test_observations_1000.csv")
# test_data['timestamp'] = pd.to_datetime(test_data['timestamp'])
# test_data['timestamp'] = test_data['timestamp'].apply(lambda d: convert_date_to_int(d))
#
# label_encoder = preprocessing.LabelEncoder()
# test_data['route_id'] = label_encoder.fit_transform(test_data['route_id'])
# d_test = xgb.DMatrix(test_data)
# label_test = xgb.DMatrix(label)

# make predictions
# prediction = bst.predict(d_test)
#test = bst.predict(test_data)
#print(prediction)

# print(accuracy_score(label_test, prediction))

val_data = pd.DataFrame(observations[train_ids:])
val_label = pd.DataFrame(availability[train_ids:].status)

predicted = model.predict(val_data)


print(accuracy_score(predicted, val_label))
print(f1_score(val_label, predicted))


observations_test = pd.read_csv("datasets/test_observations.csv")
# availability = pd.read_csv("datasets/train_availability.csv")

observations_test['timestamp'] = pd.to_datetime(observations['timestamp'])
observations_test['timestamp'] = observations_test['timestamp'].apply(lambda d: convert_date_to_int(d))

# change string values in columns to int representatives
# label_encoder_1 = preprocessing.LabelEncoder()
observations_test['route_id'] = label_encoder_1.transform(observations_test['route_id'])

predicted_test = model.predict(observations_test)
id_test = observations_test['observation_id']

result_data_dict = pd.DataFrame({'observation_id': id_test, 'status': predicted_test})
result_data_dict['status'] = result_data_dict['status'].apply(lambda x: 'OPEN' if x == 1 else 'CLSD')

result_data_dict.to_csv('test_availability.csv', index=False)

# predicted_observation_id = []
# predicted_status = []
#
# append data from predictions
# for result in range(0, len(prediction)):
#     status = ""
#     if prediction[result] == 1:
#         status = "OPEN"
#     else:
#         status = "CLSD"
#     predicted_observation_id.append(test_data['observation_id'][result])
#     predicted_status.append(status)
#
# result_data_dict = {'observation_id': predicted_observation_id, 'status': predicted_status}



# save data to file
# result_df = pd.DataFrame(result_data_dict)
# result_df.to_csv('test_availability.csv', index=False)
