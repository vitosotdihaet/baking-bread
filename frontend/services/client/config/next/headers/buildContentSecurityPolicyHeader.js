const buildContentSecurityPolicyHeader = () => {
    return {
        key: 'Content-Security-Policy',
        // Add value for sources of loading scripts from other services
        value: '', // Политика `CSP`
    };
};

module.exports = buildContentSecurityPolicyHeader;
