
from extension import db

class Book(db.Model):
    
    __tablename__ = 'books'
    
    id = db.Column(db.Integer,primary_key = True)
    
    title = db.Column(db.String(200),nullable = True )
    
    author = db.Column(db.String(200),nullable = False )
    
    available = db.Column(db.Boolean,default=True)
    
    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "author":self.author,
            "available":self.available
        }