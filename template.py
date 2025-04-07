import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)

project_name= 'mlproject'

lis_of_files = [
    # ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componetns/__init__.py",
    f"src/{project_name}/componetns/data_ingestion.py",
    f"src/{project_name}/componetns/data_transformation.py",
    f"src/{project_name}/componetns/model_trainer.py",
    f"src/{project_name}/componetns/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",   
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"

]

for file_path in lis_of_files:
    file_path = Path(file_path)
    file_dir, filename = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir}") 

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_path}")

    else:
        logging.info(f"File already exists: {file_path}")