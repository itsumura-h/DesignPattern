const path = require("path");

module.exports = {
  mode: "development",
  devServer: {
    open: true,
    openPage: "index.html",
    contentBase: path.join(__dirname, "public"),
    watchContentBase: true,
    host: "0.0.0.0",
    port: 3000,
  },
  entry: { index: "./src/index.js" },
  output: {
    path: path.join(__dirname, "dist/js"),
    publicPath: "/js/",
    filename: '[name].js',
    libraryTarget: 'umd'
  },

  module: {
    rules: [
      {
        test: /\.jsx$/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: [
                [
                  "@babel/preset-env",
                  {
                    useBuiltIns: "entry",
                    targets: "> 0.25%, not dead",
                    corejs: 3,
                  }
                ]
              ],
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
        test: /\.tsx?$/,
        use: "ts-loader"
      }
    ]
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js", ".jsx"],
  },
  devtool: 'inline-source-map'
};