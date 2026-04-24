from sklearn.model_selection import GridSearchCV


def train_model(model, X_train, Y_train):

 # Hyperparameter Tuning : 
    param_grid = {
        'model__max_depth' : [None, 5, 10, 15],
        'model__min_samples_split' : [2, 5, 10],
        'model__min_samples_leaf' : [1, 2, 4],
        'model__criterion' : ['gini', 'entropy'] 
    }

    grid = GridSearchCV(
        model,
        param_grid,
        cv=5,
        scoring ='accuracy'
    )

    grid.fit(X_train, Y_train) # Training...

 # Finding the Best-Parameters and the score :
    print('Best_param :', grid.best_params_)
    print('Best_score :', grid.best_score_)
    
    best_model = grid.best_estimator_

    return best_model