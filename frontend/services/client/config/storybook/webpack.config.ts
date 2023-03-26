import webpack from 'webpack';
import path from 'path';
import { buildSvgLoader } from '../build/loaders/buildSvgLoader';

export default ({ config }: { config: webpack.Configuration }) => {
    const srcPath = path.resolve(__dirname, '..', '..', 'src');

    config.resolve?.modules?.push(srcPath);
    config.resolve?.extensions?.push('.ts', '.tsx');

    // eslint-disable-next-line no-param-reassign
    config.module!.rules = config.module!.rules!.map((rule: any) => {
        if (/svg/.test(rule.test as string)) {
            return { ...rule, exclude: /\.svg$/i };
        }

        return rule;
    });

    // Rules
    config.module?.rules.push(buildSvgLoader());

    return config;
};
