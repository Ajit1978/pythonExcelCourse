from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

# MongoDB connection URI (replace with your actual URI)
MONGO_URI = "mongodb+srv://AjitMunj:Ajit1978@clusterfree.o11az.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFree"
client = MongoClient(MONGO_URI)
db = client.get_database('Employee')
collection = db.Grade


# Function to convert MongoDB _id field to string
def convert_objectid_to_str(doc):
    if isinstance(doc, dict):
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                doc[key] = str(value)
            elif isinstance(value, dict):
                convert_objectid_to_str(value)
            elif isinstance(value, list):
                for item in value:
                    convert_objectid_to_str(item)
    return doc


@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Query the collection (this will fetch all documents)
        data = collection.find()

        # Convert MongoDB documents to dictionaries with ObjectId as strings
        result = [convert_objectid_to_str(doc) for doc in data]

        return jsonify({"status": "success", "data": result}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/add_grade', methods=['POST'])
def add_grade():
    try:
        # Get data from the incoming POST request
        grade_data = request.json
        
        # Validate input data
        if not grade_data or not ('A' in grade_data and 'B' in grade_data and 'C' in grade_data):
            return jsonify({'error': 'Invalid data format, missing grade fields'}), 400

        # Insert data into MongoDB collection
        result = collection.insert_one(grade_data)

        # Return success response with inserted id
        return jsonify({
            'message': 'Grade data added successfully!',
            'id': str(result.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/update_grade/<string:id>', methods=['PUT'])
def update_grade(id):
    try:
        # Get the updated data from the incoming PUT request
        update_data = request.json

        # Ensure that the request contains at least one field to update
        if not update_data:
            return jsonify({'error': 'No data provided to update'}), 400

        # Check if all the necessary fields (A, B, C) exist in the update data
        if not ('A' in update_data or 'B' in update_data or 'C' in update_data):
            return jsonify({'error': 'At least one grade field (A, B, or C) is required'}), 400

        # Convert the provided id to an ObjectId type (MongoDB requires this)
        object_id = ObjectId(id)

        # Perform the update operation
        result = collection.update_one(
            {'_id': object_id},  # Search by the provided id
            {'$set': update_data}  # Update the fields
        )

        # If no document was updated
        if result.matched_count == 0:
            return jsonify({'error': 'Grade not found with the provided id'}), 404

        return jsonify({
            'message': 'Grade data updated successfully!',
            'id': id
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/delete_grade/<string:id>', methods=['DELETE'])
def delete_grade(id):
    try:
        # Convert the provided id to an ObjectId type (MongoDB requires this)
        object_id = ObjectId(id)

        # Perform the delete operation
        result = collection.delete_one({'_id': object_id})

        # If no document was deleted
        if result.deleted_count == 0:
            return jsonify({'error': 'Grade not found with the provided id'}), 404

        return jsonify({
            'message': 'Grade data deleted successfully!',
            'id': id
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
