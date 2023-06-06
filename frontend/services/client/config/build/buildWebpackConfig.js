const buildPlugins = require('./buildPlugins');
const buildRules = require('./buildRules');

const buildWebpackConfig = (
    /**
     * @type {import('webpack').Configuration}
     */
    config,
) => {
    buildPlugins(config);
    buildRules(config);
    config.resolve.fallback = { fs: false };

    return config;
};

module.exports = buildWebpackConfig;
