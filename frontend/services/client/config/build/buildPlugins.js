const webpack = require('webpack');

const buildPlugins = (config) => {
    const plugins = [new webpack.DefinePlugin()];

    return plugins;
};

module.exports = buildPlugins;
