const webpack = require("webpack");
const globby = require("globby");

module.exports = [{
	name: "js",
	entry: globby.sync(["./scripts/app.js", "./layouts/**/*.html"]),
	output: {
		filename: "app.js",
		publicPath: "http://localhost:8090/"
	},
	module: {
		loaders: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loaders: ["react-hot", "babel?presets[]=es2015&presets[]=react"]
			},
			{
				test: /\.scss$/,
				loaders: ["style", "css", "sass"]
			},
			{
				test: /\.html$/,
				loaders: ["file?emitFile=false"]
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
		port: 8090
	}
}]