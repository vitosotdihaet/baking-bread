const buildRules = require('./buildRules');
const buildPlugins = require('./buildPlugins');

const buildWebpackConfig = (
    /**
     * @type {import('webpack').Configuration}
     */
    config,
) => {
    const fileLoaderRule = config.module.rules.find((rule) => rule.test?.test?.('.svg'));
    const fileLoader = {
        ...fileLoaderRule,
        test: /\.svg$/i,
        resourceQuery: /url/,
    };

    config.module.rules.push(fileLoader);
    buildRules(config);
    buildPlugins(config);

    config.resolve.mainFiles.push('index');

    fileLoaderRule.exclude = /\.svg$/i;

    return config;
};

module.exports = buildWebpackConfig;
