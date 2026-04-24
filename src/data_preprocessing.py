# Import Lib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PowerTransformer
from sklearn.tree import DecisionTreeClassifier

#Pipeline :
def get_pipeline():

    model = Pipeline([
        ('scaler', StandardScaler()),
        ('yeo', PowerTransformer(method='yeo-johnson')),
        ('model', DecisionTreeClassifier(random_state=42))
    ])

    return model