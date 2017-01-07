module.exports = {
	entry: "./scripts/app.js",

	output: {
		filename: "app.js",
		path: __dirname + "/files",
	},
	resolve: {
		extensions: ['', '.js']
	},
	module: {
	  	loaders: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loaders: ["babel-loader"]
			}
		]
	}
}