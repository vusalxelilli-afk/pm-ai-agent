# PM AI Agent — Limitations & Risk Management

| Risk | Necə idarə olunur |
|---|---|
| LLM hallucination | `temperature=0.3` istifadə olunur və insan təsdiqi tələb edilir |
| Yanlış prioritet | Hard-coded qaydalar şəffaf və audit oluna biləndir |
| Incomplete data | Validation mexanizmi istifadə olunur; deadline və owner boş olduqda xəta qaytarılır |
| API qiyməti | `gpt-4o-mini` modeli istifadə olunur |
| API down / quota | Try/except və fallback logic istifadə olunur |
| Dependency səhvləri | Dependency validation logic tətbiq olunur |
| Manual data səhvləri | CSV format və date parsing yoxlamaları aparılır |