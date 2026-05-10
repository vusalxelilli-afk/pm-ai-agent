import pandas as pd
import json
from datetime import datetime

def load_csv(file_path):
    """CSV faylını oxuyur və list formatında qaytarır"""
    df = pd.read_csv(file_path)
    df['deadline'] = pd.to_datetime(df['deadline'])
    return df.to_dict(orient='records')

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def manual_input():
    """İstifadəçidən manual task daxil etməyi soruşur"""
    tasks = []
    while True:
        name = input("Task adı (boş buraxsan bitir): ")
        if not name:
            break
        owner = input("Owner: ")
        deadline = input("Deadline (YYYY-MM-DD): ")
        impact = input("Impact (high/medium/low): ")
        tasks.append({
            'task_name': name,
            'owner': owner,
            'deadline': datetime.strptime(deadline, '%Y-%m-%d'),
            'status': 'not_started',
            'dependency': '',
            'estimated_hours': 8,
            'impact': impact
        })
    return tasks