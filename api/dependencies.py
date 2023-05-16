from data.database import SessionLocal

# DB
def get_db():
    '''Get DB Dependency'''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
