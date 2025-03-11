import pytest
from authenticator import Authenticator

authenticator = Authenticator()

def test_register_1():
    authenticator.register("aaa", "001")
    assert authenticator.users["aaa"] == "001"

def test_register_2():
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register("aaa", "")

def test_login_1():
    assert authenticator.login("aaa", "001") == "ログイン成功"

def test_login_2():
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login("aaa", "002")