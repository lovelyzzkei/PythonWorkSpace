import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# 생존에 중요한 factor 찾기
# women의 생존율은 약 74%이고, men의 생존율은 약 19%
# => 성별이 생존자를 예측하는 중요한 factor
# 그러나 성별만이 주 factor는 아님
# by considering multiple columns, we can discover more complex patterns
# that can potentially yield better-informed predictions.

# women = train_data.loc[train_data.Sex == 'female']["Survived"]
# rate_women = sum(women) / len(women)
# print(rate_women)

y = train_data['Survived']

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index=False)