from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InstagramPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128), unique=True, nullable=False)

if __name__ == '__main__':
    app = Flask(__name__)

    db_user = getenv("POSTGRES_USER")
    db_pass = getenv("POSTGRES_PASSWORD")
    db_name = getenv("POSTGRES_DB")
    db_host = "localhost"
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
