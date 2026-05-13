import functions_framework
from flask import jsonify

@functions_framework.http
def my_first_webhook(request):
    
    req = request.get_json(silent=True)
    print(req)

    #Let's print out the tag for our fulfillment to determine what sort of operation is being defined
    tag = req.get("fulfillmentInfo", {}).get("tag", "")

    session_params = req.get("sessionInfo", {}).get("parameters", {})

    print(tag)
    print(session_params)

    response_text = "We couldn't find your student id in our records!"

    if tag == "student_id_lookup":
        # We should validate that we have some records for the student itself
        # Normally this would be a database call but let's do it here for now
        student_id = session_params.get("student_id", "")
        existing_students = [
            "BS123456",
            "KG375601",
            "RN345178",
            "GB123987"
        ]

        if student_id in existing_students:
            response_text = "We found your information in our system"

    
    response = {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [
                            response_text
                        ]
                    }
                }
            ]
        }
    }

    return jsonify(response)
