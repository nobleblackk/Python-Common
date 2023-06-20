from flask import Flask, jsonify, request 

app = Flask(__name__)


# sample data 
books = []

# get endpoint to retrieve all books 
@app.route('/books', methods=['GET'])
def get_book_by_id():
    id = request.json['id']
    # Use the retrieved ID in your logic to retrieve the book
    # Example: book = get_book_by_id(id)
    # Return the book as a JSON response
    # Example: return jsonify(book)
    return f"Retrieving book with ID: {id}, {request.args, request.json}"



if __name__ == '__main__':
    app.run(debug=True)