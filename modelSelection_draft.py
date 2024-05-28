import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from sklearn.metrics import accuracy_score

from time import time

from warnings import filterwarnings
filterwarnings('ignore')

max_depths = range(1, 11)
n_trees = [100, 500]
models = {
    # linear boundary
    'lda' : LinearDiscriminantAnalysis(),
    'log' : LogisticRegression(penalty = None, max_iter = 100000),
    'svc_linear' : LinearSVC(dual = 'auto')
}

vec = pd.read_csv('vectorized_data.csv')
vecFlat = pd.DataFrame(vec['output'])
cols = vec.columns[:-2]
for col in cols:
    colDim = len(vec.iloc[0][col][1:-1].split(', '))
    colSplits = [col+str(i) for i in range(colDim)]
    vecFlat[colSplits] = vec[col].str[1:-1].str.split(', ', expand=True)

vf_train, vf_test = train_test_split(vecFlat, shuffle=True, random_state=1025, test_size=.2)
vf_tt, vf_val = train_test_split(vf_train, shuffle=True, random_state=1025, test_size=.2)
features = vecFlat.columns[1:]
target = vecFlat.columns[0]

scores = {}
for name, model in models.items():
    t0 = time()
    model.fit(vf_tt[features],vf_tt[target])
    scores[name] = accuracy_score(vf_val[target], model.predict(vf_val[features]))
    print('Fitting',name,'takes',time()-t0,'seconds, accuracy',scores[name])