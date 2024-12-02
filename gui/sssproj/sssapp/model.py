import joblib
import os
from django.conf import settings
# Load the trained model
file_path = os.path.join(settings.BASE_DIR, 'sssapp', 'static', 'xgboost_model.pkl')
model = joblib.load(file_path)