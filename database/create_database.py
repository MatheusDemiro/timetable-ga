from database import Database
from unified_database import UnifiedDatabase

database = Database()
unifiedDatabase = UnifiedDatabase(database.teachers, database.session)

database.create_database()

database.create_teachers()

database.create_unified_database()
