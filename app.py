if __name__ == "__main__":
    from models import database
    from views import views
    from controllers import controller

    db = Database('my_database')  # Nama database
    view = View()
    controller = Controller(view, db)
    controller.run()
