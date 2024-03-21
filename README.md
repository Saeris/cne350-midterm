# CNE350 RESTful Database Access

a minimal RESTful web application powered by [Flask](https://flask.palletsprojects.com/en/3.0.x/) and [MariaDB](https://mariadb.com/)

## 🧰 Setup

<details>
  <summary>Click to view environment setup (optional)</summary>

This repo uses Python and was scaffolded using `uv`, a Rust-based package manager. Use one of the following to install it on your machine:

macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:

```ps
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Docker is also required to run the associated backend services. Setup instructions can be found [here](https://docs.docker.com/get-docker/).
</details>

1. Create a new local virtual environment:

   ```bash
   uv venv
   ```

1. Activate virtual environment (on Linux):

   ```bash
   source .venv/bin/activate
   ```

1. Install project dependencies:

   ```bash
   uv pip install -r requirements.txt
   ```

1. Deploy containers:

   ```bash
   docker-compose up -d
   ```

1. And serve!

   ```bash
   flask run
   ```

The Flask server is now running at [http://localhost:5000](http://localhost:5000]) and the Database can be accessed directly via PHPMyAdmin at [http://localhost:8080](http://localhost:8080). The default username/password is `root`/`changeme`.