from dotenv import load_dotenv
import os
import kagglehub

load_dotenv()
username = os.getenv("KAGGLE_USERNAME")

# Download latest version
path = kagglehub.dataset_download("arashnic/book-recommendation-dataset")

print("Path to dataset files:", path)
