class Authenticator:
    def __init__(self):
        self.users = {}
    
    def register(self, username, password):
        if username in self.users:
            raise ValueError("エラー: ユーザーは既に存在します。")
        else:
            self.users[username] = password

    def login(self, username, password):
        if self.users.get(username) == password:
            return "ログイン成功"
        else:
            raise ValueError("エラー: ユーザー名またはパスワードが正しくありません。")