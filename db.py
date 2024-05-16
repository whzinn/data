import pyrebase

# Configure o Firebase
config = {
  "apiKey": "SuaApiKey",
  "authDomain": "SeuAuthDomain",
  "databaseURL": "SuaDatabaseURL",
  "projectId": "SeuProjectId",
  "storageBucket": "SeuStorageBucket",
  "messagingSenderId": "SeuMessagingSenderId",
  "appId": "SeuAppId",
  "measurementId": "SuaMeasurementId"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def incrementa_acesso():
    acesso_atual = db.child("acessos").get().val()
    novo_acesso = acesso_atual + 1
    db.child("acessos").set(novo_acesso)
    print("Acesso incrementado com sucesso!")

# Exemplo de uso da função
incrementa_acesso()
