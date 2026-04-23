from app import app, db
from models import User, Story, Book

def init_db():
    with app.app_context():
        db.create_all()
        
        # Check if data already exists
        if User.query.first():
            print("Database already initialized.")
            return

        # Create 10 authors
        authors = []
        author_names = [
            ("Elara Aldridge", "elara@quietude.com"),
            ("Julian Thorne", "julian@quietude.com"),
            ("Marcus Aurel", "marcus@quietude.com"),
            ("Sarah Penning", "sarah@quietude.com"),
            ("David Kessler", "david@quietude.com"),
            ("Elena Vance", "elena@quietude.com"),
            ("Silas Marner", "silas@quietude.com"),
            ("Lyra Belacqua", "lyra@quietude.com"),
            ("Arthur Dent", "arthur@quietude.com"),
            ("Clara Oswald", "clara@quietude.com")
        ]
        
        for name, email in author_names:
            username = name.split()[0].lower() + "_" + str(author_names.index((name, email)))
            user = User(username=username, email=email, bio=f"A passionate storyteller and explorer of human experience.")
            user.set_password('password123')
            db.session.add(user)
            authors.append(user)
        
        db.session.commit() # Commit to get IDs

        # Add 100 sample stories distributed among 10 authors
        categories = ["PHILOSOPHY", "CULTURE", "TRAVEL", "FICTION", "MEMOIR"]
        for i in range(1, 101):
            category = categories[i % len(categories)]
            author = authors[i % len(authors)] # Rotate through 10 authors
            story = Story(
                title=f"The Silent Echo Vol. {i}",
                content=f"This is the content for story number {i}. Written by {author.username}, it explores the depths of {category.lower()} and the human condition...",
                excerpt=f"A deep dive into {category.lower()} by {author.username}.",
                category=category,
                read_time=f"{5 + (i % 15)} MIN READ",
                image_url=f"https://picsum.photos/seed/{i+100}/800/600",
                author=author
            )
            db.session.add(story)

        # Add 100 sample books
        for i in range(1, 101):
            author_name = author_names[i % len(author_names)][0]
            book = Book(
                title=f"Quietude Collection: Volume {i}",
                author=author_name,
                price=f"${15 + (i % 40)}.00",
                cover_url=f"https://picsum.photos/seed/{i}/400/600"
            )
            db.session.add(book)
        
        db.session.commit()
        print(f"Database initialized with {User.query.count()} authors, {Story.query.count()} stories, and {Book.query.count()} books.")

if __name__ == '__main__':
    init_db()
