import os
import uuid

def save_uploaded_file(uploaded_file, save_dir="uploads"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(save_dir, f"{file_id}_{uploaded_file.name}")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path
