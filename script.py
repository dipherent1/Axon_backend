import os

PROJECT_NAME = "axon_backend"
DIRECTORIES = [
    f"{PROJECT_NAME}/api/routers",
    f"{PROJECT_NAME}/core",
    f"{PROJECT_NAME}/data/repositories",
    f"{PROJECT_NAME}/services",
    f"{PROJECT_NAME}/workers",
    f"{PROJECT_NAME}/tests/api",
    f"{PROJECT_NAME}/tests/services",
    f"{PROJECT_NAME}/tests/data",
]

# Files to be created with placeholder comments
FILES_WITH_CONTENT = {
    f"{PROJECT_NAME}/api/main.py": "# FastAPI app instance and router setup",
    f"{PROJECT_NAME}/api/dependencies.py": "# Reusable dependencies (e.g., get_current_user)",
    f"{PROJECT_NAME}/api/routers/conversations.py": "# API endpoints for conversations",
    f"{PROJECT_NAME}/api/routers/notes.py": "# API endpoints for notes",
    f"{PROJECT_NAME}/api/routers/users.py": "# API endpoints for user profiles",
    f"{PROJECT_NAME}/core/config.py": "# Pydantic settings for environment variables",
    f"{PROJECT_NAME}/core/security.py": "# Security utilities (password hashing, JWT)",
    f"{PROJECT_NAME}/data/models.py": "# SQLAlchemy ORM models (database table structures)",
    f"{PROJECT_NAME}/data/schemas.py": "# Pydantic schemas (data validation and API models)",
    f"{PROJECT_NAME}/data/repositories/base_repository.py": "# Optional: A base class for common repository methods",
    f"{PROJECT_NAME}/data/repositories/conversation_repository.py": "# All database logic for conversations",
    f"{PROJECT_NAME}/data/repositories/note_repository.py": "# All database logic for notes",
    f"{PROJECT_NAME}/services/processing_service.py": "# Core business logic for the AI pipeline",
    f"{PROJECT_NAME}/services/ai_service.py": "# Abstraction for all external AI API calls",
    f"{PROJECT_NAME}/services/notification_service.py": "# Logic for sending emails, etc.",
    f"{PROJECT_NAME}/workers/celery_app.py": "# Celery app instance and configuration",
    f"{PROJECT_NAME}/workers/tasks.py": "# Celery tasks that call the service layer",
    f"{PROJECT_NAME}/.env": "DATABASE_URL=\nOPENAI_API_KEY=\nGEMINI_API_KEY=\n",
    f"{PROJECT_NAME}/requirements.txt": "fastapi\nuvicorn\ncelery\nredis\npydantic\npydantic-settings\nsqlalchemy\npsycopg2-binary\n# ... add other packages here\n",
    # f"{PROJECT__NAME}/README.md": f"# {PROJECT_NAME.capitalize()} Backend\n\nThis is the backend for the {PROJECT_NAME.capitalize()} platform.\n",
    f"{PROJECT_NAME}/.gitignore": "__pycache__/\n*.pyc\n.env\n.venv/\nvenv/\n",
}

def create_project_structure():
    """Creates the entire project directory and file structure."""
    
    # Create the root project directory
    if not os.path.exists(PROJECT_NAME):
        os.makedirs(PROJECT_NAME)
        print(f"Created root directory: {PROJECT_NAME}/")

    # Create all subdirectories
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}/")

    # Create empty __init__.py files to make directories into packages
    for root, dirs, _ in os.walk(PROJECT_NAME):
        if "__pycache__" not in root:
            init_path = os.path.join(root, "__init__.py")
            if not os.path.exists(init_path):
                with open(init_path, "w") as f:
                    pass
                print(f"Created __init__.py in: {root}/")
    
    # Create files with placeholder content
    for file_path, content in FILES_WITH_CONTENT.items():
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {content}\n")
            print(f"Created file: {file_path}")

if __name__ == "__main__":
    print("Starting project scaffolding...")
    create_project_structure()
    print("\nProject structure for '{}' created successfully!".format(PROJECT_NAME))
    print("Next steps:")
    print(f"1. cd {PROJECT_NAME}")
    print("2. Create a virtual environment: python -m venv .venv")
    print("3. Activate it: source .venv/bin/activate (or .\\.venv\\Scripts\\activate on Windows)")
    print("4. Install dependencies: pip install -r requirements.txt")
    print("5. Start coding!")