from database.database import Database
from database.unified_database import UnifiedDatabase

database = Database()
unifiedDatabase = UnifiedDatabase(database.teachers, database.session)

database.create_database()

database.create_teachers()

database.create_unified_database()
