from collections import deque

class Helpdesk:
    def __init__(self): 
        self.queue = deque()

    def add_request(self, request):
        self.queue.append(request)
        print(f"\n✅ Request added: \"{request}\"")

    def resolve_request(self):
        if self.queue:
            resolved = self.queue.popleft()
            print(f"\n🛠️ Resolved request: \"{resolved}\"")
        else:
            print("\n⚠️ No requests to resolve.")

    def view_requests(self):
        if self.queue:
            print("\n📋 Pending Requests:")
            for i, req in enumerate(self.queue, 1):
                print(f"  {i}. {req}")
        else:
            print("\n✅ No pending requests.")

    def count_requests(self):
        print(f"\n📊 Total pending requests: {len(self.queue)}")

def menu():
    helpdesk = Helpdesk()
    while True:
        print("\n========== STUDENT HELPDESK MENU ==========")
        print("1. Add Help Request")
        print("2. Resolve Next Request")
        print("3. View Pending Requests")
        print("4. Count Pending Requests")
        print("5. Exit")
        print("===========================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            req = input("📝 Enter your help request: ")
            helpdesk.add_request(req)
        elif choice == '2':
            helpdesk.resolve_request()
        elif choice == '3':
            helpdesk.view_requests()
        elif choice == '4':
            helpdesk.count_requests()
        elif choice == '5':
            print("\n👋 Exiting Helpdesk. Thank you!")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
