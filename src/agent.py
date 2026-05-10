from src.input_layer import load_csv
from src.logic_layer import prioritize_tasks, detect_risks
from src.llm_layer import generate_status_report, generate_tasks_from_text
from src.output_layer import print_priority_table, print_risks, save_json_report

class PMAgent:
    def __init__(self):
        self.tasks = []
        self.risks = []
    
    def load_tasks(self, csv_path):
        self.tasks = load_csv(csv_path)
        print(f"✅ {len(self.tasks)} task yükləndi.")
    
    def analyze(self):
        self.tasks = prioritize_tasks(self.tasks)
        self.risks = detect_risks(self.tasks)
    
    def show_priorities(self):
        print("\n📋 PRİORİTETLƏŞMİŞ TASK SİYAHISI:\n")
        print_priority_table(self.tasks)
    
    def show_risks(self):
        print_risks(self.risks)
    
    def generate_report(self, save_path='reports/report.json'):
        print("\n📝 Status report hazırlanır (LLM)...")
        report = f"""
# Sprint Status Report

Ümumi task sayı: {len(self.tasks)}
Aşkar olunan risk sayı: {len(self.risks)}

Ən yüksək prioritetli task: {self.tasks[0]['task_name'] if self.tasks else 'Yoxdur'}

Qeyd: AI report deaktivdir, çünki OpenAI API quota/billing aktiv deyil.
"""
        print("\n" + "="*60)
        print(report)
        print("="*60)
        save_json_report(self.tasks, self.risks, report, save_path)
        return report
    
    def generate_from_description(self, text):
        return generate_tasks_from_text(text)
