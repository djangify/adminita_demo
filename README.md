# Adminita Demo Site

Demo site showcasing the [Adminita](https://github.com/djangify/adminita) Django Admin Theme.

**Live Demo:** [adminita.todiane.com](https://adminita.todiane.com)

## Guest Login

Explore the admin interface with read-only access:

| Field | Value |
|-------|-------|
| URL | [adminita.todiane.com/admin](https://adminita.todiane.com/admin) |
| Email | `guest@adminita.demo` |
| Password | `demopassword123` |

The guest account has view-only permissions - you can browse all models but cannot add, edit, or delete anything.

## Features Demonstrated

- Modern dashboard with app cards
- Change list views with search and filters
- Change forms with various field types
- Responsive sidebar navigation
- Login and logout pages

## Local Setup
```bash
# Clone the repo
git clone https://github.com/djangify/adminita_demo.git
cd adminita_demo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (for full access)
python manage.py createsuperuser

# Create guest user (for read-only demo access)
python manage.py create_guest_user

# Run server
python manage.py runserver
```

Visit [http://localhost:8000/admin](http://localhost:8000/admin)

## Related Links

- **Adminita Theme:** [github.com/djangify/adminita](https://github.com/djangify/adminita)
- **PyPI:** Coming soon
- **Documentation:** [github.com/djangify/adminita#readme](https://github.com/djangify/adminita#readme)

## License

MIT License - See [Adminita License](https://github.com/djangify/adminita/blob/main/LICENSE)
