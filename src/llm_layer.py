import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_tasks_from_text(description):
    """Layihə təsvirindən task-lar yaradır"""
    prompt = f"""
Sən təcrübəli Project Manager-sən. Aşağıdakı layihə təsvirini oxu və 
strukturlaşdırılmış JSON formatında task siyahısı yarat.

Hər task üçün: task_name, owner (boş qoy), estimated_hours, impact (high/medium/low), 
suggested_deadline_days (neçə gün lazımdır).

Layihə təsviri:
{description}

JSON formatında qaytar (başqa heç nə yazma):
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # ucuz və sürətlidir
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content


def generate_status_report(tasks, risks):
    """Sprint status report yazır"""
    task_summary = "\n".join([
        f"- {t['task_name']} | {t['owner']} | {t['status']} | priority: {t.get('priority_score', 'N/A')}"
        for t in tasks
    ])
    risk_summary = "\n".join([
        f"- [{r['severity']}] {r['task']}: {r['message']}" for r in risks
    ])
    
    prompt = f"""
Sən Project Manager-sən. Aşağıdakı task-lar və risklər əsasında 
peşəkar status report yaz (Azərbaycan dilində, qısa, idarəyə təqdim üçün).

TASK-LAR:
{task_summary}

RİSKLƏR:
{risk_summary}

Report bölmələri:
1. Ümumi vəziyyət (1-2 cümlə)
2. Tamamlanan / icrada / başlamamış statistikası
3. Əsas risklər
4. Növbəti addımlar üçün tövsiyələr
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content
