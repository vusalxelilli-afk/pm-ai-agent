# 5 Use-Case Demo

| # | Use-Case | Necə demo edilir | Gözlənilən nəticə |
|---|---|---|---|
| 1 | Task list → Prioritetləşmiş output | `python main.py` → seçim `1`, sonra seçim `2` | Tasklar priority score üzrə sıralanır |
| 2 | Deadline risk alert | `tasks.csv`-də deadline yaxın tarix qoy → seçim `3` | Yaxın deadline olan task üçün risk çıxır |
| 3 | Sprint status report | seçim `4` | JSON report yaranır və report mətni çıxır |
| 4 | Gecikmə xəbərdarlığı | Bir task-ın deadline tarixini keçmiş tarix et → seçim `3` | OVERDUE / CRITICAL risk çıxır |
| 5 | Dependency analizi | T002 task-ının dependency-si T001-dir; T001 completed deyilsə → seçim `3` | BLOCKED riski göstərilir |