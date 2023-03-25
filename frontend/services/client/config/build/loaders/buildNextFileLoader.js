const buildNextFileLoader = (
    /**
     * @type {import('webpack').Configuration}
     */
    config,
) => {
    const fileLoaderRule = config.module.rules.find((rule) => rule.test.test?.('.svg'));

    return {
        ...fileLoaderRule,
        test: /\.svg$/i,
        resourceQuery: /url/,
    };
};

module.exports = buildNextFileLoader;
