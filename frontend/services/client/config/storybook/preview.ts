import { Preview } from '@storybook/react';
import { I18nDecorator } from '../../src/shared/config/storybook/I18nDecorator';
import { StyleDecorator } from '../../src/shared/config/storybook/StyleDecorator';
import i18n from './i18n';
import '../../src/app/styles/index.scss';

const preview: Preview = {
    parameters: {
        actions: { argTypesRegex: '^on[A-Z].*' },
        controls: {
            matchers: {
                color: /(background|color)$/i,
                date: /Date$/,
            },
        },
    },
    decorators: [StyleDecorator, I18nDecorator(i18n)],
};

export default preview;
