from datetime import datetime, timedelta

# === PRİORİTETLƏŞMƏ QAYDALARI ===
IMPACT_SCORE = {'high': 30, 'medium': 20, 'low': 10}

def calculate_priority(task, all_tasks):
    """
    Prioritet = deadline yaxınlığı + impact + dependency
    Maksimum 100 bal
    """
    score = 0
    today = datetime.now()
    days_left = (task['deadline'] - today).days
    
    # Qayda 1: Deadline yaxınlığı (max 40 bal)
    if days_left <= 1:
        score += 40
    elif days_left <= 3:
        score += 30
    elif days_left <= 7:
        score += 20
    else:
        score += 10
    
    # Qayda 2: Impact (max 30 bal)
    score += IMPACT_SCORE.get(task['impact'], 10)
    
    # Qayda 3: Dependency (başqa task bundan asılıdırsa +20)
    task_id = task.get('task_id', '')
    blocks_others = any(
        task_id in str(t.get('dependency', '')) for t in all_tasks
    )
    if blocks_others:
        score += 20
    
    # Qayda 4: Artıq başlanıbsa +10
    if task['status'] == 'in_progress':
        score += 10
    
    return min(score, 100)


# === RİSK AŞKARLAMA QAYDALARI ===
def detect_risks(tasks):
    risks = []
    today = datetime.now()
    
    # Owner-lərin yükünü hesabla
    owner_load = {}
    for t in tasks:
        if t['status'] != 'completed':
            owner_load[t['owner']] = owner_load.get(t['owner'], 0) + t['estimated_hours']
    
    for task in tasks:
        days_left = (task['deadline'] - today).days
        
        # Risk 1: Deadline keçib
        if days_left < 0 and task['status'] != 'completed':
            risks.append({
                'task': task['task_name'],
                'type': 'OVERDUE',
                'severity': 'CRITICAL',
                'message': f"Deadline {abs(days_left)} gün keçib!"
            })
        
        # Risk 2: Deadline yaxınlaşır, status başlamayıb
        elif days_left <= 2 and task['status'] == 'not_started':
            risks.append({
                'task': task['task_name'],
                'type': 'DELAY_RISK',
                'severity': 'HIGH',
                'message': f"{days_left} gün qalıb, hələ başlanmayıb"
            })
        
        # Risk 3: Resurs overload (>40 saat həftədə)
        if owner_load.get(task['owner'], 0) > 40:
            risks.append({
                'task': task['task_name'],
                'type': 'RESOURCE_OVERLOAD',
                'severity': 'MEDIUM',
                'message': f"{task['owner']} həddən çox yüklənib ({owner_load[task['owner']]} saat)"
            })
        
        # Risk 4: Dependency tamamlanmayıb
        if task.get('dependency'):
            deps = str(task['dependency']).split(';')
            for dep_id in deps:
                dep_task = next((t for t in tasks if t.get('task_id') == dep_id.strip()), None)
                if dep_task and dep_task['status'] != 'completed':
                    risks.append({
                        'task': task['task_name'],
                        'type': 'BLOCKED',
                        'severity': 'HIGH',
                        'message': f"'{dep_task['task_name']}' bitməyib, bu task başlaya bilməz"
                    })
    
    return risks


def prioritize_tasks(tasks):
    for t in tasks:
        t['priority_score'] = calculate_priority(t, tasks)
    return sorted(tasks, key=lambda x: x['priority_score'], reverse=True)
