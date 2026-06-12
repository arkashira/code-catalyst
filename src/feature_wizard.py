from src.dashboard import Dashboard, Feature

class FeatureWizard:
    def __init__(self, dashboard):
        self.dashboard = dashboard

    def run(self):
        while True:
            print("1. Add feature")
            print("2. Remove feature")
            print("3. List features")
            print("4. Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                name = input("Enter feature name: ")
                description = input("Enter feature description: ")
                feature = Feature(name, description)
                self.dashboard.add_feature(feature)
            elif choice == "2":
                name = input("Enter feature name: ")
                self.dashboard.remove_feature(name)
            elif choice == "3":
                for feature in self.dashboard.get_features():
                    print(f"{feature.name}: {feature.description}")
            elif choice == "4":
                break
            self.dashboard.save()
