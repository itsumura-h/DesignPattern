const path = require("path");

module.exports = {
  mode: "development",
    entry: "./src/index.js",
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
                test: /\.js$/,
                loader: "babel-loader",
            }
        ]
    }
};