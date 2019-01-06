from sqlalchemy import create_engine
from sqlalchemy import inspect
import pprint

# pprint config
pp = pprint.PrettyPrinter(indent=2)

db_uri = 'sqlite:///database.db'
engine = create_engine(db_uri)

inspector = inspect(engine)

# Get table(s) information
pp.pprint(inspector.get_table_names())

# Get column information
pp.pprint(inspector.get_columns('books'))