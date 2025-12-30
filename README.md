<!-- markdownlint-disable MD041 -->

![CI/CD Pipeline](https://github.com/jerosanchez/fastapi-service/actions/workflows/deploy.yaml/badge.svg)
![Beta](https://img.shields.io/badge/status-beta-yellow)
![Python Version](https://img.shields.io/badge/python-3.13-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Docs](https://img.shields.io/badge/docs-available-brightgreen)

# README

## Getting Started

Follow these steps to set up your development environment:

### 1. Clone the repository

```sh
git clone git@github.com:jerosanchez/fastapi-service.git
cd post-service
```

### 2. Install markdownlint (for Markdown linting)

You need to install `markdownlint` globally to enable linting for Markdown files:

```sh
sudo apt update && sudo apt install nodejs npm
npm install -g markdownlint-cli
```

### 3. Install Python dependencies

Before using any other make target, run:

```sh
make install
```

This will create a virtual environment (if it doesn't exist) and install all Python dependencies listed in `requirements.txt`.

### 4. Customize the template for your project

Since this repository was created from a template, you'll need to customize several files for your specific project. Here's a checklist of what to update:

#### 4.1 Project Metadata

- **[pyproject.toml](pyproject.toml)**:
  - Update `name` (currently `fastapi-service`) to your project name
  - Update `description` to describe your service
  - Update `authors` with your name and email

- **[LICENSE](LICENSE)**:
  - Update the copyright holder name if needed

- **README.md** (this file):
  - Update the CI/CD badge URL to point to your repository
  - Update the repository URL in the clone command (step 1)
  - Customize the project description and any service-specific instructions

- **[CONTRIBUTING.md](CONTRIBUTING.md)**:
  - Review and customize development workflow guidelines for your team
  - Update project-specific folder structure details if you add new directories

#### 4.2 Application Configuration

- **[app/core/config.py](app/core/config.py)**:
  - Change `app_name` from `"MyApp"` to your application name
  - Add any additional configuration variables your service needs

- **[.env.example](.env.example)**:
  - Update `APP_NAME` to match your application name
  - Update `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` with your preferred defaults
  - Add any additional environment variables your service requires
  - Copy to `.env` for local development: `cp .env.example .env`

- **[.env.production](.env.production)**:
  - Update `APP_NAME` to match your application name
  - Review and adjust production settings (ports, log levels, workers)
  - Document any additional environment variables needed in production

#### 4.3 Docker Configuration

- **[docker-compose.yml](docker-compose.yml)**:
  - Update `container_name` values (`app-db`, `fastapi-service`) to match your project
  - Review and adjust default values in environment variable fallbacks
  - Adjust port mappings if your service uses different ports

- **[Dockerfile](Dockerfile)**:
  - Review if the Python version (3.13) matches your requirements
  - Adjust worker count in the CMD line if needed for production

#### 4.4 GitHub Actions and CI/CD

If you're using GitHub Actions for CI/CD:

- Update workflow files in `.github/workflows/` to reference your repository
- Ensure the Python version used in the pipelines matches the one used in Dockerfile
- Add required secrets in GitHub repository settings (e.g., `POSTGRES_PASSWORD`, API keys)
- Update deployment targets and environment configurations

#### 4.5 Quick Start Checklist

After customizing, verify your changes:

- Search for `fastapi-service`, `MyApp`, and `jerosanchez` across the codebase
- Ensure all references point to your new project name

### 5. Set up database migrations

Initialize Alembic:

```sh
alembic init alembic
```

This creates an `alembic/` directory with migration scripts and configuration files.

Next, configure Alembic to use your application's database settings. Open `alembic/env.py` and update it as follows:

```python
from app.core.config import config
from app.db.engine import Base

# Disable lint errors for this Alembic (third-party)
# pylint: disable=no-member

target_metadata = Base.metadata

# Set the SQLAlchemy URL dynamically from your app settings
db_url = os.environ.get("ALEMBIC_DB_URL", settings.db_url)
config.set_main_option("sqlalchemy.url", db_url)
```

Now you can generate and apply migrations:

```sh
# Generate a new migration after model changes
alembic revision --autogenerate -m "Describe your migration"

# Apply migrations to the database
alembic upgrade head
```

### 6. Run, test, and verify your changes

Start the FastAPI service locally:

```sh
make start
```

Once the server is running, open your browser and go to [http://localhost:8000/](http://localhost:8000/).

You should see a welcome message indicating the service is working.

You can also check the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).

After verifying the service works locally, run the tests to ensure everything passes:

```sh
make test
```

If all tests pass, commit and push your changes to the repository:

```sh
git add .
git commit -m "Customize project files"
git push
```

Then, go to your repository on GitHub and check the Actions tab to verify that the CI/CD pipeline runs and passes successfully. This ensures your changes are correctly integrated and deployed.

---

### 7. Clean up and document your project

Once you have completed the customization and verified everything works (steps 4 and 5), you should:

- **Remove steps 4 to 6 from this README** (as well as this step 7 when ready) to keep your documentation clean and relevant for future contributors.
- **Add any relevant information about your new project** to this README, such as:
  - Project overview and features
  - Setup or deployment instructions specific to your service
  - Usage examples
  - Any other important notes for users or contributors

This will help ensure your README is up-to-date and useful for your team and users.
