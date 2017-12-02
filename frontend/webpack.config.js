const webpack = require('webpack')
const ExtractTextPlugin = require("extract-text-webpack-plugin")
const path = require('path')
const resolve = path.resolve.bind(path, __dirname);
const dev_path = resolve('dist/');
let output;
output = {
    path: dev_path,
    filename: 'js/[name].js',
    publicPath: '/dist/'
};

let commonsPlugin = new webpack.optimize.CommonsChunkPlugin({name: 'common', filename: 'js/common.js'});

module.exports = {
    entry: {
        main: "./src/main.js",
    },
    output: output,
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        'scss': 'vue-style-loader!css-loader!sass-loader',
                    }
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.s?[ac]ss$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: "css-loader!sass-loader"
                })
            },
            {
                test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: "url-loader?limit=10000&mimetype=application/font-woff"
            },
            {test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader"}
        ]
    },
    resolve: {
        //for vue-bulma fix
        extensions: ['*', '.js', '.vue'],
        alias: {
            'vue$': 'vue/dist/vue.common.js'
        }
    },
    plugins: [
        commonsPlugin,
        new ExtractTextPlugin({filename: 'css/[name].css', allChunks: true}),
    ]
};