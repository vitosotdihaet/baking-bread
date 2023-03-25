const buildRules = require('./buildRules');
const buildPlugins = require('./buildPlugins');

const buildWebpackConfig = (
    /**
     * @type {import('webpack').Configuration}
     */
    config,
) => {
    buildPlugins(config);
    buildRules(config);

    return config;
};

module.exports = buildWebpackConfig;
