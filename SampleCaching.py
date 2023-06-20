from flask import Flask, request, jsonify
import time

app = Flask(__name__)

hashmap = {}

# write to file endpoint 
@app.route('/write', methods=['POST'])
def write():
    content = request.json['content']
    
    # write to file
    try:
        with open('CachingDump.txt', 'w') as file:
            file.write(f'{content}\n')
        return f'Data written to file successfully!'

    except Exception as e:
        raise f'Error writing to file: {str(e)}'

# read from file without cache
@app.route('/read_file/', methods=['GET'])
def read_file():
    # read from file 
    try:
        with open('CachingDump.txt', 'r') as file:
            for line in file:
                content = line
                time.sleep(2)
                return jsonify(content)
    except Exception as e:
        raise f'Error reading from file: {str(e)}'
    

# read from cache 
@app.route('/read_cache/', methods=['GET'])
def read_cache():
    # check in cache
    if 'content' in hashmap:
        return jsonify(hashmap['content'])

    
    # read from file then store in cache 
    try:
        with open('CachingDump.txt', 'r') as file:
            for line in file:
                content = line
                hashmap['content'] = content
                return jsonify(content)
           
    
    except Exception as e:
        raise f'Error reading from file: {str(e)}'

    
    
    
if __name__ == '__main__':
    app.run(debug=True)