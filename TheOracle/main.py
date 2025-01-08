import asyncio, asyncpg, os, json

def get_db_password():
  return ""
def get_db_name():
  return ""

################################################################################
## SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';

## INSERT INTO prompt_data (layer, category, entry, public_value, private_value)
## VALUES (1, 'style', 'impressionistic', 'A style of painting that leaves an impression of the object.', 'The real prompt data is here.');

## SHOW server_encoding

## CREATE TABLE IF NOT EXISTS {table} (
##   id SERIAL PRIMARY KEY,
##   guid UUID UNIQUE NOT NULL,
##   email VARCHAR(100) UNIQUE NOT NULL,
##   username VARCHAR(100) UNIQUE NOT NULL
## );

## INSERT INTO {table} (guid, email, username) VALUES ({guid}, {email}, {username});

## SELECT * FROM {table} WHERE id = {id};
## SELECT COUNT(*) FROM {table};

## statement = await conn.prepare("SELECT * FROM users WHERE id = $1")
## result = await statement.fetch(1)
################################################################################

# Create/Migrate Tables
def db_create_users_table():
  create_user_table = """
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      guid UUID NOT NULL,
      email VARCHAR(100) NOT NULL,
      backup_email VARCHAR(100),
      username VARCHAR(100) NOT NULL,
      auth_info JSONB,
      UNIQUE (guid, email, username)
    );
  """
  return create_user_table
def db_create_templates_table():
  create_templates_table = """
    CREATE TABLE IF NOT EXISTS templates (
      id SERIAL PRIMARY KEY,
      category VARCHAR(255) NOT NULL,
      title VARCHAR(255) NOT NULL,
      description TEXT,
      image_url TEXT,
      layer1 TEXT,
      layer2 TEXT,
      layer3 TEXT,
      layer4 TEXT,
      input TEXT,
      private_template TEXT,
      UNIQUE (category, title)
    );
  """
  return create_templates_table
def db_create_keys_table():
  create_keys_table = """
    CREATE TABLE IF NOT EXISTS keys_data (
      id SERIAL PRIMARY KEY,
      layer INT NOT NULL,
      key_name VARCHAR(255) NOT NULL,
      key_value VARCHAR(255) NOT NULL,
      public_value TEXT,
      private_value TEXT,
      UNIQUE (key_name, key_value)
    );
  """
  return create_keys_table

async def migrate_categories_step1(conn):
  query_get_categories = """
    SELECT DISTINCT category
    FROM templates
    WHERE category IS NOT NULL;
  """
  categories = await conn.fetch(query_get_categories)

  if not categories: raise

  query_insert_category = """
    INSERT INTO categories (name) VALUEs ($1)
    ON CONFLICT (name) DO NOTHING;
  """

  for record in categories:
    category_name = record['category']
    await conn.execute(query_insert_category, category_name)

  print("Categories migration completed")
async def migrate_categories_step2(conn):
  query_add_column = """
    ALTER TABLE templates
    ADD COLUMN category_id INT;
  """
  await conn.execute(query_add_column)

  query_get_templates = """
    SELECT id, category
    FROM templates
    WHERE category IS NOT NULL;
    """
  templates = await conn.fetch(query_get_templates)

  query_get_category_id = """
    SELECT id
    FROM categories
    WHERE name = $1;
  """
  query_update_template = """
    UPDATE templates
    SET category_id = $1
    WHERE id = $2;
  """
  
  for template in templates:
    category_name = template['category']
    template_id = template['id']
  
    category_id_record = await conn.fetchrow(query_get_category_id, category_name)
    if category_id_record:
      category_id = category_id_record['id']
      await conn.execute(query_update_template, category_id, template_id)
  
  print("Templates migration complete.")
# async def migrate_categories_step3():
#   a = """ALTER TABLE templates DROP COLUMN category;"""
#   b = """VACUUM FULL templates;"""
#   c = """CREATE INDEX idx_templates_id_category_id ON templates (id, category_id);"""

