// const withPlugins = require('next-compose-plugins');
const withBundleAnalyzer = require('@next/bundle-analyzer');
const {
    PHASE_DEVELOPMENT_SERVER,
    PHASE_PRODUCTION_BUILD,
} = require('next/dist/shared/lib/constants');
const buildWebpackConfig = require('./config/build/buildWebpackConfig');
const buildSecurityHeaders = require('./config/next/buildSecurityHeaders');

withBundleAnalyzer({
    enabled: process.env.ANALYZE === 'true',
});

module.exports = async (phase, { defaultConfig }) => {
    const isDev = phase === PHASE_DEVELOPMENT_SERVER;
    const isProd = phase === PHASE_PRODUCTION_BUILD;

    const securityHeaders = buildSecurityHeaders();

    /**
     * @type {import('next').NextConfig}
     */
    const nextConfig = {
        i18n: {
            locales: ['ru-RU', 'en-US', 'nl-NL'],
            defaultLocale: 'en-US',
            localeDetection: false,
        },
        compress: true,
        distDir: 'build',
        poweredByHeader: false,
        generateEtags: true,
        httpAgentOptions: {
            keepAlive: true,
        },
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
    // TODO: READ ABOUT NEXT ESLINT AND STORYBOOK RULES
    // TODO: READ MORE ABOUT PHASES OF BUILD
    return withBundleAnalyzer({}, nextConfig);
};
