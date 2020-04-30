https://medium.com/@astatsuya/reactの環境構築-create-react-appを使わずにreactアプリを作る-2c0228b31589
https://qiita.com/riversun/items/29d5264480dd06c7b9fb


本体
```
yarn add dyo
yarn add https://github.com/TongChia/dyo-router
```

webpack
```
yarn add -D webpack webpack-cli webpack-dev-server
```
- webpack: webpack本体
- webpack-cli: Comand line Interfaceの略。これに送られたparameterが、設定ファイル(通常webpack.config.js)と一致するparameterにマッピングしてくれる。
- webpack-dev-server: 開発用サーバー

babel
```
yarn add -D babel-loader @babel/core @babel/preset-env @babel/preset-react
```
- babel-loader: ローダー。ローダーとはwebpackの前処理で使用するもののこと。JSだけでなく様々な静的ファイルがバンドル出来る。これがWebpackの変換を助ける。
- @babel/core: babelのコアファイル？例えばES6で書かれたコードをES5に変換してくれる。
- @babel/preset-env: 細かい管理をしなくても最新のJavaScriptを使えるようにしてくれるpreset
- @babel/preset-react: react用のpluginのパッケージ

core-js
```
yarn add -D core-js@3
```
https://aloerina01.github.io/blog/2019-06-21-1


TypeScript
```
yarn add -D typescript ts-loader @types/react
```
- typescript: TypeScript本体
- ts-loader: TypeScriptをコンパイルするやつ
-　@types/react .tsxファイルのJSXを解釈できるようにするやつ