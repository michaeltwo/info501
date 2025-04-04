# info501

## Sepsis Screening System based Complete Blood Count Lab Results using Data Mining Techniques
## Data preprocessing
#### Columns used
```
['Age','Sex','HGB','MCV','PLT','RBC','WBC',]  'CRP' is optional 
```

#### Columns dropped
```
['Id','Set','Sender','Episode','Time','TargetIcu','SecToIcu','PCT']，'Center' is used to split data
```

#### Preprocessing process
![image](https://github.com/michaeltwo/info501/blob/main/images/preprocessing.png)

## Model - 4 algorithms

Xgboost,
Random Forest,
KNN,
SVM

## Interpretation
#### accuracy, confusion matrix, roc-auc, etc.

## GUI Instructions
#### download code from gui folder
#### cd to sssproj folder and then run command below sequentially
```
python manage.py makemigrations && python manage.py migrate
```
```
python manage.py runserver
```
#### visit http://127.0.0.1:8000 via web browser


## Contributors
Craig, Xueping, Prasanna, Weihua

## License
B
