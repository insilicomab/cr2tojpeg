# CR2 to JPG

### 環境構築(Docker)

## CLI 上で学習を行う場合

1\. コンテナの作成と実行

```
docker compose up -d
```

2\. コンテナのシェルを起動する

```
docker compose exec -it cr2tojpeg /bin/bash
```

3\. シェルを使ってコマンドを実行する

例）CR2 を JPEG に変換する

```
python src/cr2tojpg.py <params>
```

4\. シェルから抜ける

```
exit
```

## Dev Containers 上で学習を行う場合

1\. コンテナの作成と実行

```
docker compose up
```

2\. リモートエクスプローラーの「開発コンテナー」を選択し、起動したコンテナにアタッチする

3\. VSCode 上でターミナルを表示し、学習を行う

### コンテナの停止

```
docker compose stop
```

再起動する際は以下のコマンドを実行する。

```
docker compose start
```

### コンテナの削除

```
docker compose down
```
