class DBCommands:
    create_user = 'INSERT INTO users (username, content) VALUES (\'{}\', \'{}\');'
    get_user = 'SELECT * FROM users WHERE username = \'{}\';'
    update_user_content = 'UPDATE users SET content = \'{}\' WHERE username = \'{}\';'