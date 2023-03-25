const path = require('path');

/**
 * @type {import('next-i18next').UserConfig}
 */
module.exports = {
    // https://www.i18next.com/overview/configuration-options#logging
    debug: process.env.NODE_ENV === 'development',
    i18n: {
        defaultLocale: 'default',
        locales: ['default', 'en', 'ru'],
    },
    localePath: typeof window === 'undefined' ? path.resolve('./public/locales') : '/locales',
    reloadOnPrerender: process.env.NODE_ENV === 'development',
    // saveMissing: false,
    // strictMode: true,
    // serializeConfig: false,
    // react: { useSuspense: false }
};
