from app import app, db
from models import User, Story, Book

def init_db():
    with app.app_context():
        db.create_all()
        
        # Check if data already exists
        if User.query.first():
            print("Database already initialized.")
            return

        # Add sample user
        elara = User(username="elara", email="elara@quietude.com", bio="Anthropologist tracing the invisible threads of human experience.")
        elara.set_password("password123")
        db.session.add(elara)
        
        julian = User(username="julian", email="julian@quietude.com", bio="Cultural critic and letter writing enthusiast.")
        julian.set_password("password123")
        db.session.add(julian)

        # Add sample stories
        s1 = Story(
            title="The Architecture of Silence: Navigating the Modern Noise",
            content="In an era defined by constant connectivity, the rarest luxury is the absence of sound...",
            excerpt="In an era defined by constant connectivity, the rarest luxury is the absence of sound. We explore how intentional solitude shapes the creative psyche and why we must build cathedrals of quiet in our daily lives...",
            category="PHILOSOPHY",
            read_time="12 MIN READ",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuDNLJT6lhrBEwlnbbWnud-TfIQxIJ7z_cMLndPAmWI7mSTR29oiLPV1HxRvz1GnLBt3wI70Rt5awZZLG_aNbjRDi8MqfKId4o_8qQQLRC3BUdHG6aBXBQID58WBDbTyFLMq-SXhEJP0YZ1VCoplqttpO3N8YGdJu2FSiAbr3rgv1TZ-9RNY7DFeJTo_oEB3X2AvTzGOwZELALdKnbdglpaxYD1gKIGM8N1az1nB9EWykCofPM41MsJgn6DbYtAyYzyvtdBFm9Uj5aw",
            author=elara
        )
        
        s2 = Story(
            title="The Forgotten Art of Letter Writing",
            content="Before the instant gratification of digital communication, there was the deliberate act of the handwritten letter...",
            excerpt="Before the instant gratification of digital communication, there was the deliberate act of the handwritten letter...",
            category="CULTURE",
            read_time="8 MIN READ",
            image_url="",
            author=julian
        )

        # Add 100 sample stories
        categories = ["PHILOSOPHY", "CULTURE", "TRAVEL", "FICTION", "MEMOIR"]
        for i in range(1, 101):
            category = categories[i % len(categories)]
            author = elara if i % 2 == 0 else julian
            story = Story(
                title=f"The Silent Echo Vol. {i}",
                content=f"This is the content for story number {i}. It explores the depths of {category.lower()} and the human condition...",
                excerpt=f"An exploration into {category.lower()} in volume {i} of our ongoing series.",
                category=category,
                read_time=f"{5 + (i % 15)} MIN READ",
                image_url=f"https://picsum.photos/seed/{i+100}/800/600",
                author=author
            )
            db.session.add(story)

        # Add 100 sample books
        for i in range(1, 101):
            book = Book(
                title=f"Quietude Collection: Volume {i}",
                author=f"Author {i}",
                price=f"${15 + (i % 40)}.00",
                cover_url=f"https://picsum.photos/seed/{i}/400/600"
            )
            db.session.add(book)
        
        db.session.commit()
        print(f"Database initialized with {Story.query.count()} stories and {Book.query.count()} books.")

if __name__ == '__main__':
    init_db()
