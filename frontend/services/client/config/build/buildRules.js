const buildNextSvgLoader = require('./loaders/buildNextSvgLoader');

const buildRules = (
    /**
     * @type {import('webpack').Configuration}
     */
    config,
) => {
    const svgLoader = buildNextSvgLoader();

    config.module.rules.push(svgLoader);
};

module.exports = buildRules;
