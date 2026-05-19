
from flask import request,jsonify
from service.book_service import *

def register_book(app):
    
    @app.route("/add_book",methods=["POST"])
    def add_book():
        data = request.json
        
        if not data:
            return jsonify({"Attention":"Aucunz donnee reçue"})
        
        if not data.get("author"):
            return jsonify({"Attention":"Il manque le nom de l'auteur"})
        
        book = create_book(data)
        
        return jsonify(book.to_dict()),201
    
    @app.route("/books",methods=["GET"])
    def all_books():
        
        page = request.args.get("page",1,type=int) 
        
        per_page = request.args.get("per_page",5,type = int)    
        
        books_pagination = get_books(
            page,
            per_page
        )   
        
        return jsonify({
            "page":books_pagination.page,
            "pages":books_pagination.pages,
            "page_totale":books_pagination.total,
            "items":[
                book.to_dict()
                for book in books_pagination.items
            ]
        }),200
        
        
    @app.route("/book/<int:id>",methods = ["GET"])
    def get_book(id):
        
        book = one_book(id)
        
        if book is None:
            return jsonify({
                "error": "Livre introuvable"
            }), 404
            
        return jsonify(book.to_dict()),200
        
        
    @app.route("/book/update/<int:id>",methods = ["PUT"])
    def update_book(id):
        
        data = request.json
        book = up_books(id,data)
        
        if book is None:
            return jsonify({
                "error": "Livre introuvable"
            }), 404
            
        return jsonify(book.to_dict()),200
    
    
    @app.route("/book/delete/<int:id>",methods = ["DELETE"])
    def delete_book(id):
        book = supp_books(id)
        
        if book is None:
            return jsonify({
                "error": "Livre introuvable"
            }), 404
            
        return jsonify({"message": "Livre supprimé avec succès"}),200
            
            


