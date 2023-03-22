// Disable allow auto-detect content-type for browser
const buildAllowContentTypeHeader = () => {
    return {
        key: 'X-Content-Type-Options',
        value: 'nosniff',
    };
};

module.exports = buildAllowContentTypeHeader;
