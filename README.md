<h1 align="center">FastAPI Blog</h1>
<p align="center">
	<em>A RESTful blog API built with FastAPI, PostgreSQL, and JWT authentication</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Subarna578/fastapi-blog?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Subarna578/fastapi-blog?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Subarna578/fastapi-blog?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Subarna578/fastapi-blog?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

A modern blog API built with FastAPI that provides complete CRUD operations for users and blog posts with JWT-based authentication. The project uses SQLAlchemy ORM with PostgreSQL for data persistence and Alembic for database migrations.

---

##  Features

- ✅ **User Management**: Create, read user accounts with email validation
- ✅ **Blog CRUD**: Full create, read, update, delete operations for blog posts  
- ✅ **Authentication**: JWT token-based authentication with OAuth2
- ✅ **Authorization**: Protected endpoints using Bearer tokens
- ✅ **Password Security**: Bcrypt hashing for secure password storage
- ✅ **Database Migrations**: Alembic for version-controlled schema changes
- ✅ **API Documentation**: Auto-generated Swagger UI and ReDoc
- ✅ **Testing**: Pytest suite with SQLite test database
- ✅ **Input Validation**: Pydantic schemas for request/response validation

---

##  Project Structure

```sh
└── fastapi-blog/
    └── backend
        ├── README.md
        ├── alembic
        ├── alembic.ini
        ├── apis
        ├── apps
        ├── core
        ├── db
        ├── docker-compose.yaml
        ├── main.py
        ├── requirements.txt
        ├── schemas
        ├── templates
        └── tests
```


###  Project Index
<details open>
	<summary><b><code>FASTAPI-BLOG/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			</table>
		</blockquote>
	</details>
	<details> <!-- backend Submodule -->
		<summary><b>backend</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/alembic.ini'>alembic.ini</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/docker-compose.yaml'>docker-compose.yaml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/main.py'>main.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>schemas</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/schemas/blog.py'>blog.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/schemas/user.py'>user.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<details>
						<summary><b>blogs</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/templates/blogs/home.html'>home.html</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>core</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/core/hashing.py'>hashing.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/core/config.py'>config.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/core/security.py'>security.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>apis</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/apis/base.py'>base.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>v1</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/apis/v1/route_user.py'>route_user.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/apis/v1/route_blog.py'>route_blog.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/apis/v1/route_login.py'>route_login.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>alembic</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/alembic/script.py.mako'>script.py.mako</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/alembic/env.py'>env.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>versions</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/alembic/versions/765528777cbd_first_migration.py'>765528777cbd_first_migration.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>apps</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/apps/base.py'>base.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>v1</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/apps/v1/route_blog.py'>route_blog.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>db</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/db/base.py'>base.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/db/base_class.py'>base_class.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/db/session.py'>session.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>models</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/db/models/blog.py'>blog.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/db/models/user.py'>user.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>repository</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/db/repository/blog.py'>blog.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/db/repository/user.py'>user.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Subarna578/fastapi-blog/blob/master/backend/db/repository/login.py'>login.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

- **Python**: 3.13 or higher
- **PostgreSQL**: 15 or higher (or Docker for containerized database)
- **pip**: Python package manager


###  Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Subarna578/fastapi-blog
cd fastapi-blog/backend
```

2. **Create a virtual environment:**
```bash
python -m venv env
# Windows
.\env\Scripts\activate
# Linux/Mac
source env/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**

Create a `.env` file in the `backend/` directory:
```env
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=blogdbcourse
SECRET_KEY=your-secret-key-here
```

5. **Start PostgreSQL** (using Docker):
```bash
docker-compose up -d
```

6. **Run database migrations:**
```bash
alembic upgrade head
```

###  Usage

**Start the development server:**
```bash
uvicorn main:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

**API Endpoints:**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/users/` | Create new user | No |
| POST | `/login/token` | Login and get JWT token | No |
| GET | `/blogs/` | Get all blogs | No |
| GET | `/blogs/{id}` | Get blog by ID | No |
| POST | `/blogs/` | Create new blog | Yes |
| PUT | `/blogs/{id}` | Update blog | Yes |
| DELETE | `/blogs/{id}` | Delete blog | Yes |

**Authentication Flow:**

1. Create a user: `POST /users/`
2. Login: `POST /login/token` with username (email) and password
3. Use the returned `access_token` in Authorization header: `Bearer <token>`

###  Testing

Run the test suite:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=. --cov-report=html
```


---
##  Project Roadmap

- [X] ✅ **User Management**: Create and manage user accounts
- [X] ✅ **Blog CRUD**: Complete blog post operations  
- [X] ✅ **JWT Authentication**: Secure login with token-based auth
- [X] ✅ **Database Migrations**: Alembic integration
- [X] ✅ **Testing Suite**: Pytest with fixtures
- [ ] 🔄 **Password Reset**: Email-based password recovery
- [ ] 🔄 **Comments System**: Add comments to blog posts
- [ ] 🔄 **Pagination**: Implement pagination for blog lists
- [ ] 🔄 **Search**: Full-text search for blogs
- [ ] 🔄 **Categories/Tags**: Organize blogs with categories

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/Subarna578/fastapi-blog/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Subarna578/fastapi-blog/issues)**: Submit bugs found or log feature requests for the `fastapi-blog` project.
- **💡 [Submit Pull Requests](https://github.com/Subarna578/fastapi-blog/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Subarna578/fastapi-blog
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Subarna578/fastapi-blog/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Subarna578/fastapi-blog">
   </a>
</p>
</details>

---

##  License

This project is open source and available under the MIT License.

---

##  Acknowledgments

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations
- **Alembic** - Database migration tool
- **Python-Jose** - JWT token implementation

---
