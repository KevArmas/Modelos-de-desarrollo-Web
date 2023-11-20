def user_schema(user) -> dict:

    return {"id": str (user["_id"]),            
            "username": user["username"],
            "full_name": user["fill_name"], 
            "email": user["email"],
            "phone": user["phone"],
            "photo": user["photo"]}
