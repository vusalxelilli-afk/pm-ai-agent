import json
from datetime import datetime
from tabulate import tabulate

def print_priority_table(tasks):
    rows = []
    for t in tasks:
        rows.append([
            t.get('task_name'),
            t.get('owner'),
            t['deadline'].strftime('%Y-%m-%d') if hasattr(t['deadline'], 'strftime') else t['deadline'],
            t.get('status'),
            t.get('priority_score', 0)
        ])
    print(tabulate(rows, headers=['Task', 'Owner', 'Deadline', 'Status', 'Priority'], tablefmt='grid'))


def print_risks(risks):
    if not risks:
        print("✅ Risk aşkar olunmadı.")
        return
    print("\n⚠️  AŞKAR OLUNAN RİSKLƏR:\n")
    for r in risks:
        emoji = {'CRITICAL': '🔴', 'HIGH': '🟠', 'MEDIUM': '🟡'}.get(r['severity'], '⚪')
        print(f"{emoji} [{r['severity']}] {r['task']}")
        print(f"   → {r['message']}\n")


def save_json_report(tasks, risks, report_text, filename):
    output = {
        'generated_at': datetime.now().isoformat(),
        'tasks_prioritized': [
            {**{k: (v.isoformat() if hasattr(v, 'isoformat') else v) for k, v in t.items()}}
            for t in tasks
        ],
        'risks': risks,
        'status_report': report_text
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Report yadda saxlandı: {filename}")
