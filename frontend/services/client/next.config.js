// const withPlugins = require('next-compose-plugins');
const withBundleAnalyzer = require('@next/bundle-analyzer');
const {
    PHASE_DEVELOPMENT_SERVER,
    PHASE_PRODUCTION_BUILD,
} = require('next/dist/shared/lib/constants');
const buildWebpackConfig = require('./config/build/buildWebpackConfig');
const buildSecurityHeaders = require('./config/next/buildSecurityHeaders');

// @ts-check
const { i18n } = require('./next-i18next.config.js');

module.exports = async (phase, { defaultConfig }) => {
    const isDev = phase === PHASE_DEVELOPMENT_SERVER;
    const isProd = phase === PHASE_PRODUCTION_BUILD;

    const securityHeaders = buildSecurityHeaders();

    /**
     * @type {import('next').NextConfig}
     */
    const nextConfig = {
        i18n,
        compress: true,
        distDir: 'build',
        poweredByHeader: false,
        generateEtags: true,
        httpAgentOptions: {
            keepAlive: true,
        },
        swcMinify: true,
        reactStrictMode: true,
        experimental: {
            appDir: false,
        },
        headers: securityHeaders,
        devIndicators: {
            buildActivity: true,
            buildActivityPosition: 'bottom-right',
        },
        pageExtensions: ['tsx', 'ts'],
        webpack: (config) => buildWebpackConfig(config),
    };

    return withBundleAnalyzer({
        enabled: process.env.ANALYZE === 'true',
        openAnalyzer: false,
    })(nextConfig);
};
