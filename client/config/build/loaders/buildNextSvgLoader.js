const buildNextSvgLoader = () => {
    /**
     * @type {import('webpack').RuleSetRule}
     */
    const svgLoader = {
        test: /\.svg$/i,
        issuer: /\.[jt]sx?$/,
        resourceQuery: { not: /url/ },
        use: ['@svgr/webpack'],
    };

    return svgLoader;
};

module.exports = buildNextSvgLoader;
