import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_data BLOB NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            classification_result TEXT
        )
    ''')
    conn.commit()
    conn.close()
    
def insert_image(image_data):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO images (image_data) VALUES (?)
    ''', (image_data,))
    conn.commit()
    conn.close()

def get_images():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM images')
    images = cursor.fetchall()
    conn.close()
    return images

def get_image_by_id(image_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM images WHERE id = ?', (image_id,))
    image = cursor.fetchone()
    conn.close()
    return image

def update_classification(image_id, classification_result):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE images SET classification_result = ? WHERE id = ?
    ''', (classification_result, image_id,))
    conn.commit()
    conn.close()
    
def get_latest_image_id():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM images')
    latest_id = cursor.fetchone()[0]
    conn.close()
    return latest_id

