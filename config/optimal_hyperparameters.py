optimal_params = {
    "ips_knn": {
        "wine": {'k': 57},
        "breast_cancer": {'k': 5},
        "rice": {'k': 54},
        "sonar": {'k': 1},
        "parkinsons": {'k': 4},
        "spam": {'k': 6},
        "magic": {'k': 9},
    },
    "knn": {        
        "wine": {'n_neighbors': 61, 'weights': 'distance'},
        "breast_cancer": {'n_neighbors': 5, 'weights': 'uniform'},
        "rice": {'n_neighbors': 25, 'weights': 'uniform'},
        "sonar": {'n_neighbors': 1, 'weights': 'uniform'},
        "parkinsons": {'n_neighbors': 4, 'weights': 'distance'},
        "spam": {'n_neighbors': 14, 'weights': 'distance'},
        "magic": {'n_neighbors': 12, 'weights': 'distance'},
        },
    "naive_bayes": {        
        "wine": {'var_smoothing': 1e-09},
        "breast_cancer": {'var_smoothing': 1e-09},
        "rice": {'var_smoothing': 1e-09},
        "sonar": {'var_smoothing': 1e-09},
        "parkinsons": {'var_smoothing': 1e-07},
        "spam": {'var_smoothing': 1e-09},
        "magic": {'var_smoothing': 1e-07},
        },
    "logistic_regression": {        
        "wine": {'C': 0.001, 'penalty': 'l2', 'solver': 'saga'},
        "breast_cancer": {'C': 0.1, 'penalty': 'l2', 'solver': 'liblinear'},
        "rice": {'C': 100, 'penalty': 'l2', 'solver': 'liblinear'},
        "sonar": {'C': 0.1, 'penalty': 'l2', 'solver': 'liblinear'},
        "parkinsons": {'C': 10, 'penalty': 'l2', 'solver': 'liblinear'},
        "spam": {'C': 1, 'penalty': 'l1', 'solver': 'liblinear'},
        "magic": {'C': 100, 'penalty': 'l2', 'solver': 'lbfgs'},
        },
    "svm": {        
        "wine": {'C': 1.3, 'gamma': 0.8, 'kernel': 'rbf'},
        "breast_cancer": {'C': 0.8, 'gamma': 'scale', 'kernel': 'linear'},
        "rice": {'C': 0.8, 'gamma': 0.8, 'kernel': 'rbf'},
        "sonar": {'C': 10.0, 'gamma': 0.01, 'kernel': 'rbf'},
        "parkinsons": {'C': 10.0, 'gamma': 0.1, 'kernel': 'rbf'},
        "spam": {'C': 10.0, 'gamma': 0.01, 'kernel': 'rbf'},
        "magic": {'C': 10.0, 'gamma': 'scale', 'kernel': 'rbf'},
        },
    "decision_tree": {
                "wine": {'max_depth': 15, 'max_features': 'sqrt', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 5},
        "breast_cancer": {'max_depth': 5, 'max_features': 'log2', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 2, 'min_samples_split': 5},
        "rice": {'max_depth': 5, 'max_features': 'sqrt', 'min_impurity_decrease': 0.1, 'min_samples_leaf': 1, 'min_samples_split': 2},
        "sonar": {'max_depth': 5, 'max_features': 'log2', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 5},
        "parkinsons": {'max_depth': 5, 'max_features': 'sqrt', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2},
        "spam": {'max_depth': 10, 'max_features': 'sqrt', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 5},
        "magic": {'max_depth': 15, 'max_features': 'sqrt', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 5},
    },
    "random_forest": {
                "wine": {'bootstrap': True, 'max_depth': 20, 'max_features': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50},
        "breast_cancer": {'bootstrap': False, 'max_depth': 10, 'max_features': 'sqrt', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100},
        "rice": {'bootstrap': True, 'max_depth': 5, 'max_features': 'sqrt', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10},
        "sonar": {'bootstrap': False, 'max_depth': 10, 'max_features': 'log2', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50},
        "parkinsons": {'bootstrap': True, 'max_depth': 5, 'max_features': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 20},
        "spam": {'bootstrap': False, 'max_depth': None, 'max_features': 'log2', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 1000},
        "magic": {'bootstrap': True, 'max_depth': None, 'max_features': 'sqrt', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200},
    },
    "xgboost": {
                "wine": {'colsample_bytree': 0.5, 'learning_rate': 0.01, 'max_depth': 7, 'n_estimators': 500, 'reg_alpha': 0, 'reg_lambda': 0, 'scale_pos_weight': 3, 'subsample': 0.5},
        "breast_cancer": {'colsample_bytree': 0.8, 'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 200, 'reg_alpha': 0, 'reg_lambda': 0, 'scale_pos_weight': 3, 'subsample': 0.5},
        "rice": {'colsample_bytree': 0.8, 'learning_rate': 0.05, 'max_depth': 3, 'n_estimators': 100, 'reg_alpha': 0, 'reg_lambda': 0, 'scale_pos_weight': 1, 'subsample': 0.5},
        "sonar": {'colsample_bytree': 0.8, 'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 100, 'reg_alpha': 1e-05, 'reg_lambda': 1e-05, 'scale_pos_weight': 1, 'subsample': 0.8},
        "parkinsons": {'colsample_bytree': 0.5, 'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 200, 'reg_alpha': 0, 'reg_lambda': 1e-05, 'scale_pos_weight': 1, 'subsample': 0.8},
        "spam": {'colsample_bytree': 0.5, 'learning_rate': 0.01, 'max_depth': 7, 'n_estimators': 1000, 'reg_alpha': 1e-05, 'reg_lambda': 1e-05, 'scale_pos_weight': 3, 'subsample': 0.5},
        "magic": {'colsample_bytree': 0.8, 'learning_rate': 0.05, 'max_depth': 7, 'n_estimators': 1000, 'reg_alpha': 0, 'reg_lambda': 0, 'scale_pos_weight': 3, 'subsample': 0.8},
    },
}