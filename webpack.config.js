const webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = [{
	name: "js",
	entry: "./scripts/app.js",
	output: {
		filename: "app.js",
		publicPath: "http://localhost:8081/files/"
	},
	module: {
		loaders: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loaders: ["react-hot", "babel-loader"]
			}
		]
	},
	plugins: [
		new webpack.HotModuleReplacementPlugin(),
		new webpack.ProvidePlugin({
            "React": "react",
            "ReactDOM": "react-dom",
        })
	],
	devServer: {
		hot: true,
		inline: true,
		port: 8081
	}
},{
	name: "css",
	entry: "./styles/all.scss",
	output: {
		filename: "all.css"
	},
	module: {
		loaders: [
			{
				test: /\.scss$/,
				loader: ExtractTextPlugin.extract(["css-loader", "sass-loader"])
			}
		]
	},
    plugins: [
        new ExtractTextPlugin("all.css", {allChunks: false})
    ]
}]