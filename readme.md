Djangoサンプル（一般ユーザーと企業ユーザーを分けた求人サイト）
====

# 環境構築
venv仮想環境構築
```
python -m venv venv
```
venvの有効化  
macOS  
```
. venv/bin/activate
```

WindowsOS
```
. venv/scripts/activate
```

パッケージインストール
```
pip install -r requirement.txt
```

マイグレーション
```
python manage.py makemigrations
python manage.py migrate
```

管理者アカウントの作成
サインアップ画面から作成しても管理者権限は持たないので管理画面にはアクセスできない。  
そのため、最初の管理者アカウントはコマンドから作成する  
※コマンドで作成した場合は、自動的に一般ユーザー、企業ユーザーのレコードが作られないので注意する  
　あくまで管理画面を操作する用のユーザーアカウントが作成される。  
  通常の検証は、サインアップ画面からアカウントを作成する必要がある。
```
python manage.py createsuperuser
```

# 実行方法
```
python manage.py runserver
```

http://127.0.0.1:8000   にアクセスし  
トップ画面に、ログイン、一般ユーザー用会員登録、企業ユーザー用の会員登録のリンクが表示されていれば成功

# 構成
app/: project設定等
recruit/: メインコンテンツ
users/: User関連
templates/: テンプレート
  templates/account/: allauth関連のテンプレート、ログイン画面等のカスタマイズ
static/: 静的ファイル用のフォルダ(*.js, *.css等)
media/: 画像、アップロードしたファイル等の動的に追加されるファイルを格納するフォルダ

以下は環境変数設定用のファイルのため、環境毎に用意する
.envファイルが読み込まれるため、各環境用のファイルをenvにリネームして使用する
```
.env　　実行時に使用する
.env.develop    開発用のファイルのコピー
.env.production　本番用のファイルのコピー
```

定義した変数はos.environ.get("変数名")でpyファイルで読み込める

