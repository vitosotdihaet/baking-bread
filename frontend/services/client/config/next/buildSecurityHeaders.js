const buildCrossSiteScriptingHeader = require('./headers/buildCrossSiteScriptingHeader');
const buildPrefetchHeader = require('./headers/buildPrefetchHeader');
const buildTransportSecurityHeader = require('./headers/buildTransportSecurityHeader');
const buildPermissionsPolicyHeader = require('./headers/buildPermissionsPolicyHeader');
const buildIframeHeader = require('./headers/buildIframeHeader');
const buildAllowContentTypeHeader = require('./headers/buildAllowContentTypeHeader');
const buildContentSecurityPolicyHeader = require('./headers/buildContentSecurityPolicyHeader');

const buildSecurityHeaders = () => {
    const prefetchHeader = buildPrefetchHeader();
    const transportSecurityHeader = buildTransportSecurityHeader();
    const crossSiteScriptingHeader = buildCrossSiteScriptingHeader();
    const iframeHeader = buildIframeHeader();
    const permissionsPolicyHeader = buildPermissionsPolicyHeader();

    // Optional
    const allowContentTypeHeader = buildAllowContentTypeHeader();
    const contentSecurityPolicyHeader = buildContentSecurityPolicyHeader();

    const optionalSecurityHeaders = [allowContentTypeHeader, contentSecurityPolicyHeader];

    return [
        prefetchHeader,
        transportSecurityHeader,
        crossSiteScriptingHeader,
        iframeHeader,
        permissionsPolicyHeader,
        // ...optionalSecurityHeaders,
    ];
};

module.exports = buildSecurityHeaders;
