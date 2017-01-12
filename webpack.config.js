const webpack = require('webpack');

module.exports = [{
	name: "js",
	entry: "./scripts/app.js",
	output: {
		filename: "app.js",
		publicPath: "http://localhost:8081/"
	},
	module: {
		loaders: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loaders: ["react-hot", "babel"]
			},
			{
				test: /\.scss$/,
				loaders: ["style", "css", "sass"]
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
}]