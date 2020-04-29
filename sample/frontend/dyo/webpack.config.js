// reactの環境構築-create-react-appを使わずにreactアプリを作る
// https://medium.com/@astatsuya/reactの環境構築-create-react-appを使わずにreactアプリを作る-2c0228b31589

// 新人にドヤ顔で説明できるか、今風フロントエンド開発ハンズオン(Git/Node.js/ES6/webpack4/Babel7)
// https://qiita.com/riversun/items/29d5264480dd06c7b9fb

// webpack 4 入門
// https://qiita.com/soarflat/items/28bf799f7e0335b68186

// yarn add -D webpack webpack-cli webpack-dev-server
// yarn add -D babel-loader @babel/core @babel/preset-env @babel/preset-react
// yarn add -D core-js@3
// yarn add -D typescript ts-loader @types/react

// output.pathに絶対パスを指定する必要があるため、pathモジュールを読み込んでおく
const path = require("path");

module.exports = {
  // モード値を production に設定すると最適化された状態で、
  // development に設定するとソースマップ有効でJSファイルが出力される
  mode: "development",
  // 開発用サーバー
  devServer: {
    open: true, // webpack-dev-server起動時(npm startなどで）に自動的にブラウザを起動する。
    openPage: "index.html", // 自動的にブラウザを起動するときに開くページ
    // htmlファイルや画像、CSSなどのコンテンツのルートディレクトリ
    // 作業ディレクトリ以下publicというディレクトリがコンテンツのルートディレクトリ
    contentBase: path.join(__dirname, "public"),
    // 設定した contentBase 以下にあるファイルに変更があった場合に自動的にブラウザをリロードする機能
    watchContentBase: true,
    host: "0.0.0.0",
    port: 3000,
  },

  // メインとなるJavaScriptファイル（エントリーポイント）複数のjsファイルをimportしているファイル
  // 複数になっても良いように連想配列で指定する
  entry: { index: "./src/index.js" },
  // デフォルトでは/main.jsが出力される
  // バンドルの出力先を指定
  output: {
    // dist/js/ に出力する
    path: path.join(__dirname, "dist/js"),
    // ブラウザからバンドルにアクセスする際のjsのパス
    // /js/index.js が出力される
    publicPath: "/js/",
    // [name]の中に、上のエントリーで書いたkey名が入るようになる
    filename: '[name].js',
    // ライブラリモードが有効になり、バンドル main.js にあるexportされたクラスや関数にアクセスできるようになる。
    // umd/amd  https://webpack.js.org/configuration/output/
    libraryTarget: 'umd'
  },

  module: {
    rules: [
      {
        // 拡張子 .js もしくは .jsx の場合
        test: /\.jsx$/,
        use: [
          {
            // Babel を利用する
            loader: 'babel-loader',
            // Babel のオプションを指定する
            options: {
              presets: [
                [
                  // プリセットを指定することで、ES2020 を ES5 に変換
                  // polyfill(ポリフィル=ブラウザが新しい機能に対応していない場合、
                  // それを補う為に古いブラウザでも動作する代替コードをあてがうこと)に関する設定
                  "@babel/preset-env",
                  {
                    // 自動的に必要なポリフィルをインポートしてくれる機能で、
                    // さらに各ファイルでポリフィルが必要な場合でもバンドルしたときには
                    // ポリフィルの読み込みが１回で済むように工夫してくれる
                    useBuiltIns: "entry", // デフォルトはfalse, usage/entry
                    // 市場シェアが0.25％を超えるブラウザーで実行可能な最低限のコード出力
                    targets: "> 0.25%, not dead",
                    // Babel7.4.0からは @babel/polyfill が非推奨になり、代わりにcore-jsのバージョンを指定して直接読み込む方法が提案されています。
                    corejs: 3,
                  }
                ]
              ],
              // JSXを使えるようにする
              plugins: [
                [
                  "@babel/transform-react-jsx",
                  {
                    pragma: "h",
                    pragmaFrag: "Fragment",
                  },
                ],
              ],
            },
          }
        ]
      },
      {
        // 拡張子 .ts もしくは .tsx の場合
        test: /\.tsx?$/,
        // TypeScript をコンパイルする
        use: "ts-loader"
      }
    ]
  },
  // import 文で .ts や .tsx ファイルを解決する
  resolve: {
    extensions: [".ts", ".tsx", ".js", ".jsx"],
  },
  // ソースマップの出力を有効
  devtool: 'inline-source-map'
};
