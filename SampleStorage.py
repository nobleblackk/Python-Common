from flask import Flask, jsonify, request 

app = Flask(__name__)

hashmap = {}


# write enpoint for memory 
@app.route('/memory', methods=['POST'])
def write():
    id = request.json['id']
    value = request.json['value']
    
    if not id or not value:
        raise Exception("Please send id and value")
    hashmap[id] = value 
    return jsonify('Id and value stored!!!')


# read endpoint for memory 
@app.route('/memory/<int:id>', methods=['GET'])
def read(id):
    if id in hashmap:
        return jsonify(hashmap[id])
    else:
        raise Exception("Key doesn't exist")
    

# write endpoint for file
@app.route('/file', methods=['POST'])
def write_to_file():
    # id = request.json['id']
    # value = request.json['valie']
    data = request.get_json()
    id = data['id']
    value = data['value']

    try:
        with open ('dump.txt', 'a') as file:
            file.write(f'{id},{value}\n')
        return 'Data written to file successfully!'
    except Exception as e:
        return f'Error writing to file: {str(e)}', 500
    

@app.route('/file/<int:id>', methods=['GET'])
def read_to_file(id):
    try:
        with open('dump.txt', 'r') as file:
            for line in file: 
                line_id, line_value = line.strip().split(',')
                if line_id == str(id):
                    return jsonify(f'ID: {line_id}, Value: {line_value}')
            return 'Data not found'
    except Exception as e:
        return f'Error retrieving Data: {str(e)}', 500


    

if __name__ == '__main__':
    app.run(debug=True)
