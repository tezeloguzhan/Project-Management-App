from flask import make_response, jsonify

def unauthorized():
    result={"error":
              {"msg": "401 error: Kullanıcı adı veya şifreniz yanlış."}
              }
    response=jsonify({'result': result})
    return make_response(response,401)

def unaccess():
    result={"error":
              {"msg": "401 error: Sadece adminler bu işlemleri yapabilir."}
              }
    response=jsonify({'result': result})
    return make_response(response,401)

