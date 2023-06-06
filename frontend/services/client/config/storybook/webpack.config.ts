import path from 'path';
import webpack, { DefinePlugin } from 'webpack';
import { buildSvgLoader } from '../build/loaders/buildSvgLoader';

export default ({ config }: { config: webpack.Configuration }) => {
    const srcPath = path.resolve(__dirname, '..', '..', 'src');

    config.resolve?.modules?.push(srcPath);
    config.resolve?.extensions?.push('.ts', '.tsx');
    config.resolve!.alias = {
        ...config.resolve!.alias,
        'next-i18next': 'react-i18next',
    };

    // eslint-disable-next-line no-param-reassign
    config.module!.rules = config.module!.rules!.map((rule: any) => {
        if (/svg/.test(rule.test as string)) {
            return { ...rule, exclude: /\.svg$/i };
        }

        return rule;
    });

    config.plugins?.push(new DefinePlugin({
        __PROJECT__: JSON.stringify('storybook'),
    }));

    // Rules
    config.module?.rules.push(buildSvgLoader());

    return config;
};
