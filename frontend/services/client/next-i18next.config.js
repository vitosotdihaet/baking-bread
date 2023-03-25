const path = require('path');

module.exports = {
    i18n: {
        defaultLocale: 'ru',
        locales: ['en', 'ru', 'ua'],
    },
    fallbackLng: {
        default: ['ru'],
    },
    localePath:
    typeof window === 'undefined'
        ? path.resolve('./public/locales')
        : '/locales',
    nonExplicitSupportedLngs: true,
    debug: process.env.NODE_ENV === 'development',
};
