const buildPermissionsPolicyHeader = () => {
    return {
        key: 'Permissions-Policy',
        value: 'camera=(), microphone=(), geolocation=()',
    };
};

module.exports = buildPermissionsPolicyHeader;
