// Not build with webpack
const buildNextSvgLoader = () => {
    /**
     * @type {import('webpack').RuleSetRule}
     */
    // old
    const svgLoader = {
        test: /\.svg$/i,
        issuer: /\.[jt]sx?$/,
        resourceQuery: { not: /url/ },
        use: ['@svgr/webpack'],
    };

    // const svgLoader = {
    //     test: /\.svg$/,
    //     use: [
    //         {
    //             loader: '@svgr/webpack',
    //         },
    //         {
    //             loader: 'file-loader',
    //         },
    //     ],
    //     type: 'javascript/auto',
    //     issuer: {
    //         and: [/\.(ts|tsx|js|jsx|md|mdx)$/],
    //     },
    // };

    // const svgLoader = {
    //     test: /\.svg?$/,
    //     oneOf: [
    //         {
    //             use: [
    //                 {
    //                     loader: '@svgr/webpack',
    //                     options: {
    //                         prettier: false,
    //                         svgo: true,
    //                         svgoConfig: {
    //                             plugins: [
    //                                 {
    //                                     name: 'preset-default',
    //                                     params: {
    //                                         overrides: { removeViewBox: false },
    //                                     },
    //                                 },
    //                             ],
    //                         },
    //                         titleProp: true,
    //                     },
    //                 },
    //             ],
    //             issuer: {
    //                 and: [/\.(ts|tsx|js|jsx|md|mdx)$/],
    //             },
    //         },
    //     ],
    // };

    return svgLoader;
};

module.exports = buildNextSvgLoader;
