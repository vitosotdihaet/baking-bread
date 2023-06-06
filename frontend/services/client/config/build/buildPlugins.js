const webpack = require('webpack');

const buildPlugins = (
    /**
     * @type {import('webpack').Configuration}
     */
    config,
) => {
    config.plugins.push(new webpack.DefinePlugin({
        __PROJECT__: JSON.stringify('production'),
    }));
};

module.exports = buildPlugins;
