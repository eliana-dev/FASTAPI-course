def require_auth(func):
    def wrapper(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Acceso denegado"

    return wrapper

@require_auth #encapsula de aca
def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"
# hasta aca

# auth_view_dashboard = require_auth(admin_dashboard)

# print(auth_view_dashboard("Admin"))
# print(auth_view_dashboard("Invitado"))
print(admin_dashboard("Admin"))
print(admin_dashboard("Invitado"))
