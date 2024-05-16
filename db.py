import pyrebase

# Configure o Firebase
config = {
  apiKey: "AIzaSyAenex_EGTp0WkzFokkF-_80grJGU0KQco",
  authDomain: "data-44077.firebaseapp.com",
  databaseURL: "https://data-44077-default-rtdb.firebaseio.com",
  projectId: "data-44077",
  storageBucket: "data-44077.appspot.com",
  messagingSenderId: "930609972407",
  appId: "1:930609972407:web:11f777ec00c05be500f932"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def incrementa_acesso():
    acesso_atual = db.child("acessos").get().val()
    novo_acesso = acesso_atual + 1
    d = db.child("acessos").set(novo_acesso)
    print("Acesso incrementado com sucesso!")
    return f'{acesso_atual}, {d}'
