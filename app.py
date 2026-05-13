import time

def intro():
    print("\n--- THE COPILOT ADVENTURE ---")
    print("You are a developer speedrunning a hackathon.")
    print("Your goal: Complete 12 challenges before the timer runs out.")
    print("------------------------------")
    time.sleep(1)

def start_game():
    intro()
    choice = input("Do you use GitHub Copilot for help? (yes/no): ").lower()
    
    if choice == "yes":
        print("\n✨ Copilot suggests a high-velocity workflow! You finish 3 challenges instantly.")
        print("You've gained a massive lead.")
        second_choice()
    else:
        print("\n⏳ You decide to code everything manually. It's slow... the timer is ticking.")
        print("You fall asleep on your keyboard. GAME OVER.")

def second_choice():
    print("\nYou are now at the final boss: THE AUTH0 FGA CHALLENGE.")
    choice = input("Do you (1) Read the docs or (2) Use Copilot Chat? (1/2): ")
    
    if choice == "2":
        print("\n🚀 Copilot Chat generates the perfect RAG implementation! YOU WIN THE HACKATHON!")
        print("Congratulations, Champion!")
    else:
        print("\n📚 You get stuck in a documentation loop for 5 hours. You missed the submission deadline.")
        print("GAME OVER.")

if __name__ == "__main__":
    start_game()