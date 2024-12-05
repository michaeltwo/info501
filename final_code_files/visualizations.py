#%% IMPORTS 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import roc_curve, auc
import xgboost as xgb
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#%%
def plot_feature_importance(model_metrics):
    xgb.plot_importance(model_metrics['model'], importance_type='weight')
    plt.show()


def plot_confusion_matrix(model_metrics):
    cm = model_metrics.get("confusion_matrix")
    class_labels=["Control", "Sepsis"]

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, 
                xticklabels=class_labels, 
                yticklabels=class_labels)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.show()


def plot_roc_curves(df1, df2, model_metrics):

    model = model_metrics['model']

    def calculate_roc(df):
        X = df.drop(columns=['Diagnosis'])
        y = df['Diagnosis']
        if hasattr(model, "predict_proba"):
            y_score = model.predict_proba(X)[:, 1]
        elif hasattr(model, "decision_function"):
            y_score = model.decision_function(X)
        else:
            raise ValueError("Model does not have predict_proba or decision_function methods.")
        fpr, tpr, _ = roc_curve(y, y_score)
        roc_auc = auc(fpr, tpr)
        return fpr, tpr, roc_auc

    fpr1, tpr1, roc_auc1 = calculate_roc(df1)
    fpr2, tpr2, roc_auc2 = calculate_roc(df2)

    plt.figure()
    plt.plot(fpr1, tpr1, color='blue', lw=2, label=f'UML ROC (AUC = {roc_auc1:.3f})')
    plt.plot(fpr2, tpr2, color='orange', lw=2, label=f'UMG ROC (AUC = {roc_auc2:.3f})')
    plt.plot([0, 1], [0, 1], color='red', linestyle='--', lw=2, label='Random Classifier')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) for XgBoost')
    plt.legend(loc='lower right')
    plt.grid(alpha=0.3)
    plt.show()


#%%
## this is what the input is for the visualization functions
# metrics = {
#     "accuracy": accuracy_score(y_test, y_pred),
#     "precision": precision_score(y_test, y_pred, average="weighted"),
#     "recall": recall_score(y_test, y_pred, average="weighted"),
#     "f1_score": f1_score(y_test, y_pred, average="weighted"),
#     "confusion_matrix": confusion_matrix(y_test, y_pred),
#     "roc_auc": roc_auc_score(y_test, model.predict_proba(X_test)[:, 1], multi_class="ovr", average="weighted"),
#     "model" : model
    
#     }