# Functions
async def db_list_tables(conn):
  query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
  """
  tables = await conn.fetch(query)
  if not tables:
    print("No tables found.")
  else:
    return tables
async def db_list_databases(conn):
  query = """
    SELECT datname
    FROM pg_database;
  """
  databases = await conn.fetch(query)
  if not databases:
    print("No databases found.")
  else:
    return databases
async def db_list_columns(conn, table):
  query = f"""
    SELECT column_name, data_type, is_nullable
    FROM information_schema.columns
    WHERE table_name = '{table}';
  """
  columns = await conn.fetch(query)
  if not columns:
    print(f"No table named {table} found.")
  else:
    return columns
async def db_list_indexes(conn, table):
  query = f"""
    SELECT indexname, indexdef
    FROM pg_indexes
    WHERE tablename = '{table}';
  """
  indexes = await conn.fetch(query)
  if not indexes:
    print(f"No table named {table} found.")
  else:
    return indexes
async def db_get_public(conn):
  query = """
    WITH template_data AS (
      SELECT 
        c.name AS category,
        json_agg(
          json_build_object(
            'title', t.title,
            'description', t.description,
            'imageUrl', t.image_url,
            'layer1', t.layer1,
            'layer2', t.layer2,
            'layer3', t.layer3,
            'layer4', t.layer4,
            'input', t.input
          )
        ) AS templates
      FROM templates t
      JOIN categories c ON t.category_id = c.id
      GROUP BY c.name
    )
    SELECT json_object_agg(category, templates) AS result
    FROM template_data;
  """
  result = await conn.fetchval(query)
  if result is None:
    result = {}
  
  result_dict = json.loads(result)

  with open("public_templates.json", "w") as f:
    json.dump(result_dict, f, indent=2, ensure_ascii=False)

  return result_dict

# Samples
# def update_email(user_guid, new_email):
#   query = f"""
#     UPDATE users
#     SET email = {new_email},
#     WHERE guid = {user_guid}
#   """
#   return query
# def delete_user(guid):
#   query = f"""
#     DELETE FROM users
#     WHERE guid = {guid}
#   """
#   return query

# Basics
async def connect_db(db_name):
  pw = get_db_password()
  conn = await asyncpg.create_pool(
    user="theoracleadmin",
    password=pw,
    host="theoraclepg.postgres.database.azure.com",
    port=5432,
    database=db_name
  )
  print(f"Connected to database {db_name}.")
  return conn
async def reconnect_db(connection, db_name):
  await connection.close()
  pw = get_db_password()
  conn = await asyncpg.create_pool(
    user="theoracleadmin",
    password=pw,
    host="theoraclepg.postgres.database.azure.com",
    port=5432,
    database=db_name
  )
  print(f"Connected to database {db_name}.")
  return conn


# Console
async def interactive_console(conn):
  print("Connected to the database. Type 'exit' to quit.")
  while True:
    query = input("SQL> ").strip().lower().split()
    match query:
      case ["quit"] | ["exit"]:
        print("Exiting...")
        break

      case ["list", "databases"]:
        databases = await db_list_databases(conn)
        print("Databases:")
        for database in databases:
          print(f"- {database['datname']}")

      case ["list", "tables"]:
        tables = await db_list_tables(conn)
        print("Tables:")
        for table in tables:
          print(f"- {table['table_name']}")

      case ["list", "indexes", table_name]:
        indexes = await db_list_indexes(conn, table_name)
        print(f"Indexes on {table_name}:")
        for index in indexes:
          print(f"- {index['indexname']} ({index['indexdef']})")

      case ["list", "columns", table_name]:
        columns = await db_list_columns(conn, table_name)
        print(f"Columns in {table_name}:")
        for column in columns:
          print(f"- {column['column_name']} ({column['data_type']})")

      case ["get", "public"]:
        json = await db_get_public(conn)
        print(json)

      case ["parse", "templates"]:
        try:
          # Load JSON data from a file
          if not os.path.exists("templates.json"):
            print("Error: templates.json file not found.")
            continue

          with open("templates.json", "r") as file:
            data = json.load(file)

            # Generate and execute INSERT queries
            for category, templates in data.items():
              for template in templates:
                query = """
                  INSERT INTO templates (category, title, description, image_url, layer1, layer2, layer3, layer4, input)
                  VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9);
                """
                values = [
                  category,
                  template["title"],
                  template["description"],
                  template["imageUrl"],
                  template["layer1"],
                  template["layer2"],
                  template["layer3"],
                  template["layer4"],
                  template["input"],
                ]
                await conn.execute(query, *values)
          print("Templates inserted successfully.")
        except Exception as e:
          print(f"Error parsing templates: {e}")

      #case ["migrate", "step"]:
        #await migrate_categories_step1(conn)
        #await migrate_categories_step2(conn)

      case _:
        try:
          result = await conn.fetch(" ".join(query))
          for row in result:
            print(dict(row))
        except Exception as e:
          print(f"Error: {e}")

# Main
async def main():
  print("Connecting...")
  db = get_db_name()
  conn = await connect_db(db)
  try:
    await interactive_console(conn)
  finally:
    await conn.close()
if __name__ == "__main__":
  asyncio.run(main())
