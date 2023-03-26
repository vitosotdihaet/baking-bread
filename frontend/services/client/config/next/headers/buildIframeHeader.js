// Allows to open browser in Iframes
const buildIframeHeader = () => {
    return {
        key: 'X-Frame-Options',
        value: 'SAMEORIGIN',
    };
};

module.exports = buildIframeHeader;
