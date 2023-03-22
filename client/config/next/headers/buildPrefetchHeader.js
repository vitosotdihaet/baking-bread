// Allows browsers to show DNS name for external links, images, css, etc...
const buildPrefetchHeader = () => {
    return {
        key: 'X-DNS-Prefetch-Control',
        value: 'on',
    };
};

module.exports = buildPrefetchHeader;
