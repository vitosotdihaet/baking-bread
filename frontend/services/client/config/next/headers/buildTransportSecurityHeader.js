// Allows to use https instead of http
const buildTransportSecurityHeader = () => {
    return {
        key: 'Strict-Transport-Security',
        // 2 years
        value: 'max-age=63072000; includeSubDomains; preload',
    };
};

module.exports = buildTransportSecurityHeader;
