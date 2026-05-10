from src.agent import PMAgent

def menu():
    agent = PMAgent()
    
    while True:
        print("\n" + "="*50)
        print("🤖 PM AI AGENT — MVP")
        print("="*50)
        print("1. CSV-dən task yüklə")
        print("2. Prioritetləşmə")
        print("3. Riskləri göstər")
        print("4. Status report yarat")
        print("5. Mətndən task generasiyası (AI)")
        print("6. Tam analiz (1+2+3+4)")
        print("0. Çıxış")
        
        choice = input("\nSeçim: ")
        
        if choice == '1':
            path = input("CSV yolu (default: data/tasks.csv): ") or "data/tasks.csv"
            agent.load_tasks(path)
        elif choice == '2':
            agent.analyze()
            agent.show_priorities()
        elif choice == '3':
            if not agent.risks:
                agent.analyze()
            agent.show_risks()
        elif choice == '4':
            if not agent.tasks:
                agent.load_tasks("data/tasks.csv")
            agent.analyze()
            agent.generate_report()
        elif choice == '5':
            desc = input("Layihə təsvirini yaz: ")
            print(agent.generate_from_description(desc))
        elif choice == '6':
            agent.load_tasks("data/tasks.csv")
            agent.analyze()
            agent.show_priorities()
            agent.show_risks()
            agent.generate_report()
        elif choice == '0':
            break

if __name__ == "__main__":
    menu()
