import generator
from saver import CommunityDB

from flask import Flask, request, jsonify

app = Flask(__name__)
community_db = CommunityDB("TEST_COMMUNITY")

def get_request_data(json) -> tuple[str, str, str]:
    community_id = json.get("id")
    api_key = json.get("api_key")
    request_type = json.get("type")
    data = json.get("data", [])
    if len(data) < 1:
        return (None, None, None)
    username = data[0].get("username")
    api_id = data[0].get("apiId")
    return (community_id, username, api_id)

@app.route("/general/get_version", methods=["POST"])
def get_version():
    return "Sonoran Mock Server (github.com/adamBurdik/SonoranMock)"

@app.route("/general/get_account", methods=["POST"])
def get_account():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing account_id"}), 400
    
    
    community_id, username, api_id = get_request_data(data)
    if not community_id:
        return jsonify({"error": "Missing data"}), 400
    
    generated = generator.generate_account_data(username, api_id)
    community_db.set_item("accounts", generated["uuid"], generated)

    return jsonify(generated)

@app.route("/civilian/get_characters", methods=["POST"])
def get_characters():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing account_id"}), 400
    
    community_id, username, api_id = get_request_data(data)
    if not community_id:
        return jsonify({"error": "Missing data"}), 400
    
    chars = []
    for _, value in community_db.get_collection("characters").items():
        if (username and value["username"] == username) or (api_id and api_id in value.get("apiIds", [])):
            chars.append(value)
    
    if len(chars) > 0:
        return jsonify(chars)
    
    generated = [generator.generate_cad_character(username=username, api_id=api_id) for _ in range(3)]
    for character in generated:
        community_db.set_item("characters", character["id"], character)
    return jsonify(generated)

@app.route("/civilian/edit_character", methods=["POST"])
def edit_character():
    json = request.get_json()
    if not json:
        return jsonify({"error": "Missing account_id"}), 400
    
    community_id = json.get("id")
    api_key = json.get("api_key")
    request_type = json.get("type")
    data = json.get("data", [])
    if len(data) < 1:
        return jsonify({"error": "Missing data"}), 400
    
    username = data[0].get("username")
    api_id = data[0].get("apiId")
    use_dictionary = data[0].get("useDictionary", False)
    record_id = data[0].get("recordId")
    replace_values = data[0].get("replaceValues", {})
    
    chararacter = None
    for _, value in community_db.get_collection("characters").items():
        if (username and value["username"] == username) or (api_id and api_id in value.get("apiIds", [])) or (record_id and value["id"] == record_id):
            chararacter = value
            break
            
    if not chararacter:
        return jsonify({"error": "Character not found"}), 404
    
    for key, new_value in replace_values.items():
        for section in chararacter.get("sections", []):
            for field in section.get("fields", []):
                if field.get("uid") == key:
                    field["value"] = new_value
    
    community_db.set_item("characters", chararacter["id"], chararacter)
    return f"CHARACTER {chararacter['id']} EDITED FOR {username or api_id or record_id}"
    
    
if __name__ == "__main__":
    app.run()