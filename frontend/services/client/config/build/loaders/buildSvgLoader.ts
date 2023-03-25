import { RuleSetRule } from 'webpack';

export const buildSvgLoader = (): RuleSetRule => {
    return {
        test: /\.svg$/i,
        issuer: /\.[jt]sx?$/,
        use: ['@svgr/webpack'],
    };
};
