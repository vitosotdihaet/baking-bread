const buildRules = require('./buildRules');
const buildPlugins = require('./buildPlugins');

const buildWebpackConfig = (
    /**
     * @type {import('webpack').Configuration}
     */
    config,
) => {
    buildPlugins(config);

    config.resolve.mainFiles.push('index');

    return config;
};

module.exports = buildWebpackConfig;
