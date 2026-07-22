from app.core.config import settings
def main() -> None:
    print("MultiPost backend started")
    print(settings.app_name)

if __name__ == "__main__":
    main()