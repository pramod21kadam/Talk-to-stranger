from packages.packages import *
from model.master import *

class base:
    def insert(obj):
        try:
            db.session.insert(obj)
            return True
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            print(f"Insert error:- {e}")
            return False
        except Exception as e:
            print(f"Insert error:- {e}")
            return False
    
    def commit():
        try:
            db.session.commit()
            return True
        except exc.IntegrityError as e:
            db.session.rollback()
            print(f"Commit error(1):- {e}")
            return False
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            print(f"Commit error(2):- {e}")
            return False
        except Exception as e:
            print(e)
            return False