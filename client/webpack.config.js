const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: {
    tags: './js/tags',
    menus: './js/menus',
    user_edit: './js/user_edit'
  },
  output: {
    path: path.join(__dirname, 'dist'),
    filename: '[name].js'
  },
  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js', '.jsx', '.elm']
  },
  module: {
    loaders: [
      {
        test: /\.jsx$/,
        loader: 'babel',
        query: {
          presets: ['es2015', 'react'],
          plugins: ['transform-class-properties']
        },
        exclude: [/elm-stuff/, /node_modules/]
      },
      {
        test: /\.elm$/,
        exclude: [/elm-stuff/, /node_modules/],
        loader: 'elm-webpack'
      },
      {
        test: /\.css$/,
        loader: ExtractTextPlugin.extract('style-loader', 'css-loader'),
      },
      {
        test: /\.(woff|woff2|eot|ttf|svg)$/,
        loader: 'url'
      }
    ],

    noParse: /\.elm$/
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin({
      name: 'commons',
      chunks: ['users', 'tags'],
      minChunks: 2
    }),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    }),
    new ExtractTextPlugin("styles.css")
  ]
};
