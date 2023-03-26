// Disable cross-site scripting for old browsers
const buildCrossSiteScriptingHeader = () => {
    return {
        key: 'X-XSS-Protection',
        value: '1; mode=block',
    };
};

module.exports = buildCrossSiteScriptingHeader;